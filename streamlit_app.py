# Import necessary modules
import streamlit as st
import google.generativeai as genai

# Implement API Key 
genai.configure(api_key="AIzaSyAh6als4-W2zBO5DKFEQpiDYB96zfuKX4o")

# Declaring the prompt 
prompt= st.text_input("Ask me anything:")
submit_button = st.button("Submit")


# Contextualizing the prompt
context_prompt = f"Act as an experienced technical trainer , who focuses in python and machine learning , give proper definitions , points to remember , code examples and summary on the topic {prompt}"

# Creating Model and Testing Prompt
model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content(context_prompt)

if submit_button:
    st.write(response.text)




#pip install streamlit
#pip install goggle-generativeai
# streamlit run app.py 
