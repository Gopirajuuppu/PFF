import os
import traceback
import streamlit as st
import json
import pandas as pd
from database_utility import SQLiteDatabase
from med_gpt_analyzer import AnalyzerUtil, ConversationAnalyzer
from personal_info_extractor import get_personal_details
from config import config

    
def create_checkbox(question, choices, selected_choice):
    #Keeping Bold to the Overall section choice
    if question==st.session_state['questions'][-1]:
        st.markdown("###### {}".format(question), unsafe_allow_html=True)
    else:
        st.write(question)
    for choice in choices:
        if choice == selected_choice:
            st.checkbox(choice, value=True, key=f"{question}-{choice}")
        else:
            st.checkbox(choice, key=f"{question}-{choice}")

            
@st.cache_resource(show_spinner="Loading Pipeline")
def get_analyzer_objects():
    db_name = "./DB/form_fill.db"    
    conversation_table = "conversation_log_table"
    analyzer_table = "analyzed_conversation"
    analyzer_util = AnalyzerUtil(db_name, conversation_table)    
    conversation_analyzer = ConversationAnalyzer(db_name, conversation_table, analyzer_table)    
    return analyzer_util, conversation_analyzer

st.set_page_config(page_title="Analyze Conversation", page_icon="📊")

st.markdown("# Analyze Conversation 📊")
st.sidebar.header("Analyze Conversation")
st.write("""Select a conversation for analysing""")

# Initialize Analyzer Object
analyzer_util, conversation_analyzer = get_analyzer_objects()
analyzer_util.update_chatType()

conversation_id_and_name = analyzer_util.get_conversation_id_and_name()
conversation_id_option = st.selectbox('Please select the conversation', conversation_id_and_name,index=None)

if conversation_id_option:
    conversation_id = conversation_id_option.split("|")[0].strip()
    #st.session_state["qa_messages"] = analyzer_util.get_conversation(conversation_id)
    conversation_history = analyzer_util.get_conversation(conversation_id)    

    with st.expander("Conversation"):
        #st.markdown(st.session_state["qa_messages"], unsafe_allow_html=True)
        st.markdown(conversation_history, unsafe_allow_html=True)

    if st.sidebar.button("Analyze Conversation"):
        st.session_state["analysis_found"], st.session_state["analysis"], st.session_state["choices"] = conversation_analyzer.get_analyzed_conversation(conversation_id_option)
        if not st.session_state["analysis_found"]:
            with st.spinner('Please wait while we analyze...'):
                try:
                    st.session_state["analysis"], st.session_state["choices"],personal_info_df,final_summary = conversation_analyzer(conversation_id_option)
                except Exception as error:
                    st.error("We've encountered an internal error! Please refresh the page and try again.", icon="🚨")
                    print("="*70)
                    traceback.print_exc()
                    print("="*70)

        st.markdown("### Analysis", unsafe_allow_html=True)
        for section, summary in st.session_state["analysis"].items():
            # Adding personal info in the page
            if section == "PERSONAL_INFORMATION":
                st.markdown("##### Personal Information", unsafe_allow_html=True) 
                user_info = get_personal_details(summary)                                               
                personal_info_df = pd.DataFrame.from_dict(data=user_info,orient='index',columns=['Personal Info'])
                st.dataframe(personal_info_df)
            else:
                with st.expander("Section: {}".format(section)):
                    st.markdown(summary, unsafe_allow_html=True)                        

        st.markdown("### Form Questionnaire", unsafe_allow_html=True)
        all_section_questions_and_choices = dict()

        db_name = "./DB/form_fill.db" 
        conversation_table = "conversation_log_table"
        data_base = SQLiteDatabase(db_name)
        query_to_get_mcq_type = """ select Mcq_Type from {} WHERE conversation_id='{}' """.format(conversation_table,conversation_id)
        mcq_type = data_base.fetch_query(query_to_get_mcq_type)[0][0]

        with st.expander("Questionnaire 📝"):            
            for idx1, (section, report) in enumerate(st.session_state["choices"].items()):
                st.markdown("##### Section: {}".format(section), unsafe_allow_html=True)
                #We are taking only over all section rating for phq9 as there is only one question in each section
                if mcq_type=="PHQ9":
                    questions = list(report['choice_summary'].keys())[-1]
                    st.session_state['questions'] = questions
                    selected_choices = list(report['choice_summary'].values())[-1]                   
                    all_choices = report['all_choices']                
                    all_section_questions_and_choices[section] = {"questions": [questions], "selected_choices": [selected_choices], "all_choices": all_choices}                    
                    create_checkbox(questions, all_choices, selected_choices)
                    st.markdown("<hr style='border:1px solid white'>", unsafe_allow_html=True)
                else:
                    questions = list(report['choice_summary'].keys())
                    st.session_state['questions'] = questions
                    selected_choices = list(report['choice_summary'].values())
                    all_choices = report['all_choices']                
                    all_section_questions_and_choices[section] = {"questions": questions, "selected_choices": selected_choices, "all_choices": all_choices}
                    for i, question in enumerate(questions):
                        create_checkbox(question, all_choices, selected_choices[i])
                    st.markdown("<hr style='border:1px solid white'>", unsafe_allow_html=True)
            
            #Adding Final Summary            
            if st.session_state["choices"]:                
                final_summary= conversation_analyzer.get_final_summary(mcq_type,st.session_state["choices"])
                st.markdown("### Final Choice Summary", unsafe_allow_html=True) 
                st.write(final_summary)            

        output_docx = conversation_analyzer.generate_docx(all_section_questions_and_choices, st.session_state["analysis"], conversation_id, personal_info_df, final_summary)
        with open(output_docx, "rb") as file_obj:
            st.session_state["file_bin_data"] = file_obj.read()
        _ = os.remove(output_docx) if os.path.exists(output_docx) else None
        btn = st.download_button(
                label="Download Form Docx",
                data=st.session_state["file_bin_data"],
                file_name=output_docx,
                mime="application/octet-stream"
              )
    
    #Adding Delete Tab to Remove selected conversation
    delete_column, reset_column = st.sidebar.columns(2)    
    delete_button = delete_column.button("Delete",key="Delete Conversation")
    if delete_button:                
        selected_conversation_id = conversation_id
        db =SQLiteDatabase(config.db_name)                
        #deleting from conversation table and analyzer table
        db.update_query(""" DELETE FROM {} WHERE conversation_id='{}' """.format(config.conversation_table,selected_conversation_id))
        db.update_query(""" DELETE FROM {} WHERE conversation_id='{}' """.format(config.analyzer_table,selected_conversation_id))
        print("Deleted the selected conversation...",selected_conversation_id )        
        reset_column.button("Reset")
        
