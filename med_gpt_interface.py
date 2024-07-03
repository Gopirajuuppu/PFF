from dotenv import load_dotenv
from datetime import datetime
from pprint import pprint
import os
import openai
from openai import OpenAI

from database_utility import SQLiteDatabase
import prompts
import configparser

import azure.cognitiveservices.speech as speechsdk
from tts_stt_utils import perform_speech_to_text,get_tts_audio

load_dotenv("creds.env")
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
openai.api_key = os.environ["OPENAI_API_KEY"]
AZURE_KEY= os.getenv('AZURE_KEY')
AZURE_REGION=os.getenv('AZURE_REGION')


class MedGPT(object):
    
    def __init__(self, db_name, text_conv_table):
        self._db = SQLiteDatabase(db_name)
        self.text_conv_table = text_conv_table
        #self.speech_conv_table = speech_conv_table
        self._client = OpenAI()
        self.system_prompt = prompts.CONVERSATION_INTERFACE_SYSTEM_PROMPT_4        
    
    def init_system_prompt(self, section, questions_list):
        self.section = section
        questions_list = [str(index+1) + ". " + question for index, question in enumerate(questions_list)]
        system_message = self.system_prompt.format(section, "\n".join(questions_list))        
        self.messages = [{"role": "system", "content": system_message}]
    
    def init_system_prompt_prev_conv(self, section, questions_list,prev_questions):
        self.section = section
        system_prompt = prompts.CONVERSATION_INTERFACE_SYSTEM_PROMPT_PREV_CONV
        questions_list = [str(index+1) + ". " + question for index, question in enumerate(questions_list)]
        system_message = system_prompt.format(section, "\n".join(questions_list),prev_questions)            
        self.messages = [{"role": "system", "content": system_message}]
        
        
    def init_conversation_id(self):
        conversation_id = datetime.now().strftime("%d%m%Y%H%M%S")
        return conversation_id 

    #Tex
    def call_llm_text(self, user_name, conversation_id,chat_status,mcq_type):        
        agent_response = self._client.chat.completions.create(
                                                        model=os.getenv('MODEL_NAME'),
                                                        temperature=0.5,
                                                        messages=self.messages
                                                        )
        agent_response = agent_response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": agent_response})    
        #get audio for assistant text #Text To speech(TTS) 
        assistant_audio = get_tts_audio(agent_response,conversation_id)
        self.collect_data(conversation_id,user_name,"assistant",agent_response,chat_status,mcq_type,assistant_audio)
        return agent_response
        
    def chat_text(self, patient_message, user_name, conversation_id, chat_status,mcq_type):
        self.messages.append({"role": "user", "content": patient_message})
        #tts for User message
        user_audio = get_tts_audio(patient_message,conversation_id)
        self.collect_data(conversation_id,user_name,"user",patient_message,chat_status,mcq_type,user_audio)
        agent_response = self.call_llm_text(user_name, conversation_id,chat_status,mcq_type)
        return agent_response  

    #Speech  
    def call_llm_speech(self, user_name, conversation_id,chat_status,mcq_type):        
        agent_response = self._client.chat.completions.create(
                                                        model=os.getenv('MODEL_NAME'),
                                                        temperature=0.5,
                                                        messages=self.messages
                                                        )
        agent_response = agent_response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": agent_response})  
        #get audio for assistant text #Text To speech(TTS) 
        assistant_audio = get_tts_audio(agent_response,conversation_id)        
        self.collect_data(conversation_id,user_name,"assistant",agent_response,chat_status,mcq_type,assistant_audio)
        return agent_response
        
    def chat_speech(self, patient_message, user_name, conversation_id, chat_status,mcq_type,audio_bytes):
        self.messages.append({"role": "user", "content": patient_message})
        agent_response = self.call_llm_speech(user_name, conversation_id,chat_status,mcq_type)
        self.collect_data(conversation_id,user_name,"user",patient_message,chat_status,mcq_type,audio_bytes)        
        return agent_response
    
    #inserting this row of data into converdation log table
    def collect_data(self, conversation_id,user_name,role,message,chat_status,mcq_type,audio_bytes):
        conversation = [str(conversation_id),
                           str(user_name),
                           str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")),
                           role,
                           message,
                           self.section,
                           chat_status,
                           mcq_type,
                           audio_bytes]
        self._db.insert_single_row(self.text_conv_table, conversation)  
        
    def show_messages(self):
        pprint(self.messages)
    
    #Getting previsous Incomplete chat history
    def get_previous_incomplete_chat_history(self,mcq_type):        
        incomplete_chat_hist_query = """ SELECT conversation_id, name, Chat_Type FROM {} GROUP BY conversation_id, name, Chat_Type HAVING Chat_Type = 'chat_incomplete' AND Mcq_Type = '{}' """.format(self.text_conv_table,mcq_type)
        data = self._db.fetch_query(incomplete_chat_hist_query)
        return [conv_id + " | " + name  for conv_id, name, chat_type in data]

    #Getting Selected Previous Conversation history to edit
    def get_prev_conversation_edit(self,prev_chat):    
        conv_id = prev_chat.split("|")[0].strip()        
        query_to_get_conv_chat = "SELECT * FROM {} where Conversation_ID= '{}' ".format(self.text_conv_table,conv_id)
        conv_data = self._db.fetch_query(query_to_get_conv_chat)
        user_name = prev_chat.split("|")[1].strip()
        return conv_id, user_name, conv_data
