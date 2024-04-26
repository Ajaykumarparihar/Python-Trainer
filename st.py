import streamlit as st
# input fieldcreate a text 

user_input = st.text_input("Ask me anything:")
# create as submit button

submit_button = st.button("Submit")


if submit_button:
    chatbot_response = "Hello, World!"
    st.write(chatbot_response)