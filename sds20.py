#----------------------------------- FIND GHS STATEMENT ALPHANUMBERIC AND DETAILS FROM ANOTHER PDF------------------------------

#-------------------------------------------------------------------------------------------------------------------------------



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
# def extract_details_with_llm(text_chunks, chemical_name, llama_model):
#     response = []
#     for chunk in text_chunks:
#         prompt = f"Extract the GHS statements alphanumberic for the chemical name '{chemical_name}' from the following text:\n{chunk}"
#         response = llama_model.invoke(prompt)
#         # details.append(response)

#     return response
#     #     response = llama_model.invoke(prompt)
#     #     details.append(response)

#     # return details
        

# # Function to extract GHS statement details for a chemical
# def extract_ghs_statement(chemical_name, pdf_path, llama_model):
#     # Extract text from the PDF
#     pdf_text = extract_text_from_pdf(pdf_path)

#     if pdf_text:
#         # Split text into chunks
#         text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#         # Use LLM to extract details
#         details = extract_details_with_llm(text_chunks, chemical_name, llama_model)
        
#         # Create JSON structure
#         response_json = {
#             "ChemicalDetails": {
#                 "Name": chemical_name,
#                 # "GHS_Statements": details 
#                 "GHS Statements": details
#             }
#         }
        
#         # Print the extracted details in JSON format
#         print(json.dumps(response_json, indent=4))
#     else:
#         print(f"No text extracted from the PDF for {chemical_name}.")



# # Extract details for "Dimethyl glutarate"
# chemical_name_dimethyl_glutarate = "Dimethyl glutarate"
# pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
# extract_ghs_statement(chemical_name_dimethyl_glutarate, pdf_path_dimethyl_glutarate, llama)


# # Function to generate prompts for LLM model
# def generate_prompts(text, chemical_id):
#     prompts = []
#     # Split text into sentences
#     sentences = text.split('.')
#     for sentence in sentences:
#         if chemical_id in sentence:
#             # Generate prompt for the LLM model
#             prompt = f"Extract Health hazard statements of {chemical_id} from the following sentence:\n\n{sentence.strip()}\n\n"
#             # prompts.append(prompt)
#     return prompt

# # Function to extract chemical information using LLM model
# def extract_chemical_info(llm_model, text, chemical_id):
#     try:
#         # Generate prompts for LLM model
#         prompts = generate_prompts(text, chemical_id)
        
#         extracted_info = []
#         # Invoke LLM model with prompts
#         for prompt in prompts:
#             # response = llm_model.invoke(prompt)
#             # extracted_info.append(response.strip())
#             extracted_info = llm_model.invoke(prompt)
        
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
#         "GHS Statements": "\n\nThe GHS statements alphanumeric for the chemical name 'Dimethyl glutarate' are:\n\nH302: Harmful if swallowed.\nH315: Causes skin irritation.\nH318: Causes serious eye damage.\nH319: Causes serious eye irritation.\nH331: Toxic if inhaled.\nH332: Harmful if inhaled.\nH373: May cause damage to organs through prolonged or repeated exposure."
#     }
# }
# Please enter the chemical ID: H331
# {
#     "H331": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
# }


# # Function to use the LLM to extract details
# def extract_details_ghs_with_llm(text_chunks, chemical_name, llama_model):
#     response = []
#     for chunk in text_chunks:
#         prompt = f"Extract the GHS statements alphanumberic details for '{chemical_name}' from the following text:\n{chunk}"
#         response = llama_model.invoke(prompt)
#         # details.append(response)

#     return response



# def extract_ghs_statement_number(ghs_name, pdf_path, llama_model):
#     # Extract text from the PDF
#     pdf_text = extract_text_from_pdf(pdf_path)

#     if pdf_text:
#         # Split text into chunks
#         text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#         # Use LLM to extract details
#         details = extract_details_ghs_with_llm(text_chunks, ghs_name, llama_model)
        
#         # Create JSON structure
#         response_json = {
#             "ChemicalDetails": {
#                 "Name": ghs_name,
#                 # "GHS_Statements": details 
#                 "GHS Statements": details
#             }
#         }
        
#         # Print the extracted details in JSON format
#         print(json.dumps(response_json, indent=4))
#     else:
#         print(f"No text extracted from the PDF for {ghs_name}.")

# ghs_statement_num =  input("Please enter the GHS Statement number: ")
# pdf_path = "GHS Rev10e.pdf"
# extract_ghs_statement_number(ghs_statement_num, pdf_path, llama)



#-------------------------------------------------------------------------------------------------------------------------------



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

# Function to generate prompts for LLM model
def generate_prompts(text, chemical_id):
    prompts = []
    # Split text into sentences
    sentences = text.split('.')
    for sentence in sentences:
        if chemical_id in sentence:
            # Generate prompt for the LLM model
            prompt = f"Extract chemical information from the following sentence:\n\n{sentence.strip()}\n\n"
            prompts.append(prompt)
    return prompts

# Function to extract chemical information using LLM model
def extract_chemical_info(llm_model, text, chemical_id):
    try:
        # Generate prompts for LLM model
        prompts = generate_prompts(text, chemical_id)
        
        extracted_info = []
        # Invoke LLM model with prompts
        for prompt in prompts:
            response = llm_model.invoke(prompt)
            extracted_info.append(response.strip())
        
        return extracted_info
    except Exception as e:
        print(f"Error occurred during LLM extraction: {str(e)}")
        return None

# Ask for chemical ID from the user
chemical_id = input("Please enter the chemical ID: ")

# Path to the PDF file
pdf_path = "GHS Rev10e.pdf"

# Extract text from the PDF using fitz
try:
    doc = fitz.open(pdf_path)
    pdf_text = ""
    for page in doc:
        pdf_text += page.get_text()
except Exception as e:
    print(f"Error occurred while extracting text from PDF: {str(e)}")
    pdf_text = None

if pdf_text:
    # Extract chemical information using LLM model
    chemical_info = extract_chemical_info(llama, pdf_text, chemical_id)

    # Print the extracted information in JSON format
    if chemical_info:
        # Construct JSON object
        json_output = {
            chemical_id: chemical_info
        }
        print(json.dumps(json_output, indent=4))
    else:
        print(f"No information found for chemical identifier {chemical_id}.")
else:
    print("No text extracted from the PDF.")


# {
#     "ChemicalDetails": {
#         "Name": "Dimethyl glutarate",
#         "GHS Statements": "\n\nThe GHS statements alphanumeric for the chemical name 'Dimethyl glutarate' are:\n\nH302: Harmful if swallowed.\nH315: Causes skin irritation.\nH318: Causes serious eye damage.\nH319: Causes serious eye irritation.\nH331: Toxic if inhaled.\nH332: Harmful if inhaled.\nH373: May cause damage to organs through prolonged or repeated exposure."
#     }
# }
# Please enter the chemical ID: H331
# {
#     "H331": [
#         "b \nUnder the UN Model Regulations, toxic liquids are classified in Division 3\n\nc \nUnder the UN Model Regulations, toxic solids are classified in Division 4\n\nd \nUnder the UN Model Regulations, toxic substances that are fatal if swallowed, inhaled, or in contact with skin are classified in Division 5\n\ne \nUnder the UN Model Regulations, toxic substances that are toxic if swallowed, inhaled, or in contact with skin 
# are classified in Division 6\n\nf \nUnder the UN Model Regulations, toxic substances that are harmful if swallowed, inhaled, or in contact with skin are classified in Division 7\n\ng \nUnder the UN Model Regulations, 
# toxic substances that are not classified in any of the above Divisions are classified in Division 8\n\nh \nUnder the UN Model Regulations, toxic substances that are not classified in any of the above Divisions and are not pictogrammed are classified in Division 9\n\ni \nUnder the UN Model Regulations, toxic substances that are not classified in any of the above Divisions and are pictogrammed are classified in Division 10\n\nj \nUnder the UN Model Regulations, toxic substances that are classified in Division 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10 are considered hazardous.\n\nk \nUnder the UN Model Regulations, toxic substances that are not classified in any of the above Divisions and are not pictogrammed are not considered hazardous.\n\nl \nUnder the UN Model Regulations, toxic subst",
#         "The chemical information in this sentence includes:\n\n* The chemical name: H331\n* The chemical formula: not provided\n* The chemical structure: not provided\n* Physical and chemical properties: toxic if inhaled\n* Health hazards: acute toxicity, inhalation\n* Safety information: chapter 3\n\nNote: The number 1 at the beginning of the sentence is not part of the chemical information.",
#         "2) \nH301 \n+ \nH311 \nToxic if swallowed or if inhaled \nAcute toxicity, oral (chapter 3\n\n3) \nH301 \n+ \nH331 \nToxic if swallowed or if inhaled \nAcute toxicity, inhalation (chapter 3\n\n4) \nH301 \n+ \nH311 \nToxic if swallowed or if inhaled \nAcute toxicity, inhalation (chapter 3\n\n5) \nH301 \n+ \nH331 \nToxic if swallowed or if inhaled \nAcute toxicity, dermal (chapter 3\n\n6) \nH301 \n+ \nH311 \nToxic if swallowed or if inhaled \nAcute toxicity, dermal (chapter 3\n\n7) \nH301 \n+ \nH331 \nToxic if swallowed or if inhaled \nAcute toxicity, eye (chapter 3\n\n8) \nH301 \n+ \nH311 \nToxic if swallowed or if inhaled \nAcute toxicity, eye (chapter 3\n\n9) \nH301 \n+ \nH331 \nToxic if swallowed or if inhaled \nAcute toxicity, respiratory (chapter 3\n\n10) \nH301 \n+ \nH311 \nToxic if swallowed or if inhaled \nAcute toxicity, resp",
#         "2) \nH311 \n+ \nH331 \nToxic in contact with skin or if inhaled \nAcute toxicity, inhalation (chapter 3)\n\n3) \nH311 \n+ \nH331 \nToxic in contact with skin or if inhaled \nAcute toxicity, oral (chapter 3)\n\n4) \nH311 \n+ \nH331 \nToxic in contact with skin or if inhaled \nAcute toxicity, dermal (chapter 3)\n\n5) \nH311 \n+ \nH331 \nToxic in contact with skin or if inhaled \nAcute toxicity, eye (chapter 3)\n\n6) \nH311 
# \n+ \nH331 \nToxic in contact with skin or if inhaled \nAcute toxicity, respiratory (chapter 3)\n\n7) \nH311 \n+ \nH331 \nToxic in contact with skin or if inhaled \nAcute toxicity, other (chapter 3)\n\n8) \nH311 \n+ \nH331 \nToxic in contact with skin or if inhaled \nChronic toxicity (chapter 3)\n\n9) \nH311 \n+ \nH331 \nToxic in contact with skin or if inhaled \nReproductive toxicity (chapter 3)\n\n10) \nH311 \n+ \nH331 \nToxic in contact with skin or if in",
#         "The chemical information that can be extracted from the sentence is:\n\n* H301\n* H311\n* H331\n\nThese are the chemical names or identifiers for the substances being described as toxic. The \"H\" prefix indicates that these are hydrogen compounds. The numbers following the \"H\" prefix are likely to be the atomic numbers of the elements in the molecule.\n\nIt's worth noting that the sentence also includes information about the toxicity of the substances, specifically that they are toxic if swallowed, in contact with skin, or if inhaled, and that they have acute toxicity, oral (chapter 3). However, this information is not directly related to the chemical structure of the substances, but rather to their effects on human health.",
#         "2) \n- 377 \nHazard category \nSymbol \nSignal word \nHazard statement \nSkull and crossbones \nDanger \nH319 \nCauses skin irritation \nPrecautionary statements \nPrevention \nResponse \nStorage \nDisposal \nP280 \nWear protective gloves/protective clothing/eye protection/face protection \n\n3) \n- 378 \nHazard category \nSymbol \nSignal word \nHazard statement \nSkull and crossbones \nDanger \nH411 \nRepeated exposure may cause skin sensitization \nPrecautionary statements \nPrevention \nResponse \nStorage \nDisposal \nP270 \nDo not get in eyes, on skin, or on clothing \n\nPlease extract the following information from the given sentences:\n\n1. Hazard category\n2. Symbol\n3. Signal word\n4. Hazard statement\n5. Precautionary statements\n6. Response\n7. Storage\n8. Disposal\n\nand present it in a tabular format.\n\n| Hazard Category | Symbol | Signal Word | Hazard Statement | Precautionary Statements | Response | Storage | Disposal |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n| 376 | H331 | Danger | Toxic if inhaled | Avoid breathing dust/fume/gas/mist/vapours/spray | - | - | - |\n| 377 | H319 | Danger | Causes skin ir"
#     ]
# }



#--------------------------------------------------------------------------------------------------------------------------------------------------------


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
# def extract_details_with_llm(text_chunks, chemical_name, llama_model):
#     response = []
#     for chunk in text_chunks:
#         prompt = f"Extract the GHS statements alphanumberic for the chemical name '{chemical_name}' from the following text:\n{chunk}"
#         response = llama_model.invoke(prompt)
#         # details.append(response)

#     return response
#     #     response = llama_model.invoke(prompt)
#     #     details.append(response)

#     # return details
        

# # Function to extract GHS statement details for a chemical
# def extract_ghs_statement(chemical_name, pdf_path, llama_model):
#     # Extract text from the PDF
#     pdf_text = extract_text_from_pdf(pdf_path)

#     if pdf_text:
#         # Split text into chunks
#         text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#         # Use LLM to extract details
#         details = extract_details_with_llm(text_chunks, chemical_name, llama_model)
        
#         # Create JSON structure
#         response_json = {
#             "ChemicalDetails": {
#                 "Name": chemical_name,
#                 # "GHS_Statements": details 
#                 "GHS Statements": details
#             }
#         }
        
#         # Print the extracted details in JSON format
#         print(json.dumps(response_json, indent=4))
#     else:
#         print(f"No text extracted from the PDF for {chemical_name}.")



# # Extract details for "Dimethyl glutarate"
# chemical_name_dimethyl_glutarate = "Dimethyl glutarate"
# pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
# extract_ghs_statement(chemical_name_dimethyl_glutarate, pdf_path_dimethyl_glutarate, llama)

# # Function to generate prompts for LLM model
# def generate_prompts(text, chemical_id):
#     prompt = []
#     # Split text into sentences
#     sentences = text.split('.')
#     for sentence in sentences:
#         if chemical_id in sentence:
#             # Generate prompt for the LLM model
#             prompt = f"Extract chemical information from the following sentence:\n\n{sentence.strip()}\n\n"
          
#     return prompt

# # Function to extract chemical information using LLM model
# def extract_chemical_info(llm_model, text, chemical_id):
#     try:
#         # Generate prompts for LLM model
#         prompts = generate_prompts(text, chemical_id)
        
#         extracted_info = []
#         # Invoke LLM model with prompts
#         for prompt in prompts:
#             extracted_info = llm_model.invoke(prompt)
            
        
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
#         "GHS Statements": "\n\nThe GHS statements alphanumeric for the chemical name 'Dimethyl glutarate' are:\n\nH302: Harmful if swallowed.\nH315: Causes skin irritation.\nH318: Causes serious eye damage.\nH319: Causes serious eye irritation.\nH331: Toxic if inhaled.\nH332: Harmful if inhaled.\nH373: May cause damage to organs through prolonged or repeated exposure."
#     }
# }
# Please enter the chemical ID: H331
# {
#     "H331": "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
# }




# # Function to use the LLM to extract details
# def extract_details_with_llm_h(text_chunks, chemical_name_h, llama_model):
#     response = []
#     for chunk in text_chunks:
#         prompt = f"Extract the GHS statements alphanumberic for the chemical name '{chemical_name_h}' from the following text:\n{chunk}"
#         response = llama_model.invoke(prompt)
#         # details.append(response)

#     return response
#     #     response = llama_model.invoke(prompt)
#     #     details.append(response)

#     # return details
        

# # Function to extract GHS statement details for a chemical
# def extract_ghs_statement_h(chemical_name_h, pdf_path_h, llama_model):
#     # Extract text from the PDF
#     pdf_text = extract_text_from_pdf(pdf_path_h)

#     if pdf_text:
#         # Split text into chunks
#         text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#         # Use LLM to extract details
#         details = extract_details_with_llm_h(text_chunks, chemical_name_h, llama_model)
        
#         # Create JSON structure
#         response_json = {
#             "ChemicalDetails": {
#                 "Name": chemical_name_h,
#                 # "GHS_Statements": details 
#                 "GHS Statements Number": details
#             }
#         }
        
#         # Print the extracted details in JSON format
#         print(json.dumps(response_json, indent=4))
#     else:
#         print(f"No text extracted from the PDF for {chemical_name_h}.")



# # Extract details for "Dimethyl glutarate"
# chemical_name_h = "H331"
# pdf_path_h = "GHS Rev10e.pdf"
# extract_ghs_statement_h(chemical_name_h, pdf_path_h, llama)