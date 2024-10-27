import streamlit as st
import chat
from chat import get_conversational_chain
from PyPDF2 import PdfReader
import pandas as pd
import numpy as np 
import spacy
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings


import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

st.set_page_config("Australian BioTech")

def pdf_read(pdf_doc):
    text = ""
    for pdf in pdf_doc:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# # Load environment variables from .env file
# load_dotenv()

# # Sidebar inputs
# openai_api_key = st.sidebar.text_input("Enter OpenAI API Key", os.getenv("OPENAI_API_KEY", ""))
# temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2)

def main():
    def main_page():

        st.title("Welcome to the Australian BioTech App")
        st.write("This is the main page. Use the sidebar to navigate to other pages.")

    def second_page():

        # Create two columns
        col1, col2 = st.columns([1, 3])
        
        with col1:
            # Add an image to the left column
            st.image("images/AusBioTech_logo.png", width=150)
        
        with col2:
            # Add a header to the right column
            st.markdown("<h1 style='text-align: center;'>Australian Biotechnology Companies</h1>", unsafe_allow_html=True)

        user_question = st.text_input("Ask a Question from the PDF Files")

        if user_question:
            chat.user_input(user_question)

        with st.sidebar:
            st.title("Menu:")
            pdf_doc = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
            if st.button("Submit & Process"):
                with st.spinner("Processing..."):
                    raw_text = pdf_read(pdf_doc)
                    text_chunks = chat.get_chunks(raw_text)
                    chat.vector_store(text_chunks)
                    st.success("Done")

    # Page navigation
    page = st.sidebar.selectbox("Select a page", ["Main Page", "Second Page"])

    if page == "Main Page":
        main_page()
    else:
        second_page()

    # if __name__ == "__main__":
    #     if page == "Main Page":
    #         main_page()
    #     else:
    #         second_page()

if __name__ == "__main__":
    main()
