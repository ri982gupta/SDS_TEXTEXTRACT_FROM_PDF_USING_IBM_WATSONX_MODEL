#---------------------------------------------FIND EMERGENCY DETAILS FROM THE 2ND PDF ------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------



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
        )
        response = llama_model.invoke(prompt)
        if response:
            response_text = response.strip()
            if response_text:
                return {detail_name: response_text}
    return None

# Function to extract various details from a PDF
def extract_details_from_pdf(pdf_path, llama_model):
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    if pdf_text:
        # Split text into chunks
        text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

        # List of details to extract
        details_to_extract = [
            "First-aid measures", "Firefighting measures", "Accidental release measures",
            "Handling and storage", "Disposal considerations"
        ]

        # Extract each detail independently
        found_details = {}
        for detail in details_to_extract:
            detail_result = extract_specific_detail(text_chunks, detail, llama_model)
            if detail_result:
                found_details.update(detail_result)

        # Print the extracted details in JSON format
        print(json.dumps(found_details, indent=4))
    else:
        print("No text extracted from the PDF.")

pdf_path_dimethyl_glutarate = "Caulk SDS 1.pdf"
extract_details_from_pdf(pdf_path_dimethyl_glutarate, llama)


# {
#     "First-aid measures": "First-aid measures:\n\n* Inhalation: Leave the area to obtain fresh air. If continued difficulty is experienced, get medical attention immediately.\n* Skin contact: Wash skin immediately with soap and water.\n* Eye contact: Immediately flush eyes with large quantities of water for at least 15 minutes until irritation subsides. Get medical attention immediately.\n* Ingestion: If swallowed, DO NOT INDUCE VOMITING. Get medical attention immediately.",
#     "Firefighting measures": "None.",
#     "Accidental release measures": "Please provide the actual text you want me to read and I'll be happy to assist you.",
#     "Handling and storage": "Handling: Keep out of reach of children. Do not take internally. Use only with adequate ventilation. Ensure fresh air entry during application and drying. Wash thoroughly after handling.\nStorage: Avoid excessive heat and freezing. Do not store at temperatures above 120 degrees F. Store away from caustics and oxidizers.",
#     "Disposal considerations": "Disposal considerations:\n\n* Dispose of in accordance with applicable regulations.\n* Scrape up dried material and place into containers.\n* Use personal protective equipment as necessary.\n* Avoid excessive heat and freezing.\n* Store away from caustics and oxidizers.\n* Wash thoroughly after handling."
# }