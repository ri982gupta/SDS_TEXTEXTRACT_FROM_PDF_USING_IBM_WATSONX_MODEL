#--------------------------------FIND TRANSPORT DETAILS FROM THE 2ND PDF-------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------


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
            "UN number", "Proper shipping name", "Transport hazard class",
            "Packing group", "Environmental hazards"
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
#     "UN number": "12. Ecological Information\nECOLOGICAL INFORMATION: Not available.\n13. Disposal Considerations\nDISPOSAL METHODS: Dispose of in accordance with applicable regulations.  Dispose of in a sealed container.\n14. Transport Information\nUN Number:\n1495\nUN Proper Shipping Name:\nCaulk Remover\nTransport Hazard Class:\n3\nPacking Group:\nIII\n15. Regulatory Information\nOSHA HAZARD COMMUNICATION STANDARD (29 CFR 1910.1200)\nThis product is covered by the OSHA Hazard Communication Standard.  This document has been prepared in accordance with \nrequirements of this standard.\n\n16. Other Information\nABBREVIATIONS USED IN THIS SDS:\nGHS: Globally Harmonized System of Classification and Labeling of Chemicals\nOSHA: Occupational Safety and Health Administration\nACGIH: American Conference of Governmental Industrial Hygienists\nTLV-TWA: Threshold Limit Value - Time Weighted Average\nSTEL: Short Term Exposure Limit\nPEL-TWA: Permissible Exposure Limit - Time Weighted Average\nPEL-CEILING: Permissible Exposure Limit - Ceiling\nNIOSH: National Institute for Occupational Safety and Health\nCAS-No.: Chemical Abstracts Service Number\n\n17. Revision History\nRevision Date:\n3/5/2019\nRevision Number:\n1\n\n18. Responsible Party\nDAP Products Inc.\n2400 Boston Street Suite 2",    
#     "Proper shipping name": "Please provide the actual shipping name you'd like to extract, and I'll be happy to help!",
#     "Transport hazard class": "Please enter the transport hazard class as a plain string, without any additional information or formatting.",
#     "Packing group": "Please enter the packing group from the text:",
#     "Environmental hazards": "Please provide the actual environmental hazards you want to extract, and I will be happy to help you."
# }