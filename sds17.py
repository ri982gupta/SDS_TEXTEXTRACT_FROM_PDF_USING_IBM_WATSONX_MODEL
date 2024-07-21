#------------------------------------------ FIND CHEMICAL INFO FROM PDF-----------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------


# import fitz  # PyMuPDF
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Credentials for authentication
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# try:
#     project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"
# except KeyError:
#     project_id = input("Please enter your project_id (hit enter): ")

# # Create LLM model
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')

# # Directory to persist embeddings
# persist_directory = "C:/Users/RiGupta/Desktop/22_may/persist_directory"

# # Create a Chroma vector store retriever
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to extract information from text using LLM model
# def extract_info_from_text_usellm(llm_model, text):
#     try:
#         # Prepare the prompt to extract names and emails
#         prompt = (
#             "Extract names and emails from the following text:\n\n"
#             f"{text}\n\n"
#             "Names and Emails:"
#         )
#         # Generate information using LLM
#         extracted_info = llm_model.invoke(prompt)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# # Path to the PDF file
# pdf_path = "samplee.pdf"

# # Extract text from the PDF
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

# pdf_text = extract_text_from_pdf(pdf_path)

# # Use the Watson model to extract information from the text
# extracted_info = extract_info_from_text_usellm(llama, pdf_text)

# # Prepare the output in JSON format
# output_json = {
#     "Extracted_Info": extracted_info
# }

# # Print the output in JSON format
# print(json.dumps(output_json, indent=4))


# #i am getting the output


#-----------------------------------------------------------------------------------------------------

# import fitz  # PyMuPDF
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Credentials for authentication
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# try:
#     project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"
# except KeyError:
#     project_id = input("Please enter your project_id (hit enter): ")

# # Create LLM model
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')

# # Directory to persist embeddings
# persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"

# # Create a Chroma vector store retriever
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to extract information from text using LLM model
# def extract_info_from_text_usellm(llm_model, text):
#     try:
#         # Prepare the prompt to extract names and emails
#         prompt = (
#             "Extract names and emails from the following text:\n\n"
#             f"{text}\n\n"
#             "Names and Emails:"
#         )
#         # Generate information using LLM
#         extracted_info = llm_model.invoke(prompt)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# # Path to the PDF file
# pdf_path = "samplee.pdf"

# # Extract text from the PDF
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

# pdf_text = extract_text_from_pdf(pdf_path)

# # Use the Watson model to extract information from the text
# extracted_info = extract_info_from_text_usellm(llama, pdf_text)

# # Prepare the output in a structured JSON format
# def format_extracted_info(extracted_info):
#     lines = extracted_info.strip().split("\n")
#     names_emails = []
#     for line in lines:
#         if '-' in line:
#             name, email = line.split(" - ")
#             names_emails.append({"Name": name.strip(), "Email": email.strip()})
#     return names_emails

# formatted_info = format_extracted_info(extracted_info)

# # Prepare the final output in JSON format
# output_json = {
#     "Extracted_Info": formatted_info
# }

# # Print the output in JSON format
# print(json.dumps(output_json, indent=4))

# # remove the extra function format_extracted_info directly get output as structure data from pdf using llm


#----------------------------------------------------------------------------------------------------------------------------------


# import fitz  # PyMuPDF
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Credentials for authentication
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# try:
#     project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"
# except KeyError:
#     project_id = input("Please enter your project_id (hit enter): ")

# # Create LLM model
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')

# # Directory to persist embeddings
# persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"

# # Create a Chroma vector store retriever
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to extract information from text using LLM model
# def extract_info_from_text_usellm(llm_model, text):
#     try:
#         # Prepare the prompt to extract names and emails in JSON format
#         prompt = (
#             "Extract names and emails from the following text and return the result in JSON format:\n\n"
#             f"{text}\n\n"
#             "Return the result as a JSON array of objects with 'Name' and 'Email' fields:"
#         )
#         # Generate information using LLM
#         extracted_info = llm_model.invoke(prompt)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# # Path to the PDF file
# pdf_path = "samplee.pdf"

# # Extract text from the PDF
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

# pdf_text = extract_text_from_pdf(pdf_path)

# # Use the Watson model to extract information from the text
# extracted_info = extract_info_from_text_usellm(llama, pdf_text)

# # Since the extracted_info should already be in JSON format, we can directly print it
# try:
#     output_json = json.loads(extracted_info)
# except json.JSONDecodeError as e:
#     print(f"Error decoding JSON: {str(e)}")
#     output_json = {"Extracted_Info": None}

# # Print the output in JSON format
# print(json.dumps(output_json, indent=4))


# # remove the commented line

#----------------------------------------------------------------------------------------------------------------




# import fitz 
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes


# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# try:
#     project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"
# except KeyError:
#     project_id = input("Please enter your project_id (hit enter): ")


# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')


# persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"


# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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


# def extract_info_from_text_usellm(llm_model, text):
#     try:
        
#         prompt = (
#             "Extract names and emails from the following text and return the result in JSON format:\n\n"
#             f"{text}\n\n"
#             "Return the result as a JSON array of objects with 'Name' and 'Email' fields:"
#         )
       
#         extracted_info = llm_model.invoke(prompt)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None


# pdf_path = "sampleee.pdf"


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

# pdf_text = extract_text_from_pdf(pdf_path)


# extracted_info = extract_info_from_text_usellm(llama, pdf_text)


# try:
#     output_json = json.loads(extracted_info)
# except json.JSONDecodeError as e:
#     print(f"Error decoding JSON: {str(e)}")
#     output_json = {"Extracted_Info": None}


# print(json.dumps(output_json, indent=4))


# ---------------------------------------------------------------- WTHOUT PDF --------------------------------------------------------------------------

# import fitz
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/3_june/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# def extract_info_from_text_usellm(llm_model, text, prompt):
#     try:
#         extracted_info = llm_model.invoke(prompt + text)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# def search_chemical_in_text(chemical_names, text):
#     found_chemicals = []
#     for name in chemical_names:
#         if name in text:
#             found_chemicals.append(name)
#     return found_chemicals

# # Paths to the PDFs
# pdf_path_1 = "Caulk SDS 1.pdf"
# pdf_path_2 = "GHS Rev10e.pdf"

# # Extract text from both PDFs
# text_1 = extract_text_from_pdf(pdf_path_1)
# text_2 = extract_text_from_pdf(pdf_path_2)

# # Extract chemical names from the first PDF
# chemical_names_prompt = "Extract chemical names from the following text and return the result as a JSON array:\n\n"
# extracted_chemicals_info = extract_info_from_text_usellm(llama, text_1, chemical_names_prompt)

# # Parse the extracted chemical names
# try:
#     chemical_names = json.loads(extracted_chemicals_info)
# except json.JSONDecodeError as e:
#     print(f"Error decoding JSON: {str(e)}")
#     chemical_names = []

# # Search for the extracted chemical names in the second PDF
# found_chemicals = search_chemical_in_text(chemical_names, text_2)

# # Prepare the final output in JSON format
# output_json = {
#     "Extracted_Chemicals": chemical_names,
#     "Found_Chemicals": found_chemicals
# }

# # Print the output in JSON format
# print(json.dumps(output_json, indent=4))




#------------------------------------------------------------WITH PDF-------------------------------------------------------------------------------



# import fitz
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/3_june/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# def extract_info_from_text_usellm(llm_model, text, prompt):
#     try:
#         extracted_info = llm_model.invoke(prompt + text)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# def search_chemical_in_text(chemical_names, text):
#     found_chemicals = []
#     for name in chemical_names:
#         if name in text:
#             found_chemicals.append(name)
#     return found_chemicals

# # Paths to the PDFs
# pdf_path_1 = "Caulk SDS 1.pdf"
# pdf_path_2 = "GHS Rev10e.pdf"

# # Extract text from both PDFs
# text_1 = extract_text_from_pdf(pdf_path_1)
# text_2 = extract_text_from_pdf(pdf_path_2)

# # Extract chemical names from the first PDF
# chemical_names_prompt = "Extract chemical names from the following text and return the result as a JSON array:\n\n"
# extracted_chemicals_info = extract_info_from_text_usellm(llama, text_1, chemical_names_prompt)

# # Parse the extracted chemical names
# try:
#     chemical_names = json.loads(extracted_chemicals_info)
# except json.JSONDecodeError as e:
#     print(f"Error decoding JSON: {str(e)}")
#     chemical_names = []

# # Search for the extracted chemical names in the second PDF
# details_prompt_template = "Extract detailed information for the chemical name '{}' from the following text and return the result as a JSON object:\n\n"

# found_chemical_details = []
# for chemical in chemical_names:
#     prompt = details_prompt_template.format(chemical)
#     chemical_details_info = extract_info_from_text_usellm(llama, text_2, prompt)
#     try:
#         chemical_details = json.loads(chemical_details_info)
#         found_chemical_details.append({chemical: chemical_details})
#     except json.JSONDecodeError as e:
#         print(f"Error decoding JSON for chemical '{chemical}': {str(e)}")
#         found_chemical_details.append({chemical: None})

# # Prepare the final output in JSON format
# output_json = {
#     "Extracted_Chemicals": chemical_names,
#     "Found_Chemical_Details": found_chemical_details
# }

# # Print the output in JSON format
# print(json.dumps(output_json, indent=4))




#------------------------------------------------change use case--------------------------------------------------------------



# import fitz
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Define credentials and configurations
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to extract information from text using LLM model
# def extract_info_from_text_usellm(llm_model, text, prompt):
#     try:
#         full_prompt = prompt + text
#         extracted_info = llm_model.invoke(full_prompt)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# # Function to search for chemical names in a text
# def search_chemical_in_text(chemical_names, text):
#     found_chemicals = []
#     for name in chemical_names:
#         if name in text:
#             found_chemicals.append(name)
#     return found_chemicals

# # Paths to the PDFs
# pdf_path_1 = "Caulk SDS 1.pdf"
# pdf_path_2 = "GHS Rev10e.pdf"

# # Extract text from both PDFs
# text_1 = extract_text_from_pdf(pdf_path_1)
# text_2 = extract_text_from_pdf(pdf_path_2)

# # Extract chemical names from the first PDF
# chemical_names_prompt = "Extract chemical names from the following text and return the result as a JSON array:\n\n"
# extracted_chemicals_info = extract_info_from_text_usellm(llama, text_1, chemical_names_prompt)

# # Parse the extracted chemical names
# try:
#     chemical_names = json.loads(extracted_chemicals_info)
# except json.JSONDecodeError as e:
#     print(f"Error decoding JSON: {str(e)}")
#     chemical_names = []

# # Search for the extracted chemical names in the second PDF
# found_chemical_details = {}
# for chemical in chemical_names:
#     if chemical in text_2:
#         start_idx = text_2.find(chemical)
#         end_idx = start_idx + 500  # Assume we extract 500 characters after the chemical name for context
#         found_chemical_details[chemical] = text_2[start_idx:end_idx]

# # Prepare the final output in JSON format
# output_json = {
#     "Extracted_Chemicals": chemical_names,
#     "Found_Chemical_Details": found_chemical_details
# }

# # Print the output in JSON format
# print(json.dumps(output_json, indent=4))


#-------------------------------------------upload only one file---------------------------------------------------

# import fitz 
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# # Project ID for IBM Watson Machine Learning
# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# # Initialize HuggingFace Embeddings and VectorDB Chroma
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# # Define parameters for LLM model
# parameters = {
#     "decoding_method": "greedy",
#     "max_new_tokens": 400,
#     "temperature": 0.2,
#     "stop_sequences": ["conclusion"]
# }

# # Model ID for WatsonxLLM
# model_id = ModelTypes.LLAMA_2_70B_CHAT

# # Initialize WatsonxLLM
# llama = WatsonxLLM(
#     model_id=model_id.value,
#     url=credentials.get("url"),
#     apikey=credentials.get("apikey"),
#     project_id=project_id,
#     params=parameters
# )

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

# def extract_info_from_text_usellm(llm_model, text):
#     try:
#         prompt = (
#             "Extract chemical names and their details from the following text and return the result in JSON format:\n\n"
#             f"{text}\n\n"
#             "Return the result as a JSON array of objects with 'ChemicalName' and 'Details' fields:"
#         )
#         extracted_info = llm_model.invoke(prompt)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# # Path to the GHS PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Split the input text into chunks of 400 tokens
#     chunk_size = 400
#     chunks = [pdf_text[i:i+chunk_size] for i in range(0, len(pdf_text), chunk_size)]

#     extracted_info_list = []
#     for chunk in chunks:
#         # Use VectorDB to search for chemical names (using 'similarity' search type)
#         chemical_names = docsearch.search(chunk, search_type='similarity')

#         # Extract chemical details using LLM
#         extracted_info = extract_info_from_text_usellm(llama, chunk)

#         extracted_info_list.append(extracted_info)

#     # Combine the extracted information from all chunks
#     combined_info = ''.join(extracted_info_list)

#     # Parse the extracted chemical details
#     try:
#         output_json = json.loads(combined_info)
#     except json.JSONDecodeError as e:
#         print(f"Error decoding JSON: {str(e)}")
#         output_json = {"Extracted_Chemicals": None}

#     # Print the output in JSON format
#     print(json.dumps(output_json, indent=4))
# else:
#     print("No text extracted from the PDF.")


#-------------------------------------------------4 june---------------------------------------------


# import fitz
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Define credentials and configurations
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# # Initialize embeddings and VectorDB Chroma
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to extract information from text using LLM model
# def extract_info_from_text_usellm(llm_model, text, prompt):
#     try:
#         full_prompt = prompt + text
#         extracted_info = llm_model.invoke(full_prompt)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Prompt to extract chemical names and details
#     chemical_names_prompt = "Extract chemical names and their details from the following text and return the result as a JSON array of objects with 'ChemicalName' and 'Details' fields:\n\n"
    
#     # Extract information using LLM model
#     extracted_chemicals_info = extract_info_from_text_usellm(llama, pdf_text, chemical_names_prompt)
    
#     # Parse the extracted information
#     try:
#         output_json = json.loads(extracted_chemicals_info)
#     except json.JSONDecodeError as e:
#         print(f"Error decoding JSON: {str(e)}")
#         output_json = {"Extracted_Chemicals": None}
    
#     # Print the output in JSON format
#     print(json.dumps(output_json, indent=4))
# else:
#     print("No text extracted from the PDF.")







#---------------------------------------------------------------------------------------------------------------------

# import fitz
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Define credentials and configurations
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# # Initialize embeddings and VectorDB Chroma
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to split text into chunks
# def split_text_into_chunks(text, chunk_size=4096):
#     return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# # Function to extract information from text using LLM model
# def extract_info_from_text_usellm(llm_model, text, prompt):
#     try:
#         full_prompt = prompt + text
#         extracted_info = llm_model.invoke(full_prompt)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Split the extracted text into manageable chunks
#     chunks = split_text_into_chunks(pdf_text)

#     # Initialize the result list
#     aggregated_results = []

#     # Define the prompt for extracting chemical names and details
#     chemical_names_prompt = "Extract chemical names and their details from the following text and return the result as a JSON array of objects with 'ChemicalName' and 'Details' fields:\n\n"

#     # Process each chunk using the LLM model
#     for chunk in chunks:
#         extracted_chemicals_info = extract_info_from_text_usellm(llama, chunk, chemical_names_prompt)
#         if extracted_chemicals_info:
#             try:
#                 chunk_results = json.loads(extracted_chemicals_info)
#                 aggregated_results.extend(chunk_results)
#             except json.JSONDecodeError as e:
#                 print(f"Error decoding JSON: {str(e)}")
    
#     # Remove duplicates from aggregated results
#     unique_results = {item['ChemicalName']: item for item in aggregated_results}.values()

#     # Print the aggregated results in JSON format
#     print(json.dumps(list(unique_results), indent=4))
# else:
#     print("No text extracted from the PDF.")




# Error decoding JSON: Expecting value: line 3 column 1 (char 2)
# Error decoding JSON: Expecting value: line 1 column 1 (char 0)
# Error decoding JSON: Expecting value: line 1 column 2 (char 1)
# Error decoding JSON: Expecting value: line 201 column 1 (char 400)
# Error decoding JSON: Expecting value: line 1 column 1 (char 0)


#--------------------------------------------------------------------------------------------------------------------------

# import fitz
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Define credentials and configurations
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# # Initialize embeddings and VectorDB Chroma
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to split text into chunks
# def split_text_into_chunks(text, chunk_size=4096):
#     return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# # Function to extract information from text using LLM model
# def extract_info_from_text_usellm(llm_model, text, prompt):
#     try:
#         full_prompt = prompt + text
#         extracted_info = llm_model.invoke(full_prompt)
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during text extraction: {str(e)}")
#         return None

# # Function to validate and parse JSON
# def validate_and_parse_json(json_string):
#     try:
#         parsed_json = json.loads(json_string)
#         return parsed_json
#     except json.JSONDecodeError as e:
#         print(f"Error decoding JSON: {str(e)}")
#         return None

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Split the extracted text into manageable chunks
#     chunks = split_text_into_chunks(pdf_text)

#     # Initialize the result list
#     aggregated_results = []

#     # Define the prompt for extracting chemical names and details
#     chemical_names_prompt = "Extract chemical names and their details from the following text and return the result as a JSON array of objects with 'ChemicalName' and 'Details' fields:\n\n"

#     # Process each chunk using the LLM model
#     for chunk in chunks:
#         extracted_chemicals_info = extract_info_from_text_usellm(llama, chunk, chemical_names_prompt)
#         if extracted_chemicals_info:
#             chunk_results = validate_and_parse_json(extracted_chemicals_info)
#             if chunk_results:
#                 aggregated_results.extend(chunk_results)
    
#     # Remove duplicates from aggregated results
#     unique_results = {item['ChemicalName']: item for item in aggregated_results}.values()

#     # Print the aggregated results in JSON format
#     print(json.dumps(list(unique_results), indent=4))
# else:
#     print("No text extracted from the PDF.")


# Error decoding JSON: Expecting value: line 3 column 1 (char 2)
# Error decoding JSON: Expecting value: line 1 column 1 (char 0)
# Error decoding JSON: Expecting value: line 1 column 2 (char 1)
# Error decoding JSON: Expecting value: line 201 column 1 (char 400)
# Error decoding JSON: Expecting value: line 1 column 1 (char 0)
# Error decoding JSON: Expecting value: line 1 column 1 (char 0)
# Error decoding JSON: Expecting value: line 1 column 2 (char 1)
# Error decoding JSON: Expecting value: line 3 column 1 (char 2)
# Error decoding JSON: Expecting value: line 1 column 1 (char 0)
# Error decoding JSON: Expecting value: line 3 column 1 (char 2)




#-------------------------------------------------------------------------------------------------------------------------


#phind

# import fitz
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Define credentials and configurations
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# # Initialize embeddings and VectorDB Chroma
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/3_june/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to process text through LLM model and extract chemical names
# def extract_chemical_names_from_llm(text, chemical_id):
#     # Placeholder for sending text to the LLM model and receiving a response
#     # Replace this with the actual method provided by the WatsonxLLM class
#     response = llama.send_text_to_model(text)  # Hypothetical method
    
#     # Assuming the LLM model returns a dictionary with 'chemical_names' key
#     # Replace this with the actual structure of the response
#     chemical_names = response.get('chemical_names', [])
    
#     # Filter chemical names based on the chemical identifier
#     filtered_names = [name for name in chemical_names if chemical_id in name]
    
#     return filtered_names

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"
# chemical_id = "H331"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Extract chemical names for the specified chemical identifier
#     chemical_names = extract_chemical_names_from_llm(pdf_text, chemical_id)

#     # Print the extracted chemical names
#     if chemical_names:
#         print(json.dumps({"ChemicalNames": chemical_names}, indent=4))
#     else:
#         print(f"No chemical names found for chemical identifier {chemical_id}.")
# else:
#     print("No text extracted from the PDF.")


#hypothetical method


# Error decoding JSON: Expecting value: line 1 column 2 (char 1)
# Error decoding JSON: Expecting value: line 3 column 1 (char 2)
# Error decoding JSON: Expecting value: line 1 column 1 (char 0)
# Error decoding JSON: Expecting value: line 3 column 1 (char 2)



#-----------------------------------------------------------5 June 2024----------------------------------------------------------------



# import fitz
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Define credentials and configurations
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# # Initialize embeddings and VectorDB Chroma
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/3_june/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to divide text into smaller chunks
# def chunk_text(text, max_length=3500):
#     words = text.split()
#     chunks = []
#     current_chunk = []

#     for word in words:
#         if len(current_chunk) + len(word.split()) <= max_length:
#             current_chunk.append(word)
#         else:
#             chunks.append(" ".join(current_chunk))
#             current_chunk = [word]
    
#     if current_chunk:
#         chunks.append(" ".join(current_chunk))
    
#     return chunks

# # Function to process text through LLM model and extract chemical information
# def extract_chemical_info_from_llm(text, chemical_id):
#     chunks = chunk_text(text)
#     chemical_info = []

#     for chunk in chunks:
#         prompt = f"Extract information related to chemical identifier '{chemical_id}' from the following text and return it in JSON format:\n\n{chunk}"
#         try:
#             response = llama.generate(prompt)
#             chemical_info.append(response['text'])  # Adjust this line based on actual response structure
#         except Exception as e:
#             print(f"Error occurred during LLM extraction: {str(e)}")
    
#     return chemical_info

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"
# chemical_id = "H331"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Extract chemical information for the specified chemical identifier
#     chemical_info = extract_chemical_info_from_llm(pdf_text, chemical_id)

#     # Print the extracted chemical information in JSON format
#     if chemical_info:
#         print(json.dumps({"ChemicalInfo": chemical_info}, indent=4))
#     else:
#         print(f"No information found for chemical identifier {chemical_id}.")
# else:
#     print("No text extracted from the PDF.")



# Error occurred during LLM extraction: Argument 'prompts' is expected to be of type List[str], received argument of type <class 'str'>.
# Error occurred during LLM extraction: Argument 'prompts' is expected to be of type List[str], received argument of type <class 'str'>.
# Error occurred during LLM extraction: Argument 'prompts' is expected to be of type List[str], received argument of type <class 'str'>.
# Error occurred during LLM extraction: Argument 'prompts' is expected to be of type List[str], received argument of type <class 'str'>.
# Error occurred during LLM extraction: Argument 'prompts' is expected to be of type List[str], received argument of type <class 'str'>.
# Error occurred during LLM extraction: Argument 'prompts' is expected to be of type List[str], received argument of type <class 'str'>.
# Error occurred during LLM extraction: Argument 'prompts' is expected to be of type List[str], received argument of type <class 'str'>.
# Error occurred during LLM extraction: Argument 'prompts' is expected to be of type List[str], received argument of type <class 'str'>.
# No information found for chemical identifier H331.



#-----------------------------------------------------------------------------------------------------------------------------

# import fitz
# import json
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Initialize embeddings and VectorDB Chroma
# embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
# persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"
# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# # Function to extract information for a specific chemical identifier using VectorDB
# def extract_chemical_info_from_vectordb(text, chemical_id):
#     chemical_info = []
#     search_results = docsearch.search(text, search_type='similarity')  # Using VectorDB to search for chemical terms
    
#     for result in search_results:
#         if chemical_id in result['text']:
#             context = result['context']
#             chemical_info.append(context)
    
#     return chemical_info

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"
# chemical_id = "H331"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Extract chemical information for the specified chemical identifier
#     chemical_info = extract_chemical_info_from_vectordb(pdf_text, chemical_id)

#     # Print the extracted chemical information in JSON format
#     if chemical_info:
#         print(json.dumps({"ChemicalInfo": chemical_info}, indent=4))
#     else:
#         print(f"No information found for chemical identifier {chemical_id}.")
# else:
#     print("No text extracted from the PDF.")


# No information found for chemical identifier H331.



#-------------------------------------------------------------------------------------------------------------------------------


import fitz
import json
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ibm import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# Define credentials and configurations
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
}

project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

# Initialize embeddings and VectorDB Chroma
embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
persist_directory = "C:/Users/RiGupta/Desktop/3_june/persist_directory"
docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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

# Function to extract information for a specific chemical identifier
def extract_chemical_info(text, chemical_id):
    chemical_info = []
    # Split text into lines and search for the chemical identifier
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if chemical_id in line:
            # Collect surrounding lines for context (e.g., 5 lines before and after)
            start_idx = max(0, i - 5)
            end_idx = min(len(lines), i + 5)
            chemical_info.append("\n".join(lines[start_idx:end_idx]))
    return chemical_info

# Path to the PDF file
pdf_path = "GHS Rev10e.pdf"
chemical_id = "H331"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

if pdf_text:
    # Extract information for the specified chemical identifier
    chemical_info = extract_chemical_info(pdf_text, chemical_id)

    # Print the extracted information in JSON format
    if chemical_info:
        print(json.dumps({"ChemicalInfo": chemical_info}, indent=4))
    else:
        print(f"No information found for chemical identifier {chemical_id}.")
else:
    print("No text extracted from the PDF.")


# {
#     "ChemicalInfo": [
#         "Toxic in contact with \nskin \nH311 \nInhalation \nToxic if inhaled \nH331 \n4 \nOral \nNot \napplicable ",
#         "(chapter 3.3) \n2B \nH330 Fatal if inhaled \nAcute toxicity, inhalation (chapter 3.1) \n1, 2 \nH331 Toxic if inhaled \nAcute toxicity, inhalation (chapter 3.1) \n3 \nH332 Harmful if inhaled \nAcute toxicity, inhalation (chapter 
# 3.1) ",
#         "Acute toxicity, oral (chapter 3.1) and \nacute toxicity, dermal (chapter 3.1) \n3 \nH301 \n+ \nH331 \nToxic if swallowed or if inhaled \nAcute toxicity, oral (chapter 3.1) and \nacute toxicity, inhalation (chapter 3.1) \n3 ",   
#         "Acute toxicity, oral (chapter 3.1) and \nacute toxicity, inhalation (chapter 3.1) \n3 \nH311 \n+ \nH331 \nToxic in contact with skin or if inhaled \nAcute toxicity, dermal (chapter 3.1) and \nacute toxicity, inhalation \n(chapter 3.1) ",
#         "3 \nH301 \n+ \nH311 \n+ \nH331 \nToxic if swallowed, in contact with skin or if \ninhaled \nAcute toxicity, oral (chapter 3.1), acute \ntoxicity, dermal (chapter 3.1) and acute ",
#         "Symbol \nSignal word \nHazard statement \nSkull and crossbones \nDanger \nH331 \nToxic if inhaled \nPrecautionary statements \nPrevention \nResponse "
#     ]
# }


