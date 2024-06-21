# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# import streamlit as st
# from langchain_community.llms import Ollama
#
#
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "you are a helpful assistant. Please response to the user"),
#         ("user", "Question:{messages}")
#     ]
# )
# chat = Ollama(model="mistral")
# output = StrOutputParser()
# chain = prompt | chat | output
#
# st.title("Ollama PYTHON based Chatbot")
# text = st.text_area("Type your text: ")
# if st.button("Generate"):
#     if text:
#         with st.spinner("Generating response.."):
#             st.write(chain.invoke({'messages':text}))
#
# # if text:
# #     chat = Ollama(model="mistral")
# #     output = StrOutputParser()
# #     chain = prompt | chat | output
# #     ai_response = chain.invoke({'messages':text})
# #     st.session_state[f"Question: "] = text
# #     st.session_state[f"Answer: "] = ai_response
# #     st.write(st.session_state
#
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_community.llms import Ollama

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user"),
        ("user", "Question: {messages}")
    ]
)

st.title("Ollama PYTHON based Chatbot")
text = st.text_input("Type your text: ")

# Initialize chat history in session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if text:
    try:
        chat = Ollama(model="mistral")
        output = StrOutputParser()
        chain = prompt | chat | output

        # Add user message to chat history
        st.session_state.chat_history.append(("user", text))

        # Invoke the chain with chat history messages
        messages = [{"role": role, "content": content} for role, content in st.session_state.chat_history]
        ai_response = chain.invoke({'messages': messages})

        # Add AI response to chat history
        st.session_state.chat_history.append(("assistant", ai_response))

        # Display the conversation
        for role, content in st.session_state.chat_history:
            if role == "user":
                st.write(f"Q: {content}")
            else:
                st.write(f"A: {content}")

        # Optionally, clear the text input after submission
        st.text_input("Type your text: ", value="", key="text_input")

    except Exception as e:
        st.error(f"An error occurred: {e}")



