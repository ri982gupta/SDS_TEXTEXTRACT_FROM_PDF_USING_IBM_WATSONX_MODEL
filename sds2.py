#-----------------------------------GHS STATEMENT THROUGH CHEMICAL NAME USING 2ND PDF----------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------



import fitz
import json
from langchain_ibm import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# Define credentials and configurations
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
}

project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# Initialize LLM model
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 400,
    "temperature": 0.2,
    "stop_sequences": ["conclusion"]
}

model_id = ModelTypes.LLAMA_2_70B_CHAT
llama = WatsonxLLM(
    model_id=model_id.value,
    url=credentials.get("url"),
    apikey=credentials.get("apikey"),
    project_id=project_id,
    params=parameters
)

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error occurred while extracting text from PDF: {str(e)}")
        return None

# Function to split text into chunks that fit within the token limit
def split_text_into_chunks(text, max_tokens=1000):
    sentences = text.split('. ')
    chunks = []
    current_chunk = []

    current_tokens = 0
    for sentence in sentences:
        sentence_tokens = len(sentence.split())
        if current_tokens + sentence_tokens > max_tokens:
            chunks.append('. '.join(current_chunk) + '.')
            current_chunk = [sentence]
            current_tokens = sentence_tokens
        else:
            current_chunk.append(sentence)
            current_tokens += sentence_tokens

    if current_chunk:
        chunks.append('. '.join(current_chunk) + '.')

    return chunks

# Function to use the LLM to extract details
def extract_details_with_llm(text_chunks, chemical_name, llama_model):
    details = []
    for chunk in text_chunks:
        prompt = f"Extract the GHS statement for the chemical name '{chemical_name}' from the following text:\n{chunk}"
        response = llama_model.invoke(prompt)
        details.append(response)

    return details

# Path to the PDF file
pdf_path = "Caulk SDS 1.pdf"
chemical_name = "Dimethyl glutarate"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

if pdf_text:
    # Split text into chunks
    text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

    # Use LLM to extract details
    details = extract_details_with_llm(text_chunks, chemical_name, llama)
    
    # Create JSON structure
    response_json = {
        "ChemicalDetails": {
            "Name": chemical_name,
            "GHS_Statements": details
        }
    }
    
    # Print the extracted details in JSON format
    print(json.dumps(response_json, indent=4))
else:
    print("No text extracted from the PDF.")


# {
#     "ChemicalDetails": {
#         "Name": "Dimethyl glutarate",
#         "GHS_Statements": [
#             "  Ingestion of large quantities may cause gastrointestinal irritation, nausea, vomiting, \ndiarrhea, and abdominal pain.\n12. Ecological Information\nECOLOGICAL INFORMATION: Not available.\n13. Disposal Considerations\nDISPOSAL METHODS: Dispose of in accordance with applicable regulations.  Dispose of in a sealed container.\n14. Transport Information\nUN Number:\nUN1263\nPacking Group:\nIII\nTransport Hazard Class:\n3\nTransport Hazard Subclass:\n3\nTransport Hazard Category:\n8\nSpecial Provisions:\nNone\n15. Regulatory Information\nOSHA HAZARD COMMUNICATION STANDARD (29 CFR 1910.1200)\nThis product is covered by the OSHA Hazard 
# Communication Standard.  This document has been prepared in accordance with \nrequirements of this standard.  All abbreviated terms used in this SDS are further described in Section 16.\n16. Other Information\nABBREVIATIONS USED IN THIS SDS:\nGHS - Globally Harmonized System of Classification and Labeling of Chemicals\nH319 - Causes serious eye irritation\nH331 - Causes skin sensitization\nH332 - Causes respiratory sensitization\nH373 - May cause allergic sensitization\nH411 - Repeated exposure may cause skin sensitization\nH412 - Repeated exposure may cause respiratory sensitization\nH413 - Repeated exposure may cause allergic sensitization\nH4",
#             "\n\nGHS hazard statement for Dimethyl glutarate:\nH302: Harmful if swallowed.\nH315: Causes skin irritation.\nH318: Causes serious eye damage.\nH319: Causes serious eye irritation.\nH331: Toxic if inhaled.\nH332: Harmful if inhaled.\nH373: May cause damage to organs through prolonged or repeated exposure."
#         ]
#     }
# }



