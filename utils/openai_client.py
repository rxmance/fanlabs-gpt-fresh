import os
from openai import OpenAI
import streamlit as st  # ✅ Only if you use it later

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)