#---------------------------------------EXTRACT THE MISCELLANOUS INFO FROM THE 2ND PDF ----------------------------------

#------------------------------------------------------------------------------------------------------------------------


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
            "Chemical structure", "Synonyms", "Trade names", "Uses",
            "Manufacturers and suppliers", "Exposure limits", 
            "Medical surveillance recommendations", "SDS authoring date and revision date",
            "OSHA Hazard Communication Standard", "European CLP Regulation",
            "Canadian WHMIS", "Australian Poisons Schedule",
            "Global Harmonized System of Classification and Labeling of Chemicals (GHS)"
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
#     "Chemical structure": "Dimethyl glutarate\nDimethyl succinate\nDimethyl adipate\nDiethanolamine",
#     "Synonyms": "12. Ecological Information\nECOLOGICAL INFORMATION: Not available.\n\n13. Disposal Considerations\nDISPOSAL METHODS: Dispose of in accordance with applicable regulations.  Dispose of in a sealed container.\nSPECIFIC TREATMENT: Not available.\n14. Transport Information\nTRANSPORTATION NAME: Caulk Be Gone\nUN Number:\n1993\nPacking Group:\nIII\nHazard Class:\n3\nHazard Category:\n2\nSpecial Provisions:\nNone\n15. Regulatory Information\nOSHA HAZARD COMMUNICATION STANDARD (29 CFR 1910.1200):\nThis product is covered by the OSHA Hazard Communication Standard.\n\n16. Other Information\nABBREVIATIONS USED IN THIS SDS:\nGHS: Globally Harmonized System of Classification and Labeling of Chemicals\nACGIH: American Conference of Governmental Industrial Hygienists\nOSHA: Occupational Safety and Health Administration\nNIOSH: National Institute for Occupational Safety and Health\nTLV-TWA: Threshold Limit Value - Time Weighted Average\nSTEL: Short Term Exposure Limit\nPEL-TWA: Permissible Exposure Limit - Time Weighted Average\nPEL-CEILING: Permissible Exposure Limit - Ceiling\nOES: Occupational Exposure Standard\nMEL: Maximum Exposure Limit\nSUP: Supplier's Recommendation\nSk: Skin Sensitizer\nN.E.: Not Established\n\nNote:",
#     "Trade names": "Diethanolamine\nDimethyl glutarate\nDimethyl succinate\nDimethyl adipate",
#     "Uses": "The information provided in this SDS is based on data available to the manufacturer and is believed to be accurate as of the date of preparation. However, the manufacturer makes no representation or warranty, expressed or implied, as to the completeness or accuracy of the information and disclaims any liability for loss or damage resulting from the use of this information. The manufacturer reserves the right to revise this SDS at any time without notice.\n\nThe information in this SDS is intended for use by individuals who have been trained in accordance with OSHA's Hazardous Waste Operations and Emergency Response (HAZWOPER) standard (29 CFR 1910.120) and who have experience in handling hazardous chemicals. It is not intended for use by untrained individuals.\n\nThe manufacturer is not responsible for the content of any other SDSs that may be provided by other manufacturers or suppliers of the same or similar products.\n\nThe manufacturer's liability for any loss or damage resulting from the use of this product is limited to the purchase price of the product.\n\nThe manufacturer does not warrant that the product is fit for any particular purpose, and the user assumes all risks associated with its use.\n\nThe manufacturer is not responsible for any loss or damage resulting from the use of this product in a manner that is not in accordance with the instructions and precautions set forth in this SDS or on the product label.\n\nThe manufacturer is not responsible for any loss or damag extract, and I'll be happy to help.",
#     "European CLP Regulation": "Please provide the actual text you want to read and I'll be happy to assist you.",
#     "Canadian WHMIS": "Please provide the actual WHMIS information you want extracted and I will be happy to help.",
#     "Australian Poisons Schedule": "The Australian Poisons Schedule is as follows:\n\n* Dimethyl glutarate: Not listed\n* Dimethyl succinate: Not listed\n* Dimethyl adipate: Not listed\n* Diethanolamine: Not listed\n\nNote: The Australian Poisons Schedule is a list of substances that are regulated by the Australian government due to their potential to cause harm to human health or the environment. The schedule includes substances 
# that are classified as hazardous according to the Globally Harmonized System of Classification and Labeling of Chemicals (GHS). The GHS classifies substances into different categories based on their level of hazard, and the Australian Poisons Schedule includes substances that are classified as Category 1 (extremely hazardous), Category 2 (highly hazardous), or Category 3 (hazardous) according to the GHS.\n\nIn this case, none of the ingredients in the product are listed on the Australian Poisons Schedule, indicating that they are not considered hazardous according to the GHS criteria. However, it is important to note that this does not necessarily mean that the product is safe to use without proper precautions, and users should still follow the safety instructions and recommendations provided on the product label and in the SDS.",
#     "Global Harmonized System of Classification and Labeling of Chemicals (GHS)": "Please provide the actual text you want me to read and I'll be happy to assist you."
# }