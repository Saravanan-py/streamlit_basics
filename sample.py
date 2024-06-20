import streamlit as st

st.title("Sample title")
text = st.text_input("Enter your key: ")
text1 = st.text_input("Enter your value: ")
if text and text1:
    st.session_state[text] = text1
    st.write(st.session_state)
