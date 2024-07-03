import os
import streamlit as st
from med_gpt_analyzer import AnalyzerUtil, ConversationAnalyzer
from database_utility import SQLiteDatabase

@st.cache_resource(show_spinner="Loading Pipeline")
def get_analyzer_objects():
    db_name = "./DB/form_fill.db"    
    conversation_table = "conversation_log_table"
    analyzer_table = "analyzed_conversation"
    analyzer_util = AnalyzerUtil(db_name, conversation_table)    
    conversation_analyzer = ConversationAnalyzer(db_name, conversation_table, analyzer_table)    
    return analyzer_util, conversation_analyzer
#Updating the chat type
analyzer_util, conversation_analyzer = get_analyzer_objects()
analyzer_util.update_chatType()
conversation_list = analyzer_util.get_conversation_id_and_name()
print("Completed conversation list is---",conversation_list)

#conversation_list =['conv1','conv2','conv3'] # get the completed conv list from the DB
selected_conv_id = st.selectbox('Please select the conversation', conversation_list,index=None)


if selected_conv_id:
    st.write("You have selected - ",selected_conv_id) 
    conversation_id = selected_conv_id.split("|")[0].strip()
    #Audio files will be save in the local directory ./DATA/Audio_Files/'+selected_conv_id
    analyzer_util.get_audio_data(conversation_id)

tab1, tab2 = st.tabs(["speech analytics", "Speech Dynamics"])

def adding(a,b,c):
    d= a+b+c
    st.write('Addition',d)
    return d
def multi(a,b,c):
    d =  a*b*c
    st.write('Multiplication',d)
    return d


with tab1:
    st.header("speech analytics") 
    adding(10,20,30)  

with tab2:
    st.header("Speech Dynamics")
    multi(15,25,35)
    
