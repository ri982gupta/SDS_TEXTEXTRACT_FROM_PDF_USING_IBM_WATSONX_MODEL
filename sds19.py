#----------------------------------- FIND GHS STATEMENT ALPHANUMBERIC ------------------------------

#---------------------------------------------------------------------------------------------------



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
    response = []
    for chunk in text_chunks:
        prompt = f"Extract the GHS statements alphanumberic for the chemical name '{chemical_name}' from the following text:\n{chunk}"
        response = llama_model.invoke(prompt)
        # details.append(response)

    return response
    #     response = llama_model.invoke(prompt)
    #     details.append(response)

    # return details
        

# Function to extract GHS statement details for a chemical
def extract_ghs_statement(chemical_name, pdf_path, llama_model):
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    if pdf_text:
        # Split text into chunks
        text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

        # Use LLM to extract details
        details = extract_details_with_llm(text_chunks, chemical_name, llama_model)
        
        # Create JSON structure
        response_json = {
            "ChemicalDetails": {
                "Name": chemical_name,
                # "GHS_Statements": details 
                "GHS Statements": details
            }
        }
        
        # Print the extracted details in JSON format
        print(json.dumps(response_json, indent=4))
    else:
        print(f"No text extracted from the PDF for {chemical_name}.")

# Extract details for "Dimethyl glutarate"
chemical_name_dimethyl_glutarate = "Dimethyl glutarate"
pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
extract_ghs_statement(chemical_name_dimethyl_glutarate, pdf_path_dimethyl_glutarate, llama)


# {
#     "ChemicalDetails": {
#         "Name": "Dimethyl glutarate",
#         "GHS Statements": "\n\nThe GHS statements alphanumeric for the chemical name 'Dimethyl glutarate' are:\n\nH302: Harmful if swallowed.\nH315: Causes skin irritation.\nH318: Causes serious eye damage.\nH319: Causes serious eye irritation.\nH331: Toxic if inhaled.\nH332: Harmful if inhaled.\nH373: May cause damage to organs through prolonged or repeated exposure."
#     }
# }