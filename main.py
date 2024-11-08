import streamlit as st
import os

# Define the pages
pages = {
    "Campus Radio Jockey Text Generator": "page01.py",
    "Text to Speech with PlayHT": "page02.py"
}

# Sidebar for page navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# API key input in the sidebar
st.sidebar.header("Groq API Key")
groq_api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Save the API key as an environment variable if provided
if groq_api_key:
    os.environ["GROQ_API_KEY"] = groq_api_key

# Display the selected page
page = pages[selection]
with open(page) as f:
    code = f.read()
    exec(code)
