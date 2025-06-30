import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()

# Initialize the Azure OpenAI LLM
llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4",
    temperature=0.7,
)

# Streamlit UI
st.set_page_config(page_title="Azure Chatbot", layout="centered")
st.title("🤖 Azure OpenAI Chatbot")
st.caption("Powered by LangChain & Streamlit")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Say something...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from LLM
    response = llm.invoke(HumanMessage(content=user_input))
    reply = response.content

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
