# import streamlit as st
# st.title("**Hello world**")
# x = st.text_input("This is a hello world text :guide_dog:")
# st.button('click')
# st.write(f'your text is : {x}')

import os

if __name__ =='__main__':
    region = os.environ.get('OPENAI_API_KEY')
    print(region)