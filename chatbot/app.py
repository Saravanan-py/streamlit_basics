from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
import streamlit as st
from langchain_community.llms import Ollama

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. Please response to the user"),
        ("user", "Question:{question}")
    ]
)
st.title("Ollama PYTHON based Chatbot")
text = st.text_input("Type your text: ")
chat = Ollama(model="mistral")
output = StrOutputParser()
chain = prompt | chat | output

if text:
    st.write(f"Question: {text}")
    ans = chain.invoke({"question": text})
    st.write(f"Answer: {ans}")
