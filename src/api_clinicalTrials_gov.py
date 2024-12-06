import requests
import pandas as pd
from pandas import json_normalize
import streamlit as st

def get_clinical_trials_data(condit, page_token=None):
    # URL for the ClinicalTrials.gov API
    url = "https://clinicaltrials.gov/api/v2/studies"

    # Parameters for the API request
    params = {"query.cond": condit, "countTotal": "true", "pageSize": 100, "pageToken": page_token} 

    # Headers for the API request
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        # Check if 'studies' key exists in the data
        if 'studies' in data:
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Previous Page"):
                    st.session_state.page_token = data['nextPageToken'] 
            with col2:
                if st.button("Next Page"):
                    st.session_state.page_token = data['nextPageToken']

            # Flatten the nested JSON and convert to DataFrame
            df_clinicalTrials = json_normalize(data['studies'])
            
            # Remove columns with all missing values
            df_clinicalTrials = df_clinicalTrials.dropna(axis=1, how='all')

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
            
        else:
            print("Key 'studies' not found in the data")
            return None
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None
    
    return df_clinicalTrials


# def get_clinical_trials_data(condit):
#     url = "https://clinicaltrials.gov/api/v2/studies"
#     params = {
#         "query.cond": condit,
#         "countTotal": "true",
#         "pageSize": 1000  # Adjust this value as needed
#     }
#     headers = {"accept": "application/json"}
#     all_studies = []
    
#     while True:
#         response = requests.get(url, params=params, headers=headers)
        
#         if response.status_code == 200:
#             data = response.json()
            
#             if 'studies' in data:
#                 all_studies.extend(data['studies'])
                
#                 if 'nextPageToken' in data:
#                     params['pageToken'] = data['nextPageToken']
#                 else:
#                     break
#             else:
#                 print("Key 'studies' not found in the data")
#                 return None
#         else:
#             print(f"Failed to retrieve data: {response.status_code}")
#             return None
    
#     if all_studies:
#         df_clinicalTrials = json_normalize(all_studies)
#         df_clinicalTrials = df_clinicalTrials.dropna(axis=1, how='all')
#         return df_clinicalTrials
#     else:
#         return None
    







