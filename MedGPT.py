import streamlit as st

st.set_page_config(
    page_title="MedGPT",
    page_icon="🩺",
)

st.write("# Welcome to MedGPT 🩺 - Pre-Medical Checkup Form Filling! 🗒️📝")

# st.sidebar.success("Success")

st.markdown(
    """
    # How to Use the Application

## Chat Application
1. Click on the 🤖 **Chat Premedical Form** from the side bar.
2. Provide a name for the conversation and press enter.
3. Chat simply with our medical agent and answer the questions.
4. End the conversation.
5. To start a new conversation, click on **Reset Conversation** from the side bar.
6. To change the name, provide a new name and then click **Reset Conversation** again from the side bar.

## Analyze Chat
1. Click on the 📊 **Analyze Conversation** from the side bar.
2. Select the conversation ID from the dropdown menu.
3. Click on **Analyze Conversation** from the side bar.
4. You will receive all the analysis for the selected conversation.
5. Click on the **Download DOCX** button to download the form as a Word document.

"""
)