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

# Set the page configuration
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

st.set_page_config("Australian BioTech")

# Function to load the data
@ st.cache_data
def load_csv(file):
    df = pd.read_csv(file)
    return df

# Function to convert URLs to Markdown hyperlinks
def make_clickable(url):
    return f'<a href="{url}" target="_blank">{url}</a>'

# Load the data
data = load_csv("data/bioTech_data.csv")

# Read the PDF files
def pdf_read(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf.seek(0)  # Reset the file pointer to the beginning
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text




def main():
    def home_page():
        #Create two columns
        col1, col2 = st.columns([0.5, 10])

        with col1:
            # Add an image to the left column
            st.image("images/AusBioTech_logo.png", width=100)   

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


        if choice == "City":
            # Create table showing the selected city
            city_list = data["City"].unique().tolist()
            selected_city = st.sidebar.selectbox("Select a City", city_list, index=None) 
            
            # Create checkbox to show all data
            if st.sidebar.checkbox("Show All Data"):
                # Display the data in an expander
                with st.expander("View Data"):
                    st.dataframe(data[["Category", "Companies", "Description", "City", "Location", "Website", "Contact"]],
                                 column_config={"Website": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = data
            else:
                # Display the data in an expander
                with st.expander("View Data"):
                    city_df = data[data["City"] == selected_city]
                    st.dataframe(city_df[["Category", "Companies", "Description", "City", "Location", "Website", "Contact"]],
                                 column_config={"Website": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = city_df
            

        elif choice == "Company":   
            company_list = data["Companies"].unique().tolist()
            selected_company = st.sidebar.selectbox("Select a Company", company_list, index=None) 

            # Create checkbox to show all data
            if st.sidebar.checkbox("Show All Data"):
                # Display the data in an expander
                with st.expander("View Data"):
                    st.dataframe(data[["Category", "Companies", "Description", "City", "Location", "Website", "Contact"]],
                                 column_config={"Website": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = data
            else:
                # Display the data in an expander
                with st.expander("View Data"):
                    company_df = data[data["Companies"] == selected_company]
                    st.dataframe(company_df[["Category", "Companies", "Description", "City", "Location", "Website", "Contact"]],
                                 column_config={"Website": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = company_df

        elif choice == "Category":   
            category_list = data["Category"].unique().tolist()
            selected_category = st.sidebar.selectbox("Select a Category", category_list, index=None) 

            # Create checkbox to show all data
            if st.sidebar.checkbox("Show All Data"):
                # Display the data in an expander
                with st.expander("View Data"):
                    st.dataframe(data[["Category", "Companies", "Description", "City", "Location", "Website", "Contact"]],
                                 column_config={"Website": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = data
            else:
                # Display the data in an expander
                with st.expander("View Data"):
                    category_df = data[data["Category"] == selected_category]
                    st.dataframe(category_df[["Category", "Companies", "Description", "City", "Location", "Website", "Contact"]],
                                 column_config={"Website": st.column_config.LinkColumn("Company Website")}
                                 )
                    df = category_df
            

        with col2:
            # Create plotly map showing the location of each company using the latitude and lognitude columns
            # Ensure the data contains latitude and longitude columns
            if 'Latitude' not in data.columns or 'Longitude' not in data.columns:
                st.error("The data does not contain latitude and longitude information.")
            elif choice == "Company":
                    # Create a Plotly map
                    fig = px.scatter_mapbox(
                    df,
                    lat="Latitude",
                    lon="Longitude",
                    hover_name="Companies",
                    hover_data={"Latitude": False, "Longitude": False, "Location": True, 
                                "Website": True, "Contact": True, "Category": True},
                    zoom=2,
                    height=300,
                    center={"lat": -25.2744, "lon": 133.7751}  # Center on Australia
                    )

                    fig.update_layout(mapbox_style="open-street-map")
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


                    # Display the map in the Streamlit app
                    st.plotly_chart(fig, key="map")
            
            elif choice == "City":
                    # Create a Plotly map
                    fig = px.scatter_mapbox(
                    df,
                    lat="Latitude",
                    lon="Longitude",
                    hover_name="Companies",
                    hover_data={"Latitude": False, "Longitude": False, "Location": True, 
                                "Website": True, "Contact": True, "Category": True},
                    zoom=2,
                    height=300,
                    center={"lat": -25.2744, "lon": 133.7751}  # Center on Australia
                    )
        
                    fig.update_layout(mapbox_style="open-street-map")
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        
        
                    # Display the map in the Streamlit app
                    st.plotly_chart(fig, key="map")

            elif choice == "Category":
                    # Create a Plotly map
                    fig = px.scatter_mapbox(
                    df,
                    lat="Latitude",
                    lon="Longitude",
                    hover_name="Companies",
                    hover_data={"Latitude": False, "Longitude": False, "Location": True, 
                                "Website": True, "Contact": True, "Category": True},
                    zoom=2,
                    height=300,
                    center={"lat": -25.2744, "lon": 133.7751}  # Center on Australia
                    )

                    fig.update_layout(mapbox_style="open-street-map")
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


                    # Display the map in the Streamlit app
                    st.plotly_chart(fig, key="map")

        

        
 


    def LLM_chatbot():
        with st.sidebar:
                st.title("Menu:")
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
    page = st.sidebar.selectbox("Select a page", ["Home Page", "LLM Chatbot"])

    if page == "Home Page":
        home_page()
    else:
        LLM_chatbot()

if __name__ == "__main__":
    main()
