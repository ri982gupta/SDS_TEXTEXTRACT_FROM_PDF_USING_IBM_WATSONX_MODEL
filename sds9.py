#---------------------------------------------FIND GENRAL INFO FROM 2ND PDF-----------------------------------------------------------------------

# Molecular formula 
# Molecular weight
# Physical state (solid, liquid, gas)
# Appearance
# Odor
# pH
# Melting point
# Boiling point
# Flash point
# Density
# Solubility in water
# Solubility in other solvents
# Vapor pressure
# Autoignition temperature
# Decomposition temperature

#--------------------------------------------------------------------------------------------------------------------------------------------------


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
#     results = []
#     for chunk in text_chunks:
#         prompt = (
#             "Extract the following details from the text and return the result as a JSON array of objects with fields:\n"
#             "'Molecular formula', 'Chemical name', 'Molecular weight', 'Physical state', 'Appearance', 'Odor', 'pH', 'Melting point', "
#             "'Boiling point', 'Flash point', 'Density', 'Solubility in water', 'Solubility in other solvents', 'Vapor pressure', "
#             "'Autoignition temperature', 'Decomposition temperature':\n\n"
#             f"{chunk}\n\n"
#         )
#         response = llama_model.invoke(prompt)
#         if response:
#             try:
#                 response_json = json.loads(response.strip())
#                 results.extend(response_json)
#             except json.JSONDecodeError:
#                 # Ignore the JSON decoding error
#                 continue
#     return results

# # Function to extract various details from a PDF
# def extract_details_from_pdf(pdf_path, llama_model):
#     # Extract text from the PDF
#     pdf_text = extract_text_from_pdf(pdf_path)

#     if pdf_text:
#         # Split text into chunks
#         text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#         # Use LLM to extract details
#         details = extract_details_with_llm(text_chunks, llama_model)
        
#         # Print the extracted details in JSON format
#         if details:
#             print(json.dumps(details, indent=4))
#         else:
#             print("No relevant information found.")
#     else:
#         print("No text extracted from the PDF.")

# pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
# extract_details_from_pdf(pdf_path_dimethyl_glutarate, llama)


# No relevant information found.


#--------------------------------------------------------------------------------------------------------------------------------


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

# # Function to use the LLM to extract specific detail
# def extract_specific_detail(text_chunks, detail_name, llama_model):
#     for chunk in text_chunks:
#         prompt = (
#             f"Extract the {detail_name} from the following text and return the result as a JSON object with '{detail_name}' field:\n\n"
#             f"{chunk}\n\n"
#         )
#         response = llama_model.invoke(prompt)
#         if response:
#             try:
#                 response_json = json.loads(response.strip())
#                 if detail_name in response_json:
#                     return {detail_name: response_json[detail_name]}
#             except json.JSONDecodeError:
#                 # Ignore the JSON decoding error
#                 continue
#     return {detail_name: "Not found"}

# # Function to extract various details from a PDF
# def extract_details_from_pdf(pdf_path, llama_model):
#     # Extract text from the PDF
#     pdf_text = extract_text_from_pdf(pdf_path)

#     if pdf_text:
#         # Split text into chunks
#         text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#         # List of details to extract
#         details_to_extract = [
#             "Appearance", "Odor", "pH", "Melting point", "Boiling point",
#             "Flash point", "Density", "Solubility in water", "Solubility in other solvents",
#             "Vapor pressure", "Autoignition temperature", "Decomposition temperature"
#         ]

#         # Extract each detail independently
#         found_details = {}
#         for detail in details_to_extract:
#             found_details.update(extract_specific_detail(text_chunks, detail, llama_model))

#         # Print the extracted details in JSON format
#         print(json.dumps(found_details, indent=4))
#     else:
#         print("No text extracted from the PDF.")

# pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
# extract_details_from_pdf(pdf_path_dimethyl_glutarate, llama)

# {
#     "Chemical name": "Not found",
#     "Appearance": "Not specified",
#     "Odor": "Not found",
#     "pH": "Not found",
#     "Melting point": "Not found",
#     "Boiling point": "N.A.",
#     "Flash point": "Not found",
#     "Density": "1.0-1.2 g/cm3",
#     "Solubility in water": "Not found",
#     "Solubility in other solvents": {
#         "VOC Less Water Less Exempt Solvent": 999.9,
#         "VOC Material": 357,
#         "VOC as Defined by California Consumer Product Regulation": 34.5
#     },
#     "Vapor pressure": "> 11 mg/L Rat",
#     "Autoignition temperature": "Not found",
#     "Decomposition temperature": "Not found"
# }


#--------------------------------------------------------------------------------------------------------------------------


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

# # Function to use the LLM to extract specific detail
# def extract_specific_detail(text_chunks, detail_name, llama_model):
#     for chunk in text_chunks:
#         prompt = (
#             f"Extract the {detail_name} from the following text and return the result as a JSON object with '{detail_name}' field:\n\n"
#             f"{chunk}\n\n"
#         )
#         response = llama_model.invoke(prompt)
#         if response:
#             try:
#                 response_json = json.loads(response.strip())
#                 if detail_name in response_json:
#                     return {detail_name: response_json[detail_name]}
#             except json.JSONDecodeError:
#                 # Ignore the JSON decoding error
#                 continue
#     return {detail_name: "Not Established"}

# # Function to extract various details from a PDF
# def extract_details_from_pdf(pdf_path, llama_model):
#     # Extract text from the PDF
#     pdf_text = extract_text_from_pdf(pdf_path)

#     if pdf_text:
#         # Split text into chunks
#         text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#         # List of details to extract
#         details_to_extract = [
#             "Appearance", "Physical State", "Odor", "Odor Threshold", "Density, g/cm3",
#             "pH", "Freeze Point, °C", "Viscosity (mPa.s)", "Solubility in Water",
#             "Partition Coeff., n-octanol/water", "Decomposition Temperature, °C",
#             "Explosive Limits, %", "Boiling Range, °C", "Auto-Ignition Temperature, °C",
#             "Minimum Flash Point, °C", "Vapor Pressure, mmHg", "Evaporation Rate",
#             "Flash Method", "Vapor Density", "Flammability, NFPA"
#         ]

#         # Extract each detail independently
#         found_details = {}
#         for detail in details_to_extract:
#             found_details.update(extract_specific_detail(text_chunks, detail, llama_model))

#         # Format the details for printing
#         formatted_details = []
#         for detail in details_to_extract:
#             formatted_details.append(f"{detail}: {found_details.get(detail, 'Not Established')}")

#         # Print the formatted details
#         print('\n'.join(formatted_details))
#     else:
#         print("No text extracted from the PDF.")

# pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
# extract_details_from_pdf(pdf_path_dimethyl_glutarate, llama)

# Appearance: Not specified
# Physical State: {'Gastrointestinal irritation': 'nausea, vomiting, diarrhea', 'Eye irritation': 'serious eye damage, causes serious eye irritation', 'Skin irritation': 'causes skin irritation'}
# Odor: Not Established
# Odor Threshold: Not Established
# Density, g/cm3: Not Established
# pH: Not Established
# Freeze Point, °C: Not Established
# Viscosity (mPa.s): Not Established
# Solubility in Water: Not Established
# Partition Coeff., n-octanol/water: Not Established
# Decomposition Temperature, °C: Not Established
# Explosive Limits, %: Not Established
# Boiling Range, °C: Not Established
# Auto-Ignition Temperature, °C: Not Established
# Minimum Flash Point, °C: Not Established
# Vapor Pressure, mmHg: Not Established
# Evaporation Rate: Not Established
# Flash Method: GHS05
# Vapor Density: > 11 mg/L Rat
# Flammability, NFPA: 2



#-----------------------------------------------------------------------------------------------------------------------------------------------

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

# # Function to use the LLM to extract specific detail
# def extract_specific_detail(text_chunks, detail_name, llama_model):
#     for chunk in text_chunks:
#         prompt = (
#             f"Extract the {detail_name} from the following text and return the result as a plain string:\n\n"
#             f"{chunk}\n\n"
#             f"If the {detail_name} is not mentioned, return 'Not Established'."
#         )
#         response = llama_model.invoke(prompt)
#         if response:
#             response_text = response.strip()
#             if response_text and response_text.lower() != 'not established':
#                 return {detail_name: response_text}
#     return {detail_name: "Not Established"}

# # Function to extract various details from a PDF
# def extract_details_from_pdf(pdf_path, llama_model):
#     # Extract text from the PDF
#     pdf_text = extract_text_from_pdf(pdf_path)

#     if pdf_text:
#         # Split text into chunks
#         text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#         # List of details to extract
#         details_to_extract = [
#             "Appearance", "Physical State", "Odor", "Odor Threshold", "Density, g/cm3",
#             "pH", "Freeze Point, °C", "Viscosity (mPa.s)", "Solubility in Water",
#             "Partition Coeff., n-octanol/water", "Decomposition Temperature, °C",
#             "Explosive Limits, %", "Boiling Range, °C", "Auto-Ignition Temperature, °C",
#             "Minimum Flash Point, °C", "Vapor Pressure, mmHg", "Evaporation Rate",
#             "Flash Method", "Vapor Density", "Flammability, NFPA", "Combustible Dust"
#         ]

#         # Extract each detail independently
#         found_details = {}
#         for detail in details_to_extract:
#             detail_result = extract_specific_detail(text_chunks, detail, llama_model)
#             found_details.update(detail_result)

#         # Print the extracted details in JSON format
#         print(json.dumps(found_details, indent=4))
#     else:
#         print("No text extracted from the PDF.")

# pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
# extract_details_from_pdf(pdf_path_dimethyl_glutarate, llama)



# {
#     "Appearance": "The Appearance is: Colored.",
#     "Physical State": "The Physical State of the product is: Thick Liquid",
#     "Odor": "The Odor of the product is: Fruity",
#     "Odor Threshold": "The Odor Threshold is: Not Established",
#     "Density, g/cm3": "Please return the density value as a plain string, without any units. If the density is not mentioned, return 'Not Established'.",
#     "pH": "The pH of the product is not explicitly mentioned in the provided SDS. Therefore, the answer is:\n\npH: Not Established",
#     "Freeze Point, \u00b0C": "Please provide the actual Freeze Point, \u00b0C value if it is mentioned in the SDS.",
#     "Viscosity (mPa.s)": "Please return the Viscosity (mPa.s) of the product.",
#     "Solubility in Water": "Please return the Solubility in Water value as a plain string, without the units. If the value is not mentioned, return 'Not Established'.",
#     "Partition Coeff., n-octanol/water": "Please return the Partition Coeff., n-octanol/water value as a plain string, without any unit or 'Not Established' mention.\n\nFor example, if the SDS contains the following information:\n\nPartition Coeff., n-octanol/water: 3.4\n\nThen, the expected result is: 3.4\n\nIf the SDS does not contain any information about the Partition Coeff., n-octanol/water, then the expected result is: Not Established",
#     "Decomposition Temperature, \u00b0C": "Please provide the actual temperature value if mentioned in the SDS.",
#     "Explosive Limits, %": "Please return the Explosive Limits, % as a plain string, without the units (%).",
#     "Boiling Range, \u00b0C": "Please provide the actual Boiling Range, \u00b0C from the SDS.",
#     "Auto-Ignition Temperature, \u00b0C": "Please provide the actual value if mentioned in the SDS.",
#     "Minimum Flash Point, \u00b0C": "Please provide the Minimum Flash Point, \u00b0C from the SDS and I will be happy to assist you further.",
#     "Vapor Pressure, mmHg": "Please return the Vapor Pressure, mmHg value as a plain string, without the unit. If the value is not mentioned, return 'Not Established'.",
#     "Evaporation Rate": "Please note that the SDS is written following a specific format and the information provided may vary depending on the product and the manufacturer.",
#     "Flash Method": "The Flash Method for this product is:\nSeta Closed Cup",
#     "Vapor Density": "Please return the Vapor Density of the product.",
#     "Flammability, NFPA": "Please provide the actual value for the Flammability, NFPA.\n\nPlease note that the SDS is from 2019, and some values might have changed.",
#     "Combustible Dust": "Combustible Dust: Does not support combustion"
# }



#---------------------------------------------------------------------------------------------------------------------------------


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

# Function to use the LLM to extract specific detail
def extract_specific_detail(text_chunks, detail_name, llama_model):
    # results = []
    for chunk in text_chunks:
        prompt = (
            f"Extract the {detail_name} from the following text and return the result as a plain string:\n\n"
            f"{chunk}\n\n"
            f"If the {detail_name} is not mentioned, return 'Not Established'."
        )
        response = llama_model.invoke(prompt)
        if response:
            response_text = response.strip()
            # if response_text and response_text.lower() != 'not established':
            #     return {detail_name: response_text}
            return {detail_name: response_text}
        
    # return {detail_name: "Not Established"}
    #     response = llama_model.invoke(prompt)
    #     if response:
    #         try:
    #             response_json = json.loads(response.strip())
    #             results.extend(response_json)
    #         # except json.JSONDecodeError as e:
    #         #     print(f"Error decoding JSON from chunk: {str(e)}")
    #         except json.JSONDecodeError:
    #             # Ignore the JSON decoding error
    #             continue
    # return results

# Function to extract various details from a PDF
def extract_details_from_pdf(pdf_path, llama_model):
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    if pdf_text:
        # Split text into chunks
        text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

        # List of details to extract
        details_to_extract = [
            "Appearance", "Physical State", "Odor", "Odor Threshold", "Density, g/cm3",
            "pH", "Freeze Point, °C", "Viscosity (mPa.s)", "Solubility in Water",
            "Partition Coeff., n-octanol/water", "Decomposition Temperature, °C",
            "Explosive Limits, %", "Boiling Range, °C", "Auto-Ignition Temperature, °C",
            "Minimum Flash Point, °C", "Vapor Pressure, mmHg", "Evaporation Rate",
            "Flash Method", "Vapor Density", "Flammability, NFPA", "Combustible Dust"
        ]

        # Extract each detail independently
        found_details = {}
        for detail in details_to_extract:
            detail_result = extract_specific_detail(text_chunks, detail, llama_model)
            found_details.update(detail_result)

        # Print the extracted details in JSON format
        print(json.dumps(found_details, indent=4))
    else:
        print("No text extracted from the PDF.")

pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
extract_details_from_pdf(pdf_path_dimethyl_glutarate, llama)


# {
#     "Appearance": "The Appearance is: Colored.",
#     "Physical State": "The Physical State of the product is: Thick Liquid",
#     "Odor": "The Odor of the product is: Fruity",
#     "Odor Threshold": "The Odor Threshold is: Not Established",
#     "Density, g/cm3": "Please return the density value as a plain string, without any units. If the density is not mentioned, return 'Not Established'.",
#     "pH": "The pH of the product is not explicitly mentioned in the provided SDS. Therefore, the answer is:\n\npH: Not Established",
#     "Freeze Point, \u00b0C": "Please provide the actual Freeze Point, \u00b0C value if it is mentioned in the SDS.",
#     "Viscosity (mPa.s)": "Please return the Viscosity (mPa.s) of the product.",
#     "Solubility in Water": "Please return the Solubility in Water value as a plain string, without the units. If the value is not mentioned, return 'Not Established'.",
#     "Partition Coeff., n-octanol/water": "Please return the Partition Coeff., n-octanol/water value as a plain string, without any unit or 'Not Established' mention.\n\nFor example, if the SDS contains the following information:\n\nPartition Coeff., n-octanol/water: 3.4\n\nThen, the expected result is: 3.4\n\nIf the SDS does not contain any information about the Partition Coeff., n-octanol/water, then the expected result is: Not Established",
#     "Decomposition Temperature, \u00b0C": "Please provide the actual temperature value if mentioned in the SDS.",
#     "Explosive Limits, %": "Please return the Explosive Limits, % as a plain string, without the units (%).",
#     "Boiling Range, \u00b0C": "Please provide the actual Boiling Range, \u00b0C from the SDS.",
#     "Auto-Ignition Temperature, \u00b0C": "Please provide the actual value if mentioned in the SDS.",
#     "Minimum Flash Point, \u00b0C": "Please provide the actual value of the Minimum Flash Point, \u00b0C.",
#     "Vapor Pressure, mmHg": "Please return the Vapor Pressure, mmHg value as a plain string, without the unit. If the value is not mentioned, return 'Not Established'.",
#     "Evaporation Rate": "Please note that the SDS is written following a specific format and the information provided may vary depending on the product and the manufacturer.",
#     "Flash Method": "The Flash Method for this product is:\nSeta Closed Cup",
#     "Vapor Density": "Please return the Vapor Density of the product.",
#     "Flammability, NFPA": "Please provide the actual value for the Flammability, NFPA.\n\nPlease note that the SDS is from 2019, and some values might have changed.",
#     "Combustible Dust": "Combustible Dust: Does not support combustion"
# }



