#-----------------------------------EXTRACT REGULATORY INFORMATION FROM THE 2ND PDF-------------------------------------

#-----------------------------------------------------------------------------------------------------------------------


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
            "OSHA Hazard Communication Standard (HCS) classification",
            "European CLP Regulation classification",
            "Canadian WHMIS classification",
            "Australian Poisons Schedule",
            "Other regulatory classifications (e.g., TSCA, REACH)"
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
#     "OSHA Hazard Communication Standard (HCS) classification": "Please provide the OSHA Hazard Communication Standard (HCS) classification for the given SDS.",
#     "European CLP Regulation classification": "Please provide the actual text you want me to read and I'll be happy to assist you.",
#     "Canadian WHMIS classification": "Please provide the actual Canadian WHMIS classification for the given product, based on the information provided in the SDS.",
#     "Australian Poisons Schedule": "The Australian Poisons Schedule is as follows:\n\n* Dimethyl glutarate: Not listed\n* Dimethyl succinate: Not listed\n* Dimethyl adipate: Not listed\n* Diethanolamine: Not listed\n\nNote: The Australian Poisons Schedule is a list of substances that are regulated by the Australian government due to their potential to cause harm to human health or the environment. The schedule includes substances 
# that are classified as hazardous according to the Globally Harmonized System of Classification and Labeling of Chemicals (GHS). The GHS classifies substances into different categories based on their level of hazard, and the Australian Poisons Schedule includes substances that are classified as Category 1 (extremely hazardous), Category 2 (highly hazardous), or Category 3 (hazardous) according to the GHS.\n\nIn this case, none of the ingredients in the product are listed on the Australian Poisons Schedule, indicating that they are not considered hazardous according to the GHS criteria. However, it is important to note that this does not necessarily mean that the product is safe to use without proper precautions, and users should still follow the safety instructions and recommendations provided on the product label and in the SDS.",
#     "Other regulatory classifications (e.g., TSCA, REACH)": "Other regulatory classifications:\n\n* GHS Classification: Eye Irrit. 2\n* GHS Hazard Statements: H319, H332, H337, H318\n* GHS Precautionary Statements: P264, P280, P305+P351+P338, P337+P313\n* CAS-No: 1119-40-0, 106-65-0, 627-93-0, 111-42-2\n* OSHA PEL-TWA: N.E.\n* OSHA PEL-CEILING: N.E.\n* ACGIH TLV-TWA: N.E.\n* ACGIH-TLV STEL: N.E.\n* NFPA: Non-Flammable\n* Combustible Dust: Does not support combustion"
# }