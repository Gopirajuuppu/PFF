import streamlit as st
import json
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
import io
import os
import prompts
import time
from med_gpt_interface import MedGPT
from tts_stt_utils import perform_speech_to_text,get_tts_audio
import azure.cognitiveservices.speech as speechsdk
import threading
from dotenv import load_dotenv
from database_utility import SQLiteDatabase
from config import config

print(load_dotenv("creds.env"))
AZURE_KEY= os.getenv('AZURE_KEY')
AZURE_REGION=os.getenv('AZURE_REGION')

@st.cache_resource(show_spinner="Loading Conversation Pipeline")
def get_conversation_object():
    db_name = "./DB/form_fill.db"    
    conversation_table = "conversation_log_table"    
    med_gpt = MedGPT(db_name, conversation_table)
    return med_gpt 

def recognize_speech(stop_event, output_placeholder):
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_KEY, region=AZURE_REGION)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    st.write("Listening...")
    while not stop_event.is_set():        
        result = speech_recognizer.recognize_once()
        #result = speech_recognizer.start_continuous_recognition_async() 
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            current_speech = result.text
            st.session_state['STT_TEXT'] += ' '+ current_speech
            speech_text=''
            with output_placeholder:
                st.write("You said:", current_speech)
            speech_text = speech_text+' '+current_speech           
            st.write(speech_text) 
        elif result.reason == speechsdk.ResultReason.NoMatch:
            with output_placeholder:
                st.write("No speech could be recognized")
        elif result.reason == speechsdk.ResultReason.Canceled:
            with output_placeholder:
                st.write("Speech recognition canceled: {}".format(result.cancellation_details.reason))
            break 
       
    
def get_stt_live_text(stop_event, output_placeholder):
    # Placeholder for displaying recognized speech    
    if 'STT_TEXT' not in st.session_state:
        st.session_state['STT_TEXT']='' 
    if not stop_event.is_set():
        stop_event.clear()                           
        recognize_speech(stop_event, output_placeholder) 
    return st.session_state['STT_TEXT'] 

st.set_page_config(page_title="Premedical Chat Form", page_icon="🗣️")
med_gpt = get_conversation_object()

st.markdown("# Premedical Chat Form")
medical_questions_types=['PROMIS-29','MADRS', 'PHQ9']
    
def clear_cache():
    keys = list(st.session_state.keys())
    for key in keys:
        st.session_state.pop(key)

mcq_selection = st.sidebar.radio(
    'Select Mcq',
    medical_questions_types,
    index=None,    
    )
questionary_json_file=''
if mcq_selection == medical_questions_types[0]:    
    questionary_json_file = './DATA/Questions/promis.json'
       
elif mcq_selection == medical_questions_types[1]:    
    questionary_json_file = './DATA/Questions/madrs.json'  

elif mcq_selection == medical_questions_types[2]:        
    questionary_json_file = './DATA/Questions/phq9.json'

if questionary_json_file:
    st.sidebar.write("You have Selected ",mcq_selection)
    
    # If you are selecting MCQ for the first time in the session
    if 'MCQ_TYPE' not in st.session_state:
        st.session_state['MCQ_TYPE'] = mcq_selection
    # If you are selecting another MCQ in the same session
    if st.session_state['MCQ_TYPE'] != mcq_selection:
        clear_cache()
        st.session_state['MCQ_TYPE'] = mcq_selection
        #st.sidebar.button("Reset Conversation")           

    #st.sidebar.header("Premedical Chat Form")
    chat_types=['New Chat', 'Previous Chats']
    chat_selection = st.sidebar.selectbox(
        'Select Chat',
        chat_types,
        index=None,
        placeholder="Select any Chat",
        key=st.session_state['MCQ_TYPE'],
        )

    # New Chat
    if chat_selection == chat_types[0]:       
        st.write("""Converse with our AI agent before visiting doctor""")    
        if user_name := st.text_input('Conversation Name'):                
            
            #Adding Chat Introduction
            with st.chat_message("assistant"):
                st.markdown(prompts.INTRODUCTION_MESSAGE)
                
            if "qa_messages" not in st.session_state or len(st.session_state["qa_messages"]) == 0 or st.sidebar.button("Reset Conversation"):
                # Initialized chat input disablity as False
                st.session_state["disabled"] = False
                # Set Message History
                st.session_state["qa_messages"] = []
                # Set Section Count
                st.session_state["section_count"] = 0
                st.session_state["conversation_id"] = med_gpt.init_conversation_id()        
                st.session_state["conversation_name"] = user_name
                st.session_state["chat_status"] = "chat_incomplete"
                # Set Questions Data
                with open(questionary_json_file) as jobj:
                    st.session_state["questions_data"] = json.load(jobj)
                section_name = list(st.session_state["questions_data"][st.session_state["section_count"]].keys())[0]            
                questions_list = st.session_state["questions_data"][st.session_state["section_count"]][section_name]["questions"]            
                # Initialize MedGPT
                med_gpt.init_system_prompt(section_name, questions_list)            
                conversation_id = st.session_state["conversation_id"] 
                print("User Name: {} | Conversation ID: {}".format(user_name, conversation_id))                          
            
            # Display chat messages from history on app rerun
            for qa_message in st.session_state.qa_messages:        
                with st.chat_message(qa_message["role"]):
                    st.markdown(qa_message["content"])         
            
            #User Speech input from the Mic          
            audio_bytes = audio_recorder(icon_size= '2x',pause_threshold=2, key=st.session_state["conversation_id"])               
            
            # React to user text input             
            user_manual_query = st.chat_input("Response..", disabled=st.session_state["disabled"])
            if user_manual_query:                         
                with st.chat_message("user"):
                    st.markdown(user_manual_query)
                    st.session_state.qa_messages.append({"role": "user", "content": user_manual_query})
                conversation_id = st.session_state["conversation_id"]
                chat_status = st.session_state["chat_status"]
                agent_response = med_gpt.chat_text(user_manual_query, user_name, conversation_id, chat_status,st.session_state['MCQ_TYPE'])                
                print("User Response: ",user_manual_query)
                print("Agent Response: ",agent_response)

                if "<END_CONVERSATION>" in agent_response and st.session_state["section_count"] == len(st.session_state["questions_data"])-1:
                    st.session_state["disabled"] = True
                    with st.chat_message("assistant"):
                        interim_agent_response = agent_response.replace("<END_CONVERSATION>", "").strip(" \n")
                        if interim_agent_response:
                            interim_agent_response += " Thank you for your answers. Hope you have a good rest of your day."
                        else:
                            interim_agent_response = "Thank you for your answers. Hope you have a good rest of your day."
                        st.markdown(interim_agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": "Thank you for conversing with me."})
                    user_name = None
                    st.session_state["chat_status"] = "chat_completed"
                elif "<END_CONVERSATION>" in agent_response and st.session_state["section_count"] < len(st.session_state["questions_data"])-1:
                    st.session_state["section_count"] += 1
                    section_name = list(st.session_state["questions_data"][st.session_state["section_count"]].keys())[0]                
                    questions_list = st.session_state["questions_data"][st.session_state["section_count"]][section_name]["questions"]
                    print(questions_list)
                    med_gpt.init_system_prompt(section_name, questions_list)
                    with st.chat_message("assistant"):
                        interim_agent_response = agent_response.replace("<END_CONVERSATION>", "").strip(" \n")
                        if interim_agent_response:
                            interim_agent_response += " Now let's move to the next section."
                        else:
                            interim_agent_response = "Thank you for your answers. Now let's move to the next section."
                        st.markdown(interim_agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": "Okay let's move to the next section."})
                else:
                    # Display assistant response in chat message container
                    with st.chat_message("assistant"):
                        st.markdown(agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": agent_response})
                
                #Text To speech (TTS)           
                new_chat_audio_start_time = time.time()                
                #audio_data = get_tts_audio(agent_response,conversation_id) 
                audio_file_name = './DATA/Text_To_Speech/'+conversation_id+'_result.wav'
                st.audio(audio_file_name)
                new_chat_audio_end_time = time.time() 
                #print("-- Time Taken(in Seconds) to get the Audio response for the User input text:",round(new_chat_audio_end_time-new_chat_audio_start_time,3))
            
            #speech to text (STT)                                
            #new_chat_speech_start_time = time.time()         
            elif audio_bytes: 
                print("Type of the audio bytes---",type(audio_bytes))           
                audio_text = perform_speech_to_text(audio_bytes,st.session_state["conversation_id"])
                if audio_text:
                    #del audio_bytes
                    with st.chat_message("user"):
                        st.markdown(audio_text)
                        st.session_state.qa_messages.append({"role": "user", "content": audio_text})
                conversation_id = st.session_state["conversation_id"]
                chat_status = st.session_state["chat_status"]            
                agent_response = med_gpt.chat_speech(audio_text, user_name, conversation_id, chat_status,st.session_state['MCQ_TYPE'],audio_bytes)  
                print("---- Agen Response--",agent_response)
                
                new_chat_speech_end_time = time.time() 
                #print("-- Time Taken(in Seconds) to get the speech to text response for the User input Speech:",round(new_chat_speech_end_time-new_chat_speech_start_time,3))          

                if "<END_CONVERSATION>" in agent_response and st.session_state["section_count"] == len(st.session_state["questions_data"])-1:
                    st.session_state["disabled"] = True
                    with st.chat_message("assistant"):
                        interim_agent_response = agent_response.replace("<END_CONVERSATION>", "").strip(" \n")
                        if interim_agent_response:
                            interim_agent_response += " Thank you for your answers. Hope you have a good rest of your day."
                        else:
                            interim_agent_response = "Thank you for your answers. Hope you have a good rest of your day."
                        st.markdown(interim_agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": "Thank you for conversing with me."})
                    user_name = None
                    st.session_state["chat_status"] = "chat_completed"
                elif "<END_CONVERSATION>" in agent_response and st.session_state["section_count"] < len(st.session_state["questions_data"])-1:
                    st.session_state["section_count"] += 1
                    section_name = list(st.session_state["questions_data"][st.session_state["section_count"]].keys())[0]
                    questions_list = st.session_state["questions_data"][st.session_state["section_count"]][section_name]["questions"]
                    med_gpt.init_system_prompt(section_name, questions_list)
                    with st.chat_message("assistant"):
                        interim_agent_response = agent_response.replace("<END_CONVERSATION>", "").strip(" \n")
                        if interim_agent_response:
                            interim_agent_response += " Now let's move to the next section."
                        else:
                            interim_agent_response = "Thank you for your answers. Now let's move to the next section."
                        st.markdown(interim_agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": "Okay let's move to the next section."})
                else:
                    # Display assistant response in chat message container
                    with st.chat_message("assistant"):
                        st.markdown(agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": agent_response})
                
                #Text To speech(TTS)
                #audio_data = get_tts_audio(agent_response,st.session_state["conversation_id"])
                audio_file_name = './DATA/Text_To_Speech/'+st.session_state["conversation_id"]+'_result.wav'
                st.audio(audio_file_name)        

    # Previsous Chats or Incomplete chat conversations          
    elif chat_selection == chat_types[1]:
        st.write('You selected:', chat_selection)
        # Float feature initialization
        #float_init()
        incomplete_chat_list = med_gpt.get_previous_incomplete_chat_history(st.session_state['MCQ_TYPE'])    
        prev_chat = st.sidebar.radio("Choose a previous chat",
                                incomplete_chat_list,
                                index=None,                             
                                )  
        
        st.session_state["qa_messages"] = []
        if prev_chat:        
            conv_id, user_name, conv_data = med_gpt.get_prev_conversation_edit(prev_chat)
            st.write("Conversation Name")
            st.info(prev_chat)  

            #Adding Delete Tab to Remove selected conversation
            delete_column, reset_column = st.sidebar.columns(2)            
            delete_button = delete_column.button("Delete",key="Delete Conversation")
            if delete_button:                
                selected_conversation_id = conv_id
                db =SQLiteDatabase(config.db_name)                
                #deleting from conversation table and analyzer table
                db.update_query(""" DELETE FROM {} WHERE conversation_id='{}' """.format(config.conversation_table,selected_conversation_id))
                db.update_query(""" DELETE FROM {} WHERE conversation_id='{}' """.format(config.analyzer_table,selected_conversation_id))
                print("Deleted the selected conversation...",selected_conversation_id )                
                reset_column.button("Reset")
            
            #Making Chat Introduction
            with st.chat_message("assistant"):
                st.markdown(prompts.INTRODUCTION_MESSAGE)

            prev_conv_questions =[] 
            for conv in conv_data:
                if conv[3] == 'assistant':                
                    prev_conv_questions.append(conv[4])
            
            # appending previous chat to session        
            #if "qa_messages" not in st.session_state:
            if len(st.session_state["qa_messages"]) == 0:
                #st.session_state["qa_messages"] = []
                for con_chat in conv_data:
                    if con_chat[3]=='user':
                        st.session_state.qa_messages.append({"role": "user", "content": con_chat[4]})
                    else:
                        st.session_state.qa_messages.append({"role": "assistant", "content": con_chat[4]})        
            
            if 'conversation_id' in st.session_state:
                print("Existing Conversation ID in the session is :",st.session_state["conversation_id"])
                print("Selected Conversation ID from the Previsous Chat is: ",conv_id)
            
            if "section_count" not in st.session_state or st.session_state["conversation_id"]!=conv_id :
                st.session_state["disabled"] = False
                st.session_state["conversation_id"] = conv_id        
                st.session_state["conversation_name"] = user_name
                st.session_state["chat_status"] = "chat_incomplete"
                last_section_name=conv_data[-1][5] 

                # Set Questions Data
                with open(questionary_json_file) as jobj:
                    st.session_state["questions_data"] = json.load(jobj)
                st.session_state["section_count"] = next(ind for ind, section_name in enumerate(st.session_state["questions_data"]) if last_section_name in section_name)
                questions_list = st.session_state["questions_data"][st.session_state["section_count"]][last_section_name]["questions"]                
                # Initialize MedGPT
                med_gpt.init_system_prompt_prev_conv(last_section_name, questions_list, prev_conv_questions)                
                conversation_id = st.session_state["conversation_id"] 
                print("User Name: {} | Conversation ID: {}".format(user_name, conversation_id))

            # Display chat messages from history on app rerun
            for qa_message in st.session_state.qa_messages:        
                with st.chat_message(qa_message["role"]):
                    st.markdown(qa_message["content"])
            
            #Streamlit Audio Mic
            audio_bytes = audio_recorder(key=st.session_state["conversation_id"],icon_size= '2x',pause_threshold= 1.5)  
            #Edit the Previsous chat and React to user input 
            agent_response=''                        
            user_manual_query = st.chat_input("Response..", disabled=st.session_state["disabled"])  
            if user_manual_query : 
                with st.chat_message("user"):
                    st.markdown(user_manual_query)
                    st.session_state.qa_messages.append({"role": "user", "content": user_manual_query})
                conversation_id = st.session_state["conversation_id"]
                chat_status = st.session_state["chat_status"]            
                agent_response = med_gpt.chat_text(user_manual_query, user_name, conversation_id, chat_status,st.session_state['MCQ_TYPE'])
                print("User Response: ",user_manual_query)
                print("Agent Response: ",agent_response)
                #print('Last Section name is: ', last_section_name)                 

                if "<END_CONVERSATION>" in agent_response and st.session_state["section_count"] == len(st.session_state["questions_data"])-1:
                    st.session_state["disabled"] = True
                    with st.chat_message("assistant"):
                        interim_agent_response = agent_response.replace("<END_CONVERSATION>", "").strip(" \n")
                        if interim_agent_response:
                            interim_agent_response += " Thank you for your answers. Hope you have a good rest of your day."
                        else:
                            interim_agent_response = "Thank you for your answers. Hope you have a good rest of your day."
                        st.markdown(interim_agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": "Thank you for conversing with me."})
                    user_name = None
                    st.session_state["chat_status"] = "chat_completed"
                elif "<END_CONVERSATION>" in agent_response and st.session_state["section_count"] < len(st.session_state["questions_data"])-1:
                    st.session_state["section_count"] += 1
                    section_name = list(st.session_state["questions_data"][st.session_state["section_count"]].keys())[0]                
                    questions_list = st.session_state["questions_data"][st.session_state["section_count"]][section_name]["questions"]                
                    med_gpt.init_system_prompt_prev_conv(section_name, questions_list, prev_conv_questions)
                    with st.chat_message("assistant"):
                        interim_agent_response = agent_response.replace("<END_CONVERSATION>", "").strip(" \n")
                        if interim_agent_response:
                            interim_agent_response += " Now let's move to the next section."
                        else:
                            interim_agent_response = "Thank you for your answers. Now let's move to the next section."
                        st.markdown(interim_agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": "Okay let's move to the next section."})
                else:
                    # Display assistant response in chat message container
                    with st.chat_message("assistant"):
                        st.markdown(agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": agent_response})
                
                #Text To speech (TTS)
                print("Agent Response of text before making to Audio--",agent_response)
                #audio_data = get_tts_audio(agent_response,st.session_state["conversation_id"])
                audio_file_name = './DATA/Text_To_Speech/'+conversation_id+'_result.wav'
                st.audio(audio_file_name)
            
            ## Speech to text (STT)                                   
            elif audio_bytes:                
                audio_text = perform_speech_to_text(audio_bytes,st.session_state["conversation_id"])            
                if audio_text:                                       
                    with st.chat_message("user"):
                        st.markdown(audio_text)
                    st.session_state.qa_messages.append({"role": "user", "content": audio_text})
                conversation_id = st.session_state["conversation_id"]
                chat_status = st.session_state["chat_status"]            
                agent_response = med_gpt.chat_speech(audio_text, user_name, conversation_id, chat_status,st.session_state['MCQ_TYPE'],audio_bytes)  
                print("Agen Response--",agent_response)          

                if "<END_CONVERSATION>" in agent_response and st.session_state["section_count"] == len(st.session_state["questions_data"])-1:
                    st.session_state["disabled"] = True
                    with st.chat_message("assistant"):
                        interim_agent_response = agent_response.replace("<END_CONVERSATION>", "").strip(" \n")
                        if interim_agent_response:
                            interim_agent_response += " Thank you for your answers. Hope you have a good rest of your day."
                        else:
                            interim_agent_response = "Thank you for your answers. Hope you have a good rest of your day."
                        st.markdown(interim_agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": "Thank you for conversing with me."})
                    user_name = None
                    st.session_state["chat_status"] = "chat_completed"
                elif "<END_CONVERSATION>" in agent_response and st.session_state["section_count"] < len(st.session_state["questions_data"])-1:
                    st.session_state["section_count"] += 1
                    section_name = list(st.session_state["questions_data"][st.session_state["section_count"]].keys())[0]
                    questions_list = st.session_state["questions_data"][st.session_state["section_count"]][section_name]["questions"]
                    med_gpt.init_system_prompt(section_name, questions_list)
                    with st.chat_message("assistant"):
                        interim_agent_response = agent_response.replace("<END_CONVERSATION>", "").strip(" \n")
                        if interim_agent_response:
                            interim_agent_response += " Now let's move to the next section."
                        else:
                            interim_agent_response = "Thank you for your answers. Now let's move to the next section."
                        st.markdown(interim_agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": "Okay let's move to the next section."})
                else:
                    # Display assistant response in chat message container
                    with st.chat_message("assistant"):
                        st.markdown(agent_response)
                    st.session_state.qa_messages.append({"role": "assistant", "content": agent_response})
                
                #Text To speech (TTS)
                print("Agent Response speech before making to Audio--",agent_response)
                #audio_data = get_tts_audio(agent_response,st.session_state["conversation_id"])
                audio_file_name = './DATA/Text_To_Speech/'+conversation_id+'_result.wav'
                st.audio(audio_file_name)
            
            # Float the footer container and provide CSS to target it with
            #footer_container.float("bottom: 0rem;")
        
            
            