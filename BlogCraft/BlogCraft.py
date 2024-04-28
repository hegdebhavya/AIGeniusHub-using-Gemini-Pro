import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.header('Blog Generator:memo:', divider='rainbow')



model_prompt = """You are a blog generator app designed to create informative and engaging blog posts of approximately 500 words. Given a text input, assess whether it contains coherent and relevant information for a blog post. If the input is too vague, random, or nonsensical, respond with a request for more specific or meaningful information. If the input is appropriate, proceed to generate a detailed blog post discussing the topic provided."""


def get_gemini_response(question, prompt):
    if not question:  
        st.error("Please provide some input before generating content.")
        return None
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([prompt, question])
        return response.text
    except Exception as e:
        st.error(f"Failed to generate content due to an error: {e}")
        return None

def update_button_state():
    st.session_state.button_disabled = not st.session_state.question

question = st.text_input("Topic: ", key="question", on_change=update_button_state)
if "button_disabled" not in st.session_state:
    st.session_state.button_disabled = True 

submit = st.button("Generate Content", disabled=st.session_state.button_disabled)

if submit:
    content = get_gemini_response(question, model_prompt)
    if content:
        st.markdown(content)
