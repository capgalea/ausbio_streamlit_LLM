import streamlit as st
import pandas as pd
import chat
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
import requests
#from google import genai


# Read the PDF files
def pdf_read(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf.seek(0)  # Reset the file pointer to the beginning
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def process_urls_from_dataframe(df_url):
    if 'url' in df_url.columns:
        for url in df_url['url'].dropna():
            import_webpage_to_rag(url, verify_ssl=False)  # Optionally bypass SSL verification
    else:
        st.error("The dataframe does not contain a column named 'url'.")

def import_webpage_to_rag(url, verify_ssl=True):
    try:
        response = requests.get(url, verify=verify_ssl)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            text_chunks = chat.get_chunks(text)  # Define text_chunks
            st.session_state.all_text_chunks.extend(text_chunks)  # Accumulate text chunks
            chat.vector_store(st.session_state.all_text_chunks)  # Store accumulated text chunks
            st.success(f"Webpage {url} imported successfully!")
        elif response.status_code == 403:
            st.error(f"Access to the webpage {url} is forbidden (HTTP 403).")
        else:
            st.error(f"Failed to retrieve webpage {url}. Status code: {response.status_code}")
    except requests.exceptions.SSLError as e:
        st.error(f"SSL error occurred while retrieving webpage {url}: {e}")
    except Exception as e:
        st.error(f"An error occurred while retrieving webpage {url}: {e}")

# Initialize a global list to store text chunks from all URLs
if 'all_text_chunks' not in st.session_state:
    st.session_state.all_text_chunks = []


# LLM Chatbot
def LLM_chatbot():
    with st.sidebar:
            st.title("Menu:")

            # Upload PDF files
            pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", type="pdf", accept_multiple_files=True)
            if st.button("Submit & Process"):
                if pdf_docs:
                    with st.spinner("Processing..."):
                        raw_text = ""
                        for pdf in pdf_docs:
                            pdf.seek(0)  # Reset the file pointer to the beginning
                            raw_text += pdf_read([pdf])
                        text_chunks = chat.get_chunks(raw_text)
                        chat.vector_store(text_chunks)
                        st.success("Done")
                else:
                    st.error("Please upload at least one PDF file.")

            # Upload data from list of URLs in CSV file
            url_file = st.file_uploader("Upload a CSV file containing URLs", type="csv")
            if st.button("Import URLs from CSV to RAG"):
                df_url_file = pd.read_csv(url_file)
                # Example usage
                process_urls_from_dataframe(df_url_file)
                st.success("All URLs imported successfully!")
                # if url_file:
                #     with st.spinner("Processing..."):
                #         url_df = pd.read_csv(url_file)
                #         if 'url' in url_df.columns:
                #             for url in url_df['url']:
                #                 import_webpage_to_rag(url)
                #             st.success("All URLs imported successfully!")
                #         else:
                #             st.error("The CSV file must contain a column named 'url'.")
                # else:
                #     st.error("Please upload a CSV file containing URLs.")

    # Create two columns
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Add an image to the left column
        st.image("images/LLM.jpg", width=150)
    
    with col2:
        # Add a header to the right column
        st.markdown("<h1 style='text-align: center;'>Australian Biotechnology Companies</h1>", unsafe_allow_html=True)

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        chat.user_input(user_question)