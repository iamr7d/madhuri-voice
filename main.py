import streamlit as st

# Define the pages
pages = {
    "Campus Radio Jockey Text Generator": "page01.py",
    "Text to Speech with PlayHT": "page02.py"
}

# Sidebar for page navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
with open(page) as f:
    code = f.read()
    exec(code)
