#------------------------------------------------------FIND HAZARDS DETIALS FROM THE 2ND PDF-------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------


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
    for chunk in text_chunks:
        prompt = (
            f"Extract the {detail_name} from the following text and return the result as a plain string:\n\n"
            f"{chunk}\n\n"
            f"If the {detail_name} is not mentioned, return 'Not Established'."
        )
        response = llama_model.invoke(prompt)
        if response:
            response_text = response.strip()
            if response_text and response_text.lower() != 'not established':
                return {detail_name: response_text}
    return {detail_name: "Not Established"}

# Function to extract various details from a PDF
def extract_details_from_pdf(pdf_path, llama_model):
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    if pdf_text:
        # Split text into chunks
        text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

        # List of details to extract
        details_to_extract = [
            "Acute toxicity (oral, inhalation, dermal)", "Skin irritation", "Eye irritation",
            "Skin sensitization", "Respiratory sensitization", "Germ cell mutagenicity",
            "Carcinogenicity", "Reproductive toxicity", "Specific target organ toxicity (single exposure)",
            "Specific target organ toxicity (repeated exposure)", "Aspiration hazard", "Aquatic toxicity",
            "Persistence and degradability", "Bioaccumulative potential", "Mobility in soil"
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
#     "Acute toxicity (oral, inhalation, dermal)": "Please note that the SDS is from 2019, and some of the regulations and standards mentioned in the SDS may have changed since then.",
#     "Skin irritation": "Please note that the SDS provided is a lengthy document, and the relevant information may be scattered throughout the text. It's important to carefully review the document and extract the relevant information.\n\nThe Skin irritation from the provided SDS is:\n\nEye Irritation, category 2\nH319\nCauses serious eye irritation.\n\nThe Skin irritation is mentioned in the section 2. Hazards Identification, GHS Classification, and in the GHS Hazard Statements.\n\nTherefore, the result is:\n\nEye Irritation, category 2\nH319\nCauses serious eye irritation.",
#     "Eye irritation": "Please note that the SDS provided is a sample and not an actual SDS document.",
#     "Skin sensitization": "Please note that the information provided is based on the information available on the SDS and should be used as a guide only. It is the responsibility of the user to consult the SDS and follow the recommended safety precautions when handling the chemical.",
#     "Respiratory sensitization": "Please note that the SDS provided is a lengthy document, and the relevant information may be scattered throughout the text. Therefore, it is essential to carefully review the entire SDS to ensure that all necessary information is extracted.\n\nIn this case, the Respiratory sensitization is not explicitly mentioned in the provided SDS. Therefore, the answer would be:\n\nNot Established",
#     "Germ cell mutagenicity": "Please note that the Germ cell mutagenicity is not necessarily a direct indicator of the product's carcinogenicity.",
#     "Carcinogenicity": "Please note that the text contains several tables and sections, but the relevant information for the task is contained in the first section, labeled 'Carcinogenicity'.",
#     "Reproductive toxicity": "Please note that the text contains several mentions of the phrase \"No Information\" or \"N.I.\", which indicates that there is no information available regarding certain topics.\n\nIn this case, the Reproductive toxicity is mentioned as follows:\n\n\"Dimethyladipate may increase the incidence of abnormal embryo development, based on a single suboptimally analyzed rat study. There are no human data.\"\n\nTherefore, the Reproductive toxicity is established, and the result is:\n\n\"May increase the incidence of abnormal embryo development\"",
#     "Specific target organ toxicity (single exposure)": "Please note that the information provided is based on the given SDS and might not be a comprehensive representation of the substance's properties.",
#     "Specific target organ toxicity (repeated exposure)": "Please note that the information provided is based on the given text and might not be accurate or complete.\n\nAlso, note that the answer provided is based on the given text and might not be accurate or complete.",
#     "Aspiration hazard": "Please note that the SDS provided is a lengthy document, and the relevant information may be scattered throughout the text. Therefore, it is essential to carefully review the entire SDS to ensure that all necessary information is extracted.\n\nIn this case, the Aspiration hazard is not explicitly mentioned in the provided SDS. Therefore, the answer would be 'Not Established'.",
#     "Aquatic toxicity": "Please note that the text provided is a Safety Data Sheet (SDS) for a chemical product, and it contains information about the product's properties, hazards, and safety precautions. The SDS is 
# intended to provide workers, emergency responders, and others with information on the hazards of the chemical product and how to safely handle, use, store, and dispose of it.\n\nThe SDS includes information on the product's physical and chemical properties, hazards, exposure controls, and emergency procedures. It also includes information on the product's regulatory status, including its classification under various regulations and its compliance with safety standards.\n\nThe SDS is typically prepared by the manufacturer or supplier of the chemical product and is intended to be a summary of the most important safety information about the product. It is usually provided to customers who purchase the product, and it is also made available to emergency responders and other personnel who may be exposed to the product in the course of their work.",
#     "Persistence and degradability": "Please provide the actual Persistence and degradability of the product, if possible.",
#     "Bioaccumulative potential": "Please note that the SDS provided is a lengthy document, and the relevant information may be scattered throughout the text. Therefore, it is essential to carefully review the entire SDS to ensure that all necessary information is extracted.\n\nIn this case, the SDS does not explicitly mention the Bioaccumulative potential. Therefore, the answer is:\n\nNot Established",
#     "Mobility in soil": "Please note that the information provided in the SDS is based on the knowledge available to the manufacturer at the time of preparation and may not be exhaustive. It is the responsibility of the user to consult the relevant regulations and expert advice before handling the chemical."
# }