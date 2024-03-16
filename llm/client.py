import streamlit as st
from openai import OpenAI

open_ai_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=open_ai_key)
