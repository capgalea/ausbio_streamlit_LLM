import getPatent  # Ensure this module is available and contains the get_patent function
import streamlit as st
import chat
import os
from chat import get_conversational_chain
from PyPDF2 import PdfReader
import pandas as pd
import numpy as np 
import spacy
import plotly.express as px
from streamlit_plotly_events import plotly_events
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# Set the page configuration
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

st.set_page_config("Australian BioTech", layout='wide', initial_sidebar_state='auto')

# Function to load the data
@ st.cache_data
def load_csv(file1):
    df = pd.read_csv(file1)
    return df

# Load the data
data = load_csv("data/bioTech_data.csv")

# def load_patents(file2):
#     df2 = pd.read_csv(file2)
#     return df2

# # Load the data
# patents = load_patents("data/patents.csv")

# Function to convert URLs to Markdown hyperlinks
def make_clickable(url_companies):
    return f'<a href="{url_companies}" target="_blank">{url_companies}</a>'

# Read the PDF files
def pdf_read(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf.seek(0)  # Reset the file pointer to the beginning
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


# Initialize a global list to store text chunks from all URLs
if 'all_text_chunks' not in st.session_state:
    st.session_state.all_text_chunks = []

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

def process_urls_from_dataframe(df_url):
    if 'url' in df_url.columns:
        for url in df_url['url'].dropna():
            import_webpage_to_rag(url, verify_ssl=False)  # Optionally bypass SSL verification
    else:
        st.error("The dataframe does not contain a column named 'url'.")


def main():
    def home_page():

        #Create two columns
        col1, col2 = st.columns([0.5, 10])

        with col1:
            # Add an image to the left column
            st.image("images/AusBioTech_logo.png", width=150)   

        with col2:
            # Add a header to the right column
            st.markdown("<h1 style='text-align: center;'>Australian Biotechnology Companies</h1>", unsafe_allow_html=True)

        # Add vertical space between header and plots
        st.write("")
        st.write("")

        # Display the data
        # Create two columns
        col1, col2 = st.columns([2, 2])

        with col1:
            # Create bar plotly bar chart showing the number of companies by city
            st.write("Number of Companies by State")
            city_counts = data["City"].value_counts()
            st.bar_chart(city_counts)

        # Create a sidebar to choose the company or city
        choice = st.sidebar.radio("Menu", ["Company", "City", "Category"])

        # Create a sidebar to choose the company or city
        if choice == "City":
            # Create table showing the selected city
            city_list = data["City"].unique().tolist()
            selected_city = st.sidebar.selectbox("Select a City", city_list, index=None) 
            
            # Create checkbox to show all data
            if st.sidebar.checkbox("Show All Data"):
                # Display the data in an expander
                with st.expander("View Data"):
                    st.dataframe(data[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                 column_config={"url": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = data
            else:
                # Display the data in an expander
                with st.expander("View Data"):
                    city_df = data[data["City"] == selected_city]
                    st.dataframe(city_df[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                 column_config={"url": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = city_df
            
        # Create a sidebar to choose the company or city
        elif choice == "Company":   
            company_list = data["Companies"].unique().tolist()
            selected_company = st.sidebar.selectbox("Select a Company", company_list, index=None) 

            # Create checkbox to show all data
            if st.sidebar.checkbox("Show All Data"):
                # Display the data in an expander
                with st.expander("View Data"):
                    st.dataframe(data[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                 column_config={"url": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = data
            else:
                # Display the data in an expander
                with st.expander("View Data"):
                    company_df = data[data["Companies"] == selected_company]
                    st.dataframe(company_df[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                 column_config={"url": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = company_df
        # Create a sidebar to choose the company or city
        elif choice == "Category":   
            category_list = data["Category"].unique().tolist()
            selected_category = st.sidebar.selectbox("Select a Category", category_list, index=None) 

            # Create checkbox to show all data
            if st.sidebar.checkbox("Show All Data"):
                # Display the data in an expander
                with st.expander("View Data"):
                    st.dataframe(data[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                 column_config={"url": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = data
            else:
                # Display the data in an expander
                with st.expander("View Data"):
                    category_df = data[data["Category"] == selected_category]
                    st.dataframe(category_df[["Category", "Companies", "Description", "City", "Location", "url", "Contact"]],
                                 column_config={"url": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = category_df
            

        with col2:
            # Create plotly map showing the location of each company using the latitude and lognitude columns
            # Ensure the data contains latitude and longitude columns
            if 'Latitude' not in data.columns or 'Longitude' not in data.columns:
                st.error("The data does not contain latitude and longitude information.")
            
            # Create a sidebar to choose the company or city
            elif choice == "Company":
                    # Create a Plotly map
                    fig = px.scatter_mapbox(
                    df,
                    lat="Latitude",
                    lon="Longitude",
                    hover_name="Companies",
                    hover_data={"Latitude": False, "Longitude": False, "Location": True, 
                                "url": True, "Contact": True, "Category": True},
                    zoom=2,
                    height=300,
                    center={"lat": -25.2744, "lon": 133.7751}  # Center on Australia
                    )

                    fig.update_layout(mapbox_style="open-street-map")
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


                    # Display the map in the Streamlit app
                    st.plotly_chart(fig, key="map")
            
            # Create a sidebar to choose the company or city
            elif choice == "City":
                    # Create a Plotly map
                    fig = px.scatter_mapbox(
                    df,
                    lat="Latitude",
                    lon="Longitude",
                    hover_name="Companies",
                    hover_data={"Latitude": False, "Longitude": False, "Location": True, 
                                "url": True, "Contact": True, "Category": True},
                    zoom=2,
                    height=300,
                    center={"lat": -25.2744, "lon": 133.7751}  # Center on Australia
                    )
        
                    fig.update_layout(mapbox_style="open-street-map")
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        
        
                    # Display the map in the Streamlit app
                    st.plotly_chart(fig, key="map")

            # Create a sidebar to choose the company or city
            elif choice == "Category":
                    # Create a Plotly map
                    fig = px.scatter_mapbox(
                    df,
                    lat="Latitude",
                    lon="Longitude",
                    hover_name="Companies",
                    hover_data={"Latitude": False, "Longitude": False, "Location": True, 
                                "url": True, "Contact": True, "Category": True},
                    zoom=2,
                    height=300,
                    center={"lat": -25.2744, "lon": 133.7751}  # Center on Australia
                    )

                    fig.update_layout(mapbox_style="open-street-map")
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


                    # Display the map in the Streamlit app
                    st.plotly_chart(fig, key="map")

        
    def patents_page():
        # Title of patent table
        st.title("Patents Data")

        # Create input box to wnter query for patents
        query = st.text_input("Enter Title, Applicants, Application Number, PTC Number, Filing Date, Application Status", "")
        df_patents = getPatent.get_patent(query)

        # Display the filtered patents table
        #st.dataframe(df_patents, use_container_width=True)

        # Flatten the applicants column
        all_applicants = [applicant for sublist in df_patents["applicants"] for applicant in sublist]

        # Create text search box in sidebar to search multiple columns in patents table. Also dropdown to filter by status, type, and applicant.
        search = st.sidebar.text_input("Search Title, Applicants, Application Number, PTC Number, Filing Date, Application Status", key="search")
        status = st.sidebar.multiselect("Filter by Status", df_patents["applicationStatus"].unique(), key="application_status")
        applicant = st.sidebar.multiselect("Filter by Applicant", list(set(all_applicants)), key="patent_applicants")

        
        # Filter table by search, status, type, and applicant
        filtered_patents = df_patents
        if search:
            search_terms = search.split()
            for term in search_terms:
                filtered_patents = df_patents[
                df_patents.apply(lambda row: row.astype(str).str.contains(term, case=False).any(), axis=1)
            ]
        if status:
            filtered_patents = df_patents[df_patents["applicationStatus"].isin(status)]
        if applicant:
            filtered_patents = df_patents[df_patents["applicants"].isin(applicant)]

        # Display the filtered patents table
        st.dataframe(filtered_patents, use_container_width=True)


        # # Create a TITLE text search box in sidebar for patents table
        # search_title = st.sidebar.text_input("Search Title or Inventor", "")

        # # Create a INVENTOR text search box in sidebar for patents table
        # #search_inventor = st.sidebar.text_input("Search Inventor", "")

        # # Create sidebar to filter status of patents
        # status = st.sidebar.multiselect("Filter by Status", patents["STATUS"].unique(), key="patent_status")

        # # filter table by search and status
        # filtered_patents = patents
        # if search_title:
        #     filtered_patents = filtered_patents[
        #         filtered_patents["TITLE"].str.contains(search_title, case=False)] | filtered_patents[filtered_patents["INVENTORS"].str.contains(search_title, case=False)
        #                      ]
        # # elif search_inventor:
        # #     filtered_patents = filtered_patents[filtered_patents["INVENTORS"].str.contains(search_inventor, case=False)]
        # elif status:
        #     filtered_patents = filtered_patents[filtered_patents["STATUS"].isin(status)]
        # else:
        #     filtered_patents = patents
        # st.dataframe(filtered_patents)


    



        




        
        
            
       
        
 

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
            st.image("images/AusBioTech_logo.png", width=150)
        
        with col2:
            # Add a header to the right column
            st.markdown("<h1 style='text-align: center;'>Australian Biotechnology Companies</h1>", unsafe_allow_html=True)

        user_question = st.text_input("Ask a Question from the PDF Files")

        if user_question:
            chat.user_input(user_question)
            
        # with st.sidebar:
        #     st.title("Menu:")
        #     pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", type="pdf", accept_multiple_files=True)
        #     if st.button("Submit & Process"):
        #         if pdf_docs:
        #             with st.spinner("Processing..."):
        #                 raw_text = ""
        #                 for pdf in pdf_docs:
        #                     pdf.seek(0)  # Reset the file pointer to the beginning
        #                     raw_text += pdf_read([pdf])
        #                 text_chunks = chat.get_chunks(raw_text)
        #                 chat.vector_store(text_chunks)
        #                 st.success("Done")
        #         else:
        #             st.error("Please upload at least one PDF file.")

    # Page navigation
    page = st.sidebar.selectbox("Select a page", ["Home Page", "Patents Page", "LLM Chatbot"])

    if page == "Home Page":
        home_page()
    elif page == "Patents Page":
        patents_page()
    else:
        LLM_chatbot()

if __name__ == "__main__":
    main()
