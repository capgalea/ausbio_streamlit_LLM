import api_clinicalTrials_gov
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
            st.image("images/AusBioTech_logo.png", width=10)   

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

        # Create input box to enter query for patents
        query = st.text_input("Enter Title, Applicants, Application Number, PTC Number, Filing Date, Application Status", "")
        df_patents = getPatent.get_patent(query)

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




    # Clinical Trials Page
    def clinicalTrials_page():
        # Title of patent table
        st.title("Clinical Trials Data")

        # Initialize the page token
        if 'page_token' not in st.session_state:
            st.session_state.page_token = None

        # Create input box to enter condition
        condition = st.text_input("Enter the condition for clinical trials", "")

        # Get the clinical trials data
        df_clinicalTrials = api_clinicalTrials_gov.get_clinical_trials_data(condition, st.session_state.page_token)

        # Rename the columns
        df_clinicalTrials.rename(columns={
                'protocolSection.identificationModule.nctId': 'NCT ID',
                'protocolSection.identificationModule.orgStudyIdInfo.id': 'Unique Protocol Identification Number',
                'protocolSection.identificationModule.organization.fullName': 'Organization Full Name',
                'protocolSection.identificationModule.organization.class': 'Organization Class',
                'protocolSection.identificationModule.briefTitle': 'Brief Title',
                'protocolSection.identificationModule.officialTitle': 'Official Title',
                'protocolSection.identificationModule.acronym': 'Acronym',
                'protocolSection.statusModule.statusVerifiedDate': 'Record Verification Date',
                'protocolSection.statusModule.overallStatus': 'Overall Recruitment Status',
                'protocolSection.statusModule.expandedAccessInfo.hasExpandedAccess': 'Availability of Expanded Access',
                'protocolSection.statusModule.startDateStruct.date': 'Study Start Date',
                'protocolSection.statusModule.startDateStruct.type': 'Start Date Type',
                'protocolSection.statusModule.primaryCompletionDateStruct.date': 'Primary Completion Date',
                'protocolSection.statusModule.primaryCompletionDateStruct.type': 'Primary Completion Date Type',
                'protocolSection.statusModule.completionDateStruct.date': 'Study Completion Date',
                'protocolSection.statusModule.completionDateStruct.type': 'Study Completion Date Type',
                'protocolSection.statusModule.studyFirstSubmitDate': 'Study First Submitted Date',
                'protocolSection.statusModule.studyFirstSubmitQcDate': 'Study First QC Date',
                'protocolSection.statusModule.studyFirstPostDateStruct.date': 'Study First Posted Date',
                'protocolSection.statusModule.studyFirstPostDateStruct.type': 'Study First Posted Date Type',
                'protocolSection.statusModule.lastUpdateSubmitDate': 'Last Update Submitted Date',
                'protocolSection.statusModule.lastUpdatePostDateStruct.date': 'Last Update Posted Date',
                'protocolSection.statusModule.lastUpdatePostDateStruct.type': 'Last Update Posted Date Type',
                'protocolSection.sponsorCollaboratorsModule.responsibleParty.type': 'Responsible Party Type',
                'protocolSection.sponsorCollaboratorsModule.leadSponsor.name': 'Lead Sponsor Name',
                'protocolSection.sponsorCollaboratorsModule.leadSponsor.class': 'Lead Sponsor Class',
                'protocolSection.oversightModule.oversightHasDmc': 'Data Monitoring Committee',
                'protocolSection.oversightModule.isFdaRegulatedDrug': 'FDA Regulated Drug Product',
                'protocolSection.oversightModule.isFdaRegulatedDevice': 'FDA Regulated Device Product',
                'protocolSection.descriptionModule.briefSummary': 'Brief Summary',
                'protocolSection.conditionsModule.conditions': 'Conditions',
                'protocolSection.conditionsModule.keywords': 'Keywords',
                'protocolSection.designModule.studyType': 'Study Type',
                'protocolSection.designModule.phases': 'Study Phase',
                'protocolSection.designModule.designInfo.allocation': 'Design Allocation',
                'protocolSection.designModule.designInfo.interventionModel': 'Intervention Model',
                'protocolSection.designModule.designInfo.primaryPurpose': 'Primary Purpose',
                'protocolSection.designModule.designInfo.maskingInfo.masking': 'Masking',
                'protocolSection.designModule.enrollmentInfo.count': 'Enrollment Count',
                'protocolSection.designModule.enrollmentInfo.type': 'Enrollment Type',
                'protocolSection.armsInterventionsModule.armGroups': 'Arm Groups',
                'protocolSection.armsInterventionsModule.interventions': 'Interventions',
                'protocolSection.outcomesModule.primaryOutcomes': 'Primary Outcomes',
                'protocolSection.outcomesModule.secondaryOutcomes': 'Secondary Outcomes',
                'protocolSection.eligibilityModule.eligibilityCriteria': 'Eligibility Criteria',
                'protocolSection.eligibilityModule.healthyVolunteers': 'Healthy Volunteers',
                'protocolSection.eligibilityModule.sex': 'Sex',
                'protocolSection.eligibilityModule.minimumAge': 'Minimum Age',
                'protocolSection.eligibilityModule.maximumAge': 'Maximum Age',
                'protocolSection.eligibilityModule.stdAges': 'Standard Ages',
                'protocolSection.contactsLocationsModule.centralContacts': 'Central Contacts',
                'protocolSection.contactsLocationsModule.overallOfficials': 'Overall Officials',
                'protocolSection.contactsLocationsModule.locations': 'Locations',
                'protocolSection.ipdSharingStatementModule.ipdSharing': 'IPD Sharing Plan',
                'derivedSection.miscInfoModule.versionHolder': 'Version Holder',
                'derivedSection.conditionBrowseModule.meshes': 'Condition Mesh Terms',
                'derivedSection.conditionBrowseModule.ancestors': 'Condition Ancestors',
                'derivedSection.conditionBrowseModule.browseLeaves': 'Condition Browse Leaves',
                'derivedSection.conditionBrowseModule.browseBranches': 'Condition Browse Branches',
                'derivedSection.interventionBrowseModule.meshes': 'Intervention Mesh Terms',
                'derivedSection.interventionBrowseModule.ancestors': 'Intervention Ancestors',
                'derivedSection.interventionBrowseModule.browseLeaves': 'Intervention Browse Leaves',
                'derivedSection.interventionBrowseModule.browseBranches': 'Intervention Browse Branches',
                'protocolSection.identificationModule.secondaryIdInfos': 'Secondary ID Information',
                'protocolSection.sponsorCollaboratorsModule.responsibleParty.investigatorFullName': 'Investigator Full Name',
                'protocolSection.sponsorCollaboratorsModule.responsibleParty.investigatorTitle': 'Investigator Title',
                'protocolSection.sponsorCollaboratorsModule.responsibleParty.investigatorAffiliation': 'Investigator Affiliation',
                'protocolSection.sponsorCollaboratorsModule.collaborators': 'Collaborators',
                'protocolSection.oversightModule.isUsExport': 'US Export Product',
                'protocolSection.descriptionModule.detailedDescription': 'Detailed Description',
                'protocolSection.designModule.designInfo.maskingInfo.whoMasked': 'Who Masked',
                'protocolSection.ipdSharingStatementModule.description': 'IPD Sharing Description',
                'protocolSection.ipdSharingStatementModule.infoTypes': 'IPD Info Types',
                'protocolSection.ipdSharingStatementModule.timeFrame': 'IPD Sharing Time Frame',
                'protocolSection.ipdSharingStatementModule.accessCriteria': 'IPD Access Criteria',
                'documentSection.largeDocumentModule.largeDocs': 'Large Documents',
                'protocolSection.statusModule.whyStopped': 'Why Stopped',
                'protocolSection.designModule.designInfo.timePerspective': 'Time Perspective',
                'protocolSection.designModule.bioSpec.retention': 'Biospecimen Retention',
                'protocolSection.designModule.bioSpec.description': 'Biospecimen Description',
                'protocolSection.eligibilityModule.studyPopulation': 'Study Population',
                'protocolSection.eligibilityModule.samplingMethod': 'Sampling Method',
                'protocolSection.designModule.designInfo.maskingInfo.maskingDescription': 'Masking Description',
                'protocolSection.referencesModule.seeAlsoLinks': 'See Also Links',
                'protocolSection.ipdSharingStatementModule.url': 'IPD Sharing URL',
                'derivedSection.miscInfoModule.removedCountries': 'Removed Countries',
                'protocolSection.outcomesModule.otherOutcomes': 'Other Outcomes',
                'protocolSection.referencesModule.references': 'References',
                'protocolSection.statusModule.resultsFirstSubmitDate': 'Results First Submitted Date',
                'protocolSection.statusModule.resultsFirstSubmitQcDate': 'Results First Submitted QC Date',
                'protocolSection.statusModule.resultsFirstPostDateStruct.date': 'Results First Posted Date',
                'protocolSection.statusModule.resultsFirstPostDateStruct.type': 'Results First Posted Date Type',
                'protocolSection.designModule.designInfo.interventionModelDescription': 'Intervention Model Description',
                'resultsSection.participantFlowModule.recruitmentDetails': 'Recruitment Details',
                'resultsSection.participantFlowModule.groups': 'Participant Flow Groups',
                'resultsSection.participantFlowModule.periods': 'Participant Flow Periods',
                'resultsSection.baselineCharacteristicsModule.populationDescription': 'Baseline Population Description',
                'resultsSection.baselineCharacteristicsModule.groups': 'Baseline Groups',
                'resultsSection.baselineCharacteristicsModule.denoms': 'Baseline Denominators',
                'resultsSection.baselineCharacteristicsModule.measures': 'Baseline Measures',
                'resultsSection.outcomeMeasuresModule.outcomeMeasures': 'Outcome Measures',
                'resultsSection.adverseEventsModule.frequencyThreshold': 'Adverse Events Frequency Threshold',
                'resultsSection.adverseEventsModule.timeFrame': 'Adverse Events Time Frame',
                'resultsSection.adverseEventsModule.description': 'Adverse Events Description',
                'resultsSection.adverseEventsModule.eventGroups': 'Adverse Events Groups',
                'resultsSection.adverseEventsModule.otherEvents': 'Other Adverse Events',
                'resultsSection.moreInfoModule.limitationsAndCaveats.description': 'Limitations and Caveats Description',
                'resultsSection.moreInfoModule.certainAgreement.piSponsorEmployee': 'PI Sponsor Employee',
                'resultsSection.moreInfoModule.pointOfContact.title': 'Point of Contact Title',
                'resultsSection.moreInfoModule.pointOfContact.organization': 'Point of Contact Organization',
                'resultsSection.moreInfoModule.pointOfContact.email': 'Point of Contact Email',
                'resultsSection.moreInfoModule.pointOfContact.phone': 'Point of Contact Phone',
                'derivedSection.miscInfoModule.submissionTracking.firstMcpInfo.postDateStruct.date': 'Submission First MCP Date',
                'derivedSection.miscInfoModule.submissionTracking.firstMcpInfo.postDateStruct.type': 'Submission First MCP Date Type',
                'protocolSection.designModule.patientRegistry': 'Patient Registry',
                'protocolSection.designModule.targetDuration': 'Target Duration',
                'protocolSection.designModule.designInfo.observationalModel': 'Observational Model',
                'annotationSection.annotationModule.unpostedAnnotation.unpostedResponsibleParty': 'Unposted Responsible Party',
                'annotationSection.annotationModule.unpostedAnnotation.unpostedEvents': 'Unposted Events',
                'derivedSection.miscInfoModule.submissionTracking.estimatedResultsFirstSubmitDate': 'Estimated Results First Submit Date',
                'derivedSection.miscInfoModule.submissionTracking.submissionInfos': 'Submission Infos',
                'resultsSection.participantFlowModule.preAssignmentDetails': 'Pre-assignment Details',
                'resultsSection.adverseEventsModule.seriousEvents': 'Serious Adverse Events',
                'resultsSection.moreInfoModule.certainAgreement.restrictiveAgreement': 'Restrictive Agreement'
                }, inplace=True)
            
        # Display the clinical trials data in table
        st.dataframe(df_clinicalTrials, height=500)



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
    page = st.sidebar.selectbox("Select a page", ["Home Page", "Patents Page", "Clinical Trials Page", "LLM Chatbot"])

    if page == "Home Page":
        home_page()
    elif page == "Patents Page":
        patents_page()
    elif page == "Clinical Trials Page":
        clinicalTrials_page()
    else:
        LLM_chatbot()

if __name__ == "__main__":
    main()
