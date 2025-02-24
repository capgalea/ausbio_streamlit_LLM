import requests
import pandas as pd
from dotenv import load_dotenv
import os
import streamlit as st

def get_patent(query):
    # Import IP Australia API client ID and client secret from toml file
    # CLIENT_ID = st.secrets["client_id"]
    # CLIENT_SECRET = st.secrets["client_secret"]

    # Access the environment variables on Render.com
    CLIENT_ID  = os.getenv("client_id")
    CLIENT_SECRET = os.getenv("client_secret")

    # URL for obtaining the access token
    token_url = "https://test.api.ipaustralia.gov.au/public/external-token-api/v1/access_token"

    # Data for the POST request to get the access token
    token_data = {
        "grant_type": "client_credentials",
    }

    # Headers for the token request
    token_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Make the POST request to get the access token
    token_response = requests.post(token_url, auth=(CLIENT_ID, CLIENT_SECRET), data=token_data, headers=token_headers)

    # Check if the response is successful
    if token_response.status_code == 200:
        response_data = token_response.json()
        access_token = response_data.get("access_token")
        token_type = response_data.get("token_type")
        print("Access Token:", access_token)
        print("Token Type:", token_type)



    # Retreive data from IP Australia database
    # API endpoint for the Australian patent search
    api_url = "https://test.api.ipaustralia.gov.au/public/australian-patent-search-api/v1/search/quick"

    # Request body for the API
    query_payload = {
        "query": query,
        "searchType": "DETAILS",
        "sort": {
        "field": "APPLICATION_NUMBER",
        "direction": "DESC"
        },
        "pageSize": 20,
        "pageNumber": 0,
        "searchMode": "QUICK_NO_ABSTRACT"
    }

    # Headers for the API request
    api_headers = {
        "Authorization": f"{token_type} {access_token}",  # Pass the token for authentication
        "Content-Type": "application/json"  # Specify JSON as the content type
    }

    # Make the POST request to the API with the payload
    try:
        api_response = requests.post(api_url, json=query_payload, headers=api_headers)

        # Print the response status code
        print(f"Status Code: {api_response.status_code}")

        # Print the response headers
        print("Headers:", api_response.headers)

        # Check if the API request is successful
        if api_response.status_code == 200:
            api_result = api_response.json()
            print("API Response:", api_result)
            # Normalize the nested JSON
            df_patent = pd.json_normalize(api_result["results"], sep="_")
            # Rename the columns
            df_patent = pd.DataFrame(api_result["results"])
            df_patent.rename(columns={
                'applicationNumber': 'Application Number',
                'pctNumber': 'PCT Number',
                'title': 'Title',
                'filingDate': 'Filing Date',
                'applicants': 'Applicants',
                'applicationStatus': 'Application Status'
                }, inplace=False)
        else:
            print("Error Response:", api_response.json())


    except Exception as e:
        print("An error occurred:", e)
        # Save the API response as a dataframe
        if api_response.status_code == 200:
            api_result = api_response.json()
            df_patent = pd.DataFrame(api_result)
            # Rename the columns
            df_patent.rename(columns={
                'applicationNumber': 'Application Number',
                'pctNumber': 'PCT Number',
                'title': 'Title',
                'filingDate': 'Filing Date',
                'applicants': 'Applicants',
                'applicationStatus': 'Application Status'
                }, inplace=False)
        else:
            print("Failed to make API request. Response:")
            print(api_response.status_code, api_response.text)
            
    return df_patent


