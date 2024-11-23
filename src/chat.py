import streamlit as st
import pandas as pd
import numpy as np 
import spacy
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.agents import AgentExecutor, create_tool_calling_agent


# Load the spacy model
embeddings = SpacyEmbeddings(model_name="en_core_web_sm")

def get_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks


def vector_store(text_chunks):
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_db")


def get_conversational_chain(tools,ques):

    # Import OpenAI token from toml file
    openai_api = st.secrets["OPENAI_API_TOKEN"]

    if not openai_api:
        st.sidebar.error('API key is missing. Please set the OPENAI_API_TOKEN in the /src/.streamlit/secrets.toml file.')
        return None
    
    #os.environ["ANTHROPIC_API_KEY"]=os.getenv["ANTHROPIC_API_KEY"]
    #llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0, api_key=os.getenv("ANTHROPIC_API_KEY"),verbose=True)
    try:
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, api_key=openai_api, verbose=True)
    except Exception as e:
        st.sidebar.error(f'Error initializing ChatOpenAI: {e}')
        return None

    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful assistant. Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer""",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)
    tool=[tools]
    agent = create_tool_calling_agent(llm, tool, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tool, verbose=True)
    response=agent_executor.invoke({"input": ques})
    print(response)
    st.write("Reply: ", response['output'])



def user_input(user_question):
    new_db = FAISS.load_local("faiss_db", embeddings,allow_dangerous_deserialization=True)
    
    retriever=new_db.as_retriever()
    retrieval_chain= create_retriever_tool(retriever,"pdf_extractor","This tool is to give answer to queries from the pdf")
    get_conversational_chain(retrieval_chain,user_question)



