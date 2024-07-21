#------------------------------FIND CHEMICAL NAME FROM THE PDF------------------------

#-------------------------------------------------------------------------------------


# import fitz
# import json
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Define credentials and configurations
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# # Initialize LLM model
# parameters = {
#     "decoding_method": "greedy",
#     "max_new_tokens": 400,
#     "temperature": 0.2,
#     "stop_sequences": ["conclusion"]
# }

# model_id = ModelTypes.LLAMA_2_70B_CHAT
# llama = WatsonxLLM(
#     model_id=model_id.value,
#     url=credentials.get("url"),
#     apikey=credentials.get("apikey"),
#     project_id=project_id,
#     params=parameters
# )

# # Function to extract text from a PDF
# def extract_text_from_pdf(pdf_path):
#     try:
#         doc = fitz.open(pdf_path)
#         text = ""
#         for page in doc:
#             text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"Error occurred while extracting text from PDF: {str(e)}")
#         return None

# # Function to split text into chunks that fit within the token limit
# def split_text_into_chunks(text, max_tokens=1000):
#     sentences = text.split('. ')
#     chunks = []
#     current_chunk = []

#     current_tokens = 0
#     for sentence in sentences:
#         sentence_tokens = len(sentence.split())
#         if current_tokens + sentence_tokens > max_tokens:
#             chunks.append('. '.join(current_chunk) + '.')
#             current_chunk = [sentence]
#             current_tokens = sentence_tokens
#         else:
#             current_chunk.append(sentence)
#             current_tokens += sentence_tokens

#     if current_chunk:
#         chunks.append('. '.join(current_chunk) + '.')

#     return chunks

# # Function to use the LLM to extract details
# def extract_details_with_llm(text_chunks, llama_model):
#     response = []
#     for chunk in text_chunks:
#         prompt = f"Extract the Chemical Name from the following text:\n{chunk}"
#         response = llama_model.invoke(prompt)
#         # details.append(response)

#     return response
#     #     response = llama_model.invoke(prompt)
#     #     details.append(response)

#     # return details
        

# # Function to extract GHS statement details for a chemical
# def extract_ghs_statement(pdf_path, llama_model):
#     # Extract text from the PDF
#     pdf_text = extract_text_from_pdf(pdf_path)

#     if pdf_text:
#         # Split text into chunks
#         text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#         # Use LLM to extract details
#         details = extract_details_with_llm(text_chunks, llama_model)
        
#         # Create JSON structure
#         response_json = {
#             "ChemicalDetails": {
#                 # "Name": chemical_name,
#                 # "GHS_Statements": details 
#                 "Chemical_Name": details
#             }
#         }
        
#         # Print the extracted details in JSON format
#         print(json.dumps(response_json, indent=4))
#     else:
#         print("No text extracted from the PDF.")

# # Extract details for "Dimethyl glutarate"
# # chemical_name_dimethyl_glutarate = "Dimethyl glutarate"
# pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
# extract_ghs_statement(pdf_path_dimethyl_glutarate, llama)


# {
#     "ChemicalDetails": {
#         "Chemical_Name": "\n\nDimethyl glutarate\nDimethyl succinate\nDimethyl adipate\nDiethanolamine"
#     }
# }




#----------------------------------------------------------------------------------------------------------------

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
def extract_details_with_llm(text_chunks, llama_model):
    results = []
    for chunk in text_chunks:
        prompt = (
            "Extract chemical name from the following text and return the result as a JSON array of objects with 'Chemical name' fields:\n\n"
            f"{chunk}\n\n"
        )
        response = llama_model.invoke(prompt)
        if response:
            try:
                response_json = json.loads(response.strip())
                results.extend(response_json)
            # except json.JSONDecodeError as e:
            #     print(f"Error decoding JSON from chunk: {str(e)}")
            except json.JSONDecodeError:
                # Ignore the JSON decoding error
                continue
    return results

# Function to extract molecular formula and chemical name from a PDF
def extract_chemical_name(pdf_path, llama_model):
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    if pdf_text:
        # Split text into chunks
        text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

        # Use LLM to extract details
        details = extract_details_with_llm(text_chunks, llama_model)
        
        # Print the extracted details in JSON format
        if details:
            print(json.dumps(details, indent=4))
        else:
            print("No relevant information found.")
    else:
        print("No text extracted from the PDF.")

pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
extract_chemical_name(pdf_path_dimethyl_glutarate, llama)



# [
#     {
#         "Chemical name": "Dimethyl glutarate"
#     },
#     {
#         "Chemical name": "Dimethyl succinate"
#     },
#     {
#         "Chemical name": "Dimethyl adipate"
#     },
#     {
#         "Chemical name": "Diethanolamine"
#     }
# ]