from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_community.llms import Ollama


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. Please response to the user"),
        ("user", "Question:{messages}")
    ]
)

st.title("Ollama PYTHON based Chatbot")
text = st.text_input("Type your text: ")
if text:
    chat = Ollama(model="mistral", endpoint="http://localhost:11434/api/generate")
    output = StrOutputParser()
    chain = prompt | chat | output
    ai_response = chain.invoke({'messages':text})
    st.session_state[f"Answer: "] = ai_response
    st.session_state[f"Question: "] = text
    st.write(st.session_state)



