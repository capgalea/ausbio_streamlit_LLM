import streamlit as st
import pandas as pd
import api_getPatent

# Define the function to display the patents page
def patents_page():
        # Title of patent table
        st.title("Patents Data")

        # Create input box to enter query for patents
        query = st.text_input("Enter Title, Applicants, Application Number, PTC Number, Filing Date, Application Status", "")
        df_patents = api_getPatent.get_patent(query)

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