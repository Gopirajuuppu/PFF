import azure.cognitiveservices.speech as speechsdk
import configparser
from dotenv import load_dotenv
import os
from pydub import AudioSegment
from io import BytesIO
import openai
from openai import OpenAI
import prompts
import tempfile
import time

load_dotenv("creds.env")
AZURE_KEY= os.getenv('AZURE_KEY')
AZURE_REGION=os.getenv('AZURE_REGION')
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
openai.api_key = os.environ["OPENAI_API_KEY"]
openAI_client = OpenAI()

config = configparser.ConfigParser()
config.read("./config/config.ini")

#Speech to Text
def perform_speech_to_text(audio_bytes,conversation_id):
    temp_audio_path = './DATA/Speech_To_Text/'+conversation_id+'_temp_audio.wav'    
    
    # Save the audio bytes to a temporary WAV file
    with open(temp_audio_path, "wb") as audio_file:        
        audio_file.write(audio_bytes)
        audio_file.close()

    # Convert the audio to a format supported by Azure Speech
    print("temp_audio_path",temp_audio_path)
    audio = AudioSegment.from_wav(temp_audio_path)
    audio.export(temp_audio_path, format="wav")

    # Perform speech-to-text using Azure Speech
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_KEY, region=AZURE_REGION)
    speech_config.speech_recognition_language=config['SPEECH_TO_TEXT']['speech_recognition_language']
    audio_input = speechsdk.AudioConfig(filename=temp_audio_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    print("Recognizing speech...")
    #time.sleep(1)
    result = speech_recognizer.recognize_once_async().get()
    print("Speech recognized:", result.text)

    # Clean up temporary files
    speech_recognizer.canceled
    del speech_recognizer
    del audio_input
    del audio
    del audio_file
    #del temp_audio_path
    os.remove(temp_audio_path)

    return result.text

#text to speech
def get_tts_audio(agent_response,conversation_id): 
        tone_response = openAI_client.chat.completions.create(
            model = os.getenv('MODEL_NAME'),
            temperature = 0,
            messages = [
                {"role": "system", "content": prompts.TTS_CATEGORIZE_PROMPT},
                {"role": "user", "content": agent_response},
            ]
        )
        tone_response = tone_response.choices[0].message.content
        print("tone for this message",tone_response)

        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription=AZURE_KEY, region=AZURE_REGION)        
        #audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        
        # The neural multilingual voice can speak different languages based on the input text.
        speech_config.speech_synthesis_voice_name=config['TEXT_TO_SPEECH']['speech_synthesis_voice_name']        
        #speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config) 
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)                
        
        text = config['TEXT_TO_SPEECH']['text_to_xml'].replace('{tone_response}', tone_response).replace('{agent_response}', agent_response)        
        xml_file_name = './DATA/Text_To_Speech/'+conversation_id+'_text_tts.xml'
        
        with open(xml_file_name, 'w') as file:
            file.write(text)

        ssml_string = open(xml_file_name, 'r').read()
        result = speech_synthesizer.speak_ssml(ssml_string)
        #result = speech_synthesizer.speak_ssml_async(ssml_string).get()

        stream = speechsdk.AudioDataStream(result)
        audio_file_name = './DATA/Text_To_Speech/'+conversation_id+'_result.wav'
        #Saving this file in /DATA/Text_To_Speech file Directory
        stream.save_to_wav_file(audio_file_name)

        # Read the .wav file
        audio_data=None
        with open(audio_file_name, 'rb') as file:
            audio_data = file.read()

        #return audio_file_name 
        return audio_data     
        