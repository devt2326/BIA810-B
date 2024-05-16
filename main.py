import streamlit as st
from streamlit_chat import message
#from dotenv import load_dotenv
import os
from api_key import apikey
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)

def init():
    os.environ["OPENAI_API_KEY"]=apikey
    st.set_page_config(
        page_title="Chat with Dr. Kalam",
    )


def main():
    
    init()

    chat = ChatOpenAI()

    if "messages" not in st.session_state:
        st.session_state.messages=[
            SystemMessage(content="You are Dr. Apj Abdul Kalam and answer all the questions as himslef. Use his tone and vocabulary to answer all the questions")
    ]
    st.header("Chat with Dr. Kalam")
    user_input = st.text_input("Your question", key="user_input")

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Hmm..."):
            response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
 

    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 ==0:
            message(msg.content, is_user=True, key=str(i)+'_user')
        else:
            message(msg.content, is_user=False, key=str(i)+'_ai')
   
if __name__ == '__main__':
    main()