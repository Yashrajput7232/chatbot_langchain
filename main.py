import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from streamlit_chat import message
def init():
    load_dotenv()
    
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print(os.getenv("OPENAI_API_KEY"),"OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")
    st.set_page_config(page_title=" Your Own chat bot ",
                       page_icon="🤖")

def main():
    init()
    st.header("Welcome to Your own Assistant 🤖")
    chat =ChatOpenAI(temperature=0.5)
    if "messages" not in st.session_state:
        st.session_state.messages=[
            SystemMessage(content="you are a helpfull assistant")
        ]
    with st.sidebar:
            user_input = st.text_input("Your message: ", key="user_input")

            # handle user input
            if user_input:
                st.session_state.messages.append(HumanMessage(content=user_input))
                # with st.spinner("Thinking..."):
                response = chat(st.session_state.messages)
                st.session_state.messages.append(AIMessage(content=response.content))

        # display message history
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')


if __name__=="__main__":
    main()