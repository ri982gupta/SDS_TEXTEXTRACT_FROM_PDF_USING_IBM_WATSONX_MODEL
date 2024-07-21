#------------------------------------------ FIND CAS NUMBER OF CHEMICAL NAME-----------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------


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
        prompt = f"Extract the CAS Number for the chemical name '{chemical_name}' from the following text:\n{chunk}"
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
                "CAS_Number": details
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

# # Function to generate prompts for LLM model
# def generate_prompts(text, chemical_id):
#     prompts = []
#     # Split text into sentences
#     sentences = text.split('.')
#     for sentence in sentences:
#         if chemical_id in sentence:
#             # Generate prompt for the LLM model
#             prompt = f"Extract chemical information from the following sentence:\n\n{sentence.strip()}\n\n"
#             prompts.append(prompt)
#     return prompts

# # Function to extract chemical information using LLM model
# def extract_chemical_info(llm_model, text, chemical_id):
#     try:
#         # Generate prompts for LLM model
#         prompts = generate_prompts(text, chemical_id)
        
#         extracted_info = []
#         # Invoke LLM model with prompts
#         for prompt in prompts:
#             response = llm_model.invoke(prompt)
#             extracted_info.append(response.strip())
        
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during LLM extraction: {str(e)}")
#         return None

# # Ask for chemical ID from the user
# chemical_id = input("Please enter the chemical ID: ")

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF using fitz
# try:
#     doc = fitz.open(pdf_path)
#     pdf_text = ""
#     for page in doc:
#         pdf_text += page.get_text()
# except Exception as e:
#     print(f"Error occurred while extracting text from PDF: {str(e)}")
#     pdf_text = None

# if pdf_text:
#     # Extract chemical information using LLM model
#     chemical_info = extract_chemical_info(llama, pdf_text, chemical_id)

#     # Print the extracted information in JSON format
#     if chemical_info:
#         # Construct JSON object
#         json_output = {
#             chemical_id: chemical_info
#         }
#         print(json.dumps(json_output, indent=4))
#     else:
#         print(f"No information found for chemical identifier {chemical_id}.")
# else:
#     print("No text extracted from the PDF.")


# {
#     "ChemicalDetails": {
#         "Name": "Dimethyl glutarate",
#         "CAS_Number": "\n\nThe CAS Number for the chemical name 'Dimethyl glutarate' is 111-40-0."
#     }
# }