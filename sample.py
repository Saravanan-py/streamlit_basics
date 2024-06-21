import streamlit as st

st.title("Sample title")
prompt = st.chat_input("ask for anything...")
if prompt:
    with st.chat_message('assistant'):
        st.markdown(prompt)