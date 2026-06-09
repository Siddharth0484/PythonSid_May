from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import HumanMessage
from Prompt_templates import system_prompt   # 👈 import it
# 8_Prompt_UI_templates.py

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)

st.header("SID AI Application")

user_input = st.text_input("Enter your question (computer-related only)")

if st.button("Click me"):
    if user_input.strip():
        with st.spinner("Thinking... 🤖"):
            messages = [
                system_prompt,
                HumanMessage(content=user_input)
            ]

            result = model.invoke(messages)

        st.write(result.content)
    else:
        st.warning("Please enter a question first.")
