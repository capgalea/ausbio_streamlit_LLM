import requests
import pandas as pd
from pandas import json_normalize

# Example URL, replace with the actual API endpoint
url = "https://clinicaltrials.gov/api/v2/studies?format=json&markupFormat=markdown&query.cond=lung+cancer&query.term=AREA%5BLastUpdatePostDate%5DRANGE%5B2024-01-15%2CMAX%5D"
response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    
    # Check if 'studies' key exists in the data
    if 'studies' in data:
        # Flatten the nested JSON and convert to DataFrame
        df = json_normalize(data['studies'])
        # Remove columns with all missing values
        df = df.dropna(axis=1, how='all')
        print(df.head())  # Debug print to check the DataFrame
    else:
        print("Key 'studies' not found in the data")

else:
    print(f"Failed to retrieve data: {response.status_code}")

