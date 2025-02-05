import pandas as pd

data = [
{
"company": "Actinogen Medical Limited",
"pipeline": [
{
"drug": "Xanamem",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "Cognitive enhancer for Alzheimer's disease and other neurological conditions"
}
]
},
{
"company": "AdAlta Limited",
"pipeline": [
{
"drug": "AD-214",
"phase": "Phase 1",
"type_of_drug": "antibody",
"description": "CAR T therapy for fibrotic diseases"
},
{
"drug": "AD-324",
"phase": "Preclinical",
"type_of_drug": "antibody",
"description": "i-body for fibrotic diseases"
}
]
},
{
"company": "Algorae Pharmaceuticals (formerly Living Cell Technologies)",
"pipeline": [
{
"drug": "NTCELL",
"phase": "Phase 1/2",
"type_of_drug": "cell therapy",
"description": "Alginate encapsulated neonatal porcine choroid plexus for Parkinson's disease"
}
]
},
{
"company": "Amplia Therapeutics Limited",
"pipeline": [
{
"drug": "AMP945",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Focal Adhesion Kinase (FAK) inhibitor for cancer and fibrosis"
},
{
"drug": "AMP886",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Focal Adhesion Kinase (FAK) inhibitor for cancer and fibrosis"
}
]
},
{
"company": "Anteris Technologies",
"pipeline": [
{
"drug": "ADAPT",
"phase": "Preclinical",
"type_of_drug": "medical device",
"description": "Novel tissue engineering technology for heart valve replacement"
}
]
},
{
"company": "Aravax",
"pipeline": [
{
"drug": "PVX108",
"phase": "Phase 1",
"type_of_drug": "peptide",
"description": "Peptide immunotherapy for peanut allergy"
}
]
},
{
"company": "Argenica Therapeutics Ltd",
"pipeline": [
{
"drug": "ARG-007",
"phase": "Phase 1",
"type_of_drug": "small molecule",
"description": "Neuroprotective agent for stroke"
}
]
},
{
"company": "Arovella Therapeutics Ltd",
"pipeline": [
{
"drug": "CAR19-iNKT",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "Invariant natural killer T (iNKT) cell therapy for cancer"
},
{
"drug": "DNT-001",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "Invariant natural killer T (iNKT) cell therapy for cancer"
}
]
},
{
"company": "Asteri Pharma",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Novel therapeutics for neurological disorders"
}
]
},
{
"company": "Aucentra Therapeutics",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Novel therapeutics for cancer"
}
]
},
{
"company": "Avecho Biotechnology",
"pipeline": [
{
"drug": "CBD Soft Gel Capsules",
"phase": "Phase 2",
"type_of_drug": "cannabinoid",
"description": "Cannabidiol (CBD) soft gel capsules for various indications"
},
{
"drug": "DHA Soft Gel Capsules",
"phase": "Phase 1",
"type_of_drug": "fatty acid",
"description": "Docosahexaenoic acid (DHA) soft gel capsules for various indications"
}
]
},
{
"company": "Avita Medical",
"pipeline": [
{
"drug": "RECELL",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Autologous cell harvesting device for skin regeneration"
}
]
},
{
"company": "BioDiem Ltd",
"pipeline": [
{
"drug": "BDM-I",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "Immunomodulatory agent for infectious diseases"
}
]
},
{
"company": "BiomeBank",
"pipeline": [
{
"drug": "Donated Faecal Microbiota",
"phase": "Approved",
"type_of_drug": "microbiome",
"description": "Faecal microbiota transplant for Clostridium difficile infection"
}
]
},
{
"company": "Biotron Limited",
"pipeline": [
{
"drug": "BIT225",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "Antiviral agent for HIV and Hepatitis C"
}
]
},
{
"company": "Cambium Bio Limited",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Novel therapeutics for cancer"
}
]
},
{
"company": "Cancure",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "Allogeneic T cell immunotherapy for cancer"
}
]
},
{
"company": "Carina Biotech",
"pipeline": [
{
"drug": "CAR T",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "CAR T therapy for cancer"
}
]
},
{
"company": "Cartherics",
"pipeline": [
{
"drug": "CAR T",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "iPSC derived CAR T therapy for cancer"
}
]
},
{
"company": "Celosia Therapeutics Pty Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "gene therapy",
"description": "Gene therapy for ALS/MND/LGD/AD/dementia/dravet syndrome"
}
]
},
{
"company": "Certa Therapeutics",
"pipeline": [
{
"drug": "FT011",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "Novel therapeutics for inflammatory diseases"
},
{
"drug": "FT009",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Novel therapeutics for inflammatory diseases"
}
]
},
{
"company": "Chimeric Therapeutics Ltd",
"pipeline": [
{
"drug": "CHM 1101",
"phase": "Phase 1",
"type_of_drug": "cell therapy",
"description": "CAR T and CAR NK therapy for cancer"
},
{
"drug": "CHM 2101",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "CAR T and CAR NK therapy for cancer"
}
]
},
{
"company": "Clarity Pharmaceuticals",
"pipeline": [
{
"drug": "SARTATE",
"phase": "Phase 3",
"type_of_drug": "radiopharmaceutical",
"description": "Copper-64 based radiopharmaceutical for cancer imaging and therapy"
},
{
"drug": "SAR-Bombesin",
"phase": "Phase 1",
"type_of_drug": "radiopharmaceutical",
"description": "Copper-64 based radiopharmaceutical for cancer imaging and therapy"
}
]
},
{
"company": "Cochlear Limited",
"pipeline": [
{
"drug": "Cochlear Implants",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Cochlear implants for hearing loss"
}
]
},
{
"company": "CSL Limited",
"pipeline": [
{
"drug": "Hizentra",
"phase": "Approved",
"type_of_drug": "biologic",
"description": "Immunoglobulin therapy for immunodeficiency"
},
{
"drug": "Privigen",
"phase": "Approved",
"type_of_drug": "biologic",
"description": "Immunoglobulin therapy for immunodeficiency"
},
{
"drug": "Idelvion",
"phase": "Approved",
"type_of_drug": "biologic",
"description": "Recombinant coagulation factor IX for hemophilia B"
},
{
"drug": "Kcentra",
"phase": "Approved",
"type_of_drug": "biologic",
"description": "Prothrombin complex concentrate for bleeding disorders"
},
{
"drug": "Haegarda",
"phase": "Approved",
"type_of_drug": "biologic",
"description": "C1 esterase inhibitor for hereditary angioedema"
},
{
"drug": "Respreeza",
"phase": "Approved",
"type_of_drug": "biologic",
"description": "Alpha-1 proteinase inhibitor for alpha-1 antitrypsin deficiency"
},
{
"drug": "Zemaira",
"phase": "Approved",
"type_of_drug": "biologic",
"description": "Alpha-1 proteinase inhibitor for alpha-1 antitrypsin deficiency"
},
{
"drug": "Berinert",
"phase": "Approved",
"type_of_drug": "biologic",
"description": "C1 esterase inhibitor for hereditary angioedema"
},
{
"drug": "Glatopa",
"phase": "Approved",
"type_of_drug": "biologic",
"description": "Glatiramer acetate for multiple sclerosis"
},
{
"drug": "Afluria",
"phase": "Approved",
"type_of_drug": "vaccine",
"description": "Influenza vaccine"
},
{
"drug": "Fluad",
"phase": "Approved",
"type_of_drug": "vaccine",
"description": "Influenza vaccine"
},
{
"drug": "Seqirus",
"phase": "Approved",
"type_of_drug": "vaccine",
"description": "Influenza vaccine"
}
]
},
{
"company": "Currus Biologics",
"pipeline": [
{
"drug": "CAR T",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "CAR T therapy for cancer"
}
]
},
{
"company": "Cynata Therapeutics",
"pipeline": [
{
"drug": "CYP-001",
"phase": "Phase 2",
"type_of_drug": "cell therapy",
"description": "iPSC derived MSC therapy for graft-versus-host disease"
},
{
"drug": "CYP-002",
"phase": "Phase 1",
"type_of_drug": "cell therapy",
"description": "iPSC derived MSC therapy for osteoarthritis"
}
]
},
{
"company": "Cyteph",
"pipeline": [
{
"drug": "VSTs",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "Allogeneic CMV+ virus specific T cells for cancer"
}
]
},
{
"company": "Dimerix Limited",
"pipeline": [
{
"drug": "DMX-200",
"phase": "Phase 3",
"type_of_drug": "small molecule",
"description": "Chemokine receptor blocker for kidney disease"
},
{
"drug": "DMX-700",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Chemokine receptor blocker for respiratory diseases"
}
]
},
{
"company": "Emyria Ltd",
"pipeline": [
{
"drug": "MDMA",
"phase": "Phase 2",
"type_of_drug": "psychedelic",
"description": "MDMA-assisted therapy for PTSD"
},
{
"drug": "CBD",
"phase": "Phase 2",
"type_of_drug": "cannabinoid",
"description": "Cannabidiol (CBD) for various indications"
}
]
},
{
"company": "ENA Respiratory",
"pipeline": [
{
"drug": "INNA-051",
"phase": "Phase 2",
"type_of_drug": "nasal spray",
"description": "Nasal spray for respiratory infections"
}
]
},
{
"company": "EnGeneIC",
"pipeline": [
{
"drug": "EDV",
"phase": "Phase 1",
"type_of_drug": "nanocell",
"description": "EnGeneIC Dream Vector (EDV) nanocell for cancer therapy"
}
]
},
{
"company": "EpiAxis TherapeuticsEpichem Pty Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Novel therapeutics for cancer"
}
]
},
{
"company": "Genetic Techonologies Ltd",
"pipeline": [
{
"drug": "GeneType",
"phase": "Approved",
"type_of_drug": "genetic test",
"description": "Genetic test for breast cancer risk"
}
]
},
{
"company": "GPN Vaccines",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "vaccine",
"description": "Novel vaccines for infectious diseases"
}
]
},
{
"company": "HaemaLogiX Pty Ltd",
"pipeline": [
{
"drug": "CAR T",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "CAR T therapy for hematological malignancies"
}
]
},
{
"company": "Immuron Limited",
"pipeline": [
{
"drug": "Travelan",
"phase": "Phase 2",
"type_of_drug": "antibody",
"description": "Antibody therapy for traveler's diarrhea"
},
{
"drug": "IMM-124E",
"phase": "Phase 1",
"type_of_drug": "antibody",
"description": "Antibody therapy for NASH"
}
]
},
{
"company": "Immutep Limited",
"pipeline": [
{
"drug": "eftilagimod alpha",
"phase": "Phase 2",
"type_of_drug": "immunotherapy",
"description": "Immunotherapy for cancer"
},
{
"drug": "IMP761",
"phase": "Preclinical",
"type_of_drug": "antibody",
"description": "LAG-3 antibody for cancer"
}
]
},
{
"company": "ImmVirX",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "oncolytic virus",
"description": "Oncolytic virus therapy for cancer"
}
]
},
{
"company": "Imugene Ltd",
"pipeline": [
{
"drug": "HER-Vaxx",
"phase": "Phase 2",
"type_of_drug": "immunotherapy",
"description": "CAR T and oncolytic virus therapy for cancer"
},
{
"drug": "CHECKvacc",
"phase": "Phase 1",
"type_of_drug": "oncolytic virus",
"description": "Oncolytic virus therapy for cancer"
},
{
"drug": "PD1-Vaxx",
"phase": "Phase 1",
"type_of_drug": "immunotherapy",
"description": "Immunotherapy for cancer"
}
]
},
{
"company": "InhaleRx Ltd",
"pipeline": [
{
"drug": "IRX-001",
"phase": "Phase 1",
"type_of_drug": "inhaler",
"description": "Inhaled drug for respiratory diseases"
}
]
},
{
"company": "INOVIQ Limited",
"pipeline": [
{
"drug": "SubB2M",
"phase": "Preclinical",
"type_of_drug": "diagnostic",
"description": "Diagnostic test for cancer"
},
{
"drug": "hTERT",
"phase": "Preclinical",
"type_of_drug": "diagnostic",
"description": "Diagnostic test for cancer"
}
]
},
{
"company": "Invion Limited",
"pipeline": [
{
"drug": "INV-101",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "Anti-inflammatory agent for respiratory diseases"
}
]
},
{
"company": "LBT Innovations",
"pipeline": [
{
"drug": "Automated Plate Assessment System (APAS)",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Automated plate assessment system for microbiology"
}
]
},
{
"company": "Mesoblast Limited",
"pipeline": [
{
"drug": "Remestemcel-L",
"phase": "Phase 3",
"type_of_drug": "cell therapy",
"description": "Autologous MSC therapy for graft-versus-host disease"
},
{
"drug": "MPC-150-IM",
"phase": "Phase 3",
"type_of_drug": "cell therapy",
"description": "Autologous MSC therapy for chronic heart failure"
},
{
"drug": "MPC-25-IC",
"phase": "Phase 3",
"type_of_drug": "cell therapy",
"description": "Autologous MSC therapy for chronic lower back pain"
},
{
"drug": "REVASCOR",
"phase": "Phase 3",
"type_of_drug": "cell therapy",
"description": "Autologous MSC therapy for acute myocardial infarction"
},
{
"drug": "MPC-25-Osteo",
"phase": "Phase 2",
"type_of_drug": "cell therapy",
"description": "Autologous MSC therapy for osteoarthritis"
},
{
"drug": "MPC-100-AD",
"phase": "Phase 2",
"type_of_drug": "cell therapy",
"description": "Autologous MSC therapy for Alzheimer's disease"
},
{
"drug": "MSB-GVHD",
"phase": "Phase 3",
"type_of_drug": "cell therapy",
"description": "Autologous MSC therapy for graft-versus-host disease"
}
]
},
{
"company": "Microba Pty Ltd",
"pipeline": [
{
"drug": "Microbiome Testing",
"phase": "Approved",
"type_of_drug": "diagnostic",
"description": "Microbiome testing for various indications"
}
]
},
{
"company": "MINIMUM bio Pty Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Novel therapeutics for cancer"
}
]
},
{
"company": "Noxopharm",
"pipeline": [
{
"drug": "Veyonda",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "Anti-cancer agent"
},
{
"drug": "NOX66",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Anti-cancer agent"
}
]
},
{
"company": "Nyrada Inc",
"pipeline": [
{
"drug": "NYR-BI01",
"phase": "Phase 1",
"type_of_drug": "small molecule",
"description": "Cholesterol-lowering agent"
},
{
"drug": "NYR-LI01",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Neuroprotective agent for traumatic brain injury"
}
]
},
{
"company": "Obatica Pty Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "immunotherapy",
"description": "Immunotherapy for cancer"
}
]
},
{
"company": "OncoRes Medical Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "medical device",
"description": "Medical device for cancer detection"
}
]
},
{
"company": "OncoSil Medical Ltd",
"pipeline": [
{
"drug": "OncoSil",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Radioactive implant for pancreatic cancer"
}
]
},
{
"company": "Opthea Limited",
"pipeline": [
{
"drug": "OPT-302",
"phase": "Phase 3",
"type_of_drug": "biologic",
"description": "VEGF-C/D inhibitor for wet AMD"
}
]
},
{
"company": "OptiScan Imaging Ltd",
"pipeline": [
{
"drug": "InVivo Confocal Microscope",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Confocal microscope for real-time imaging"
}
]
},
{
"company": "Orthocell",
"pipeline": [
{
"drug": "Ortho-ACI",
"phase": "Approved",
"type_of_drug": "cell therapy",
"description": "Autologous chondrocyte implantation for cartilage repair"
},
{
"drug": "CelGro",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Collagen scaffold for tissue repair"
},
{
"drug": "SmrtGraft",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "Autologous tendon stem cell therapy"
}
]
},
{
"company": "Osteopore",
"pipeline": [
{
"drug": "Osteopore",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Bioresorbable implant for bone regeneration"
}
]
},
{
"company": "Paradigm BioPharmaceuticals Ltd",
"pipeline": [
{
"drug": "Pentosan Polysulfate Sodium (PPS)",
"phase": "Phase 3",
"type_of_drug": "small molecule",
"description": "Drug for osteoarthritis"
}
]
},
{
"company": "Patrys Ltd",
"pipeline": [
{
"drug": "PAT-DX1",
"phase": "Phase 1",
"type_of_drug": "antibody",
"description": "Antibody therapy for cancer"
},
{
"drug": "PAT-DX3",
"phase": "Preclinical",
"type_of_drug": "antibody",
"description": "Antibody therapy for cancer"
}
]
},
{
"company": "PharmAust Limited",
"pipeline": [
{
"drug": "Monepantel",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "Drug for motor neuron disease"
}
]
},
{
"company": "PolyActiva Pty Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "polymer",
"description": "Biodegradable polymers for drug delivery"
}
]
},
{
"company": "Polynovo Ltd",
"pipeline": [
{
"drug": "Novosorb BTM",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Biodegradable temporizing matrix for dermal regeneration"
},
{
"drug": "Novosorb MTX",
"phase": "Preclinical",
"type_of_drug": "medical device",
"description": "Biodegradable temporizing matrix for dermal regeneration"
},
{
"drug": "Novosorb ADM",
"phase": "Preclinical",
"type_of_drug": "medical device",
"description": "Biodegradable temporizing matrix for dermal regeneration"
}
]
},
{
"company": "Prescient Therapeutics Limited",
"pipeline": [
{
"drug": "PTX-100",
"phase": "Phase 1",
"type_of_drug": "small molecule",
"description": "CAR T therapy for cancer"
},
{
"drug": "PTX-200",
"phase": "Phase 1",
"type_of_drug": "small molecule",
"description": "CAR T therapy for cancer"
}
]
},
{
"company": "Protagonist Pty Ltd",
"pipeline": [
{
"drug": "PN-943",
"phase": "Phase 2",
"type_of_drug": "peptide",
"description": "Peptide therapy for inflammatory bowel disease"
},
{
"drug": "PN-235",
"phase": "Phase 1",
"type_of_drug": "peptide",
"description": "Peptide therapy for inflammatory bowel disease"
}
]
},
{
"company": "Proteomics International Laboratories Limited",
"pipeline": [
{
"drug": "PromarkerD",
"phase": "Approved",
"type_of_drug": "diagnostic",
"description": "Diagnostic test for diabetic kidney disease"
}
]
},
{
"company": "PYC Therapeutics",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "mRNA",
"description": "mRNA therapy for genetic diseases"
}
]
},
{
"company": "QBiotics Group Limited",
"pipeline": [
{
"drug": "EBC-46",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "Anti-cancer agent"
}
]
},
{
"company": "Race Oncology Limited",
"pipeline": [
{
"drug": "Zantrene",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "Anti-cancer agent"
}
]
},
{
"company": "Recce Pharmaceuticals Ltd",
"pipeline": [
{
"drug": "RECCE 327",
"phase": "Phase 1",
"type_of_drug": "anti-infective",
"description": "Anti-infective agent for bacterial infections"
},
{
"drug": "RECCE 529",
"phase": "Preclinical",
"type_of_drug": "anti-infective",
"description": "Anti-infective agent for viral infections"
}
]
},
{
"company": "Regeneus",
"pipeline": [
{
"drug": "Progenza",
"phase": "Phase 1",
"type_of_drug": "cell therapy",
"description": "Autologous MSC therapy for osteoarthritis"
},
{
"drug": "Sygenus",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "Allogeneic MSC therapy for osteoarthritis"
}
]
},
{
"company": "ReNerve",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "medical device",
"description": "Nerve repair sheaths for nerve damage"
}
]
},
{
"company": "Resonance Health Pty Ltd",
"pipeline": [
{
"drug": "FerriScan",
"phase": "Approved",
"type_of_drug": "diagnostic",
"description": "MRI-based diagnostic for liver iron overload"
}
]
},
{
"company": "Respiri Limited",
"pipeline": [
{
"drug": "wheezo",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Wearable device for asthma monitoring"
}
]
},
{
"company": "Respirion Pharmaceuticals Pty Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Novel therapeutics for respiratory diseases"
}
]
},
{
"company": "Sementis Limited",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "vaccine",
"description": "Novel vaccines for infectious diseases"
}
]
},
{
"company": "Sienna Cancer Diagnostics",
"pipeline": [
{
"drug": "hTERT",
"phase": "Preclinical",
"type_of_drug": "diagnostic",
"description": "Diagnostic test for cancer"
}
]
},
{
"company": "Skin2Neuron",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "Hair follicle derived neurons for dementia"
}
]
},
{
"company": "Snoretox Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "medical device",
"description": "Medical device for sleep apnea"
}
]
},
{
"company": "SpeeDx Pty Ltd",
"pipeline": [
{
"drug": "PlexPCR",
"phase": "Approved",
"type_of_drug": "diagnostic",
"description": "Molecular diagnostic tests for infectious diseases"
}
]
},
{
"company": "Starpharma Holdings Limited",
"pipeline": [
{
"drug": "VivaGel",
"phase": "Phase 3",
"type_of_drug": "antiviral",
"description": "Antiviral agent for bacterial vaginosis"
},
{
"drug": "DEP",
"phase": "Preclinical",
"type_of_drug": "drug delivery",
"description": "Drug delivery platform for various indications"
}
]
},
{
"company": "Syntara",
"pipeline": [
{
"drug": "LOX-1 Inhibitor",
"phase": "Phase 2",
"type_of_drug": "small molecule",
"description": "LOX-1 inhibitor for fibrotic diseases"
}
]
},
{
"company": "TekCyte Pty Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "medical device",
"description": "Novel biomaterials for cell culture"
}
]
},
{
"company": "Teleaus Bioscience Health Pty Ltd (Genofax)",
"pipeline": [
{
"drug": "Genofax",
"phase": "Approved",
"type_of_drug": "diagnostic",
"description": "Genetic testing for various indications"
}
]
},
{
"company": "Telix Pharmaceuticals Pty Ltd",
"pipeline": [
{
"drug": "Illuccix",
"phase": "Phase 3",
"type_of_drug": "radiopharmaceutical",
"description": "PSMA-targeting radiopharmaceutical for prostate cancer imaging"
},
{
"drug": "TLX250-CDx",
"phase": "Phase 3",
"type_of_drug": "radiopharmaceutical",
"description": "CAIX-targeting radiopharmaceutical for kidney cancer imaging"
},
{
"drug": "TLX591",
"phase": "Phase 1",
"type_of_drug": "radiopharmaceutical",
"description": "PSMA-targeting radiopharmaceutical for prostate cancer therapy"
},
{
"drug": "TLX101",
"phase": "Phase 1",
"type_of_drug": "radiopharmaceutical",
"description": "18F-DOPA PET imaging agent for brain tumors"
},
{
"drug": "TLX250",
"phase": "Phase 1",
"type_of_drug": "radiopharmaceutical",
"description": "CAIX-targeting radiopharmaceutical for kidney cancer therapy"
},
{
"drug": "TLX650",
"phase": "Preclinical",
"type_of_drug": "radiopharmaceutical",
"description": "Novel radiopharmaceutical for cancer therapy"
},
{
"drug": "TLX300",
"phase": "Preclinical",
"type_of_drug": "radiopharmaceutical",
"description": "Novel radiopharmaceutical for cancer therapy"
}
]
},
{
"company": "Tessara Therapeutics",
"pipeline": [
{
"drug": "TTX-001",
"phase": "Preclinical",
"type_of_drug": "cell therapy",
"description": "Off-the-shelf dopamine replacement micro tissue therapy for Parkinson's disease"
}
]
},
{
"company": "Tissue Repair",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "medical device",
"description": "Novel biomaterials for tissue repair"
}
]
},
{
"company": "TruScreen Pty Ltd",
"pipeline": [
{
"drug": "TruScreen",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Cervical cancer screening device"
}
]
},
{
"company": "Universal Biosensors Pty Ltd",
"pipeline": [
{
"drug": "XeroSens",
"phase": "Approved",
"type_of_drug": "medical device",
"description": "Blood glucose monitoring system"
}
]
},
{
"company": "Vaxxas Pty Ltd",
"pipeline": [
{
"drug": "HD-MAP",
"phase": "Phase 1",
"type_of_drug": "vaccine delivery",
"description": "High-density microarray patch for vaccine delivery"
}
]
},
{
"company": "Vectus Biosystems Limited",
"pipeline": [
{
"drug": "VB198",
"phase": "Preclinical",
"type_of_drug": "small molecule",
"description": "Anti-cancer agent"
}
]
},
{
"company": "Vitrafy Life Sciences Ltd",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "medical device",
"description": "Novel biomaterials for cell culture"
}
]
},
{
"company": "Vitura Health Limited",
"pipeline": [
{
"drug": "Cannabis Products",
"phase": "Approved",
"type_of_drug": "cannabinoid",
"description": "Medical cannabis products for various indications"
}
]
},
{
"company": "VivaZome",
"pipeline": [
{
"drug": "TBA",
"phase": "Preclinical",
"type_of_drug": "exosomes",
"description": "mRNA delivery in exosomes"
}
]
}
]

# Flatten the nested structure
flattened_data = []
for company in data:
	for pipeline_item in company['pipeline']:
		flattened_data.append({
			'company': company['company'],
			**pipeline_item
		})

df = pd.DataFrame(flattened_data)
print(df.head())
df.to_csv('output.csv', index=False, header=True)
print("CSV file created: output.csv")