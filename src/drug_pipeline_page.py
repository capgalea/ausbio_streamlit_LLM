import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    # Load the drug pipeline data
    df = pd.read_csv('data/Drug_Pipelines.csv')
    return df

def drug_pipeline_page():
    st.title('Drugs in the Pipeline')
    
    # Load data
    try:
        df = load_data()
        
        # Sidebar for filtering
        st.sidebar.header('Filters')


        #st.dataframe(df)
        # Add checkbox to control main table visibility
        if not st.sidebar.checkbox('Show Raw Data Table'):
            # Display raw data table
            st.subheader('Drug Pipeline Data')
            st.dataframe(df)
        else:
            # Create visualizations
        
            # 1. Drug Development Phase Distribution
            if 'phase' in df.columns:
                st.subheader('Distribution by Development Phase')
                phase_fig = px.pie(df, names='phase', title='Drug Distribution by Phase')
                st.plotly_chart(phase_fig)
        
        # 2. Therapeutic Areas
        # if 'Therapeutic_Area' in df.columns:
        #     st.subheader('Distribution by Therapeutic Area')
        #     therapy_fig = px.bar(df['Therapeutic_Area'].value_counts(), 
        #                        title='Drug Count by Therapeutic Area')
        #     st.plotly_chart(therapy_fig)
        
        # 3. Timeline if dates are available
        # if 'Start_Date' in df.columns:
        #     st.subheader('Pipeline Timeline')
        #     timeline_fig = px.timeline(df, x_start='Start_Date', x_end='End_Date',
        #                              y='Drug_Name', title='Drug Development Timeline')
        #     st.plotly_chart(timeline_fig)
        
        # Add filters and interactive elements
            if st.sidebar.checkbox('Show Phase Filter'):
                phase_filter = st.sidebar.multiselect(
                    'Select Phases',
                    options=df['phase'].unique(),
                    default=df['phase'].unique()
                )
                df_filtered = df[df['phase'].isin(phase_filter)]
                st.subheader('Filtered Data')
                st.dataframe(df_filtered)

    except Exception as e:
        st.error(f"Error loading or processing data: {str(e)}")

# if __name__ == "__drug_pipeline_page__":
#     drug_pipeline_page()