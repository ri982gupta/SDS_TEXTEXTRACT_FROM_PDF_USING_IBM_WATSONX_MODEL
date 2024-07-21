#----------------------------------------ALL GENERAL INFORMATION FROM THE PDF---------------------------------------------------

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
            "Chemical name", "CAS number", "EINECS number", "RTECS number",
            "Molecular formula", "Molecular weight", "Physical state (solid, liquid, gas)",
            "Appearance", "Odor", "pH", "Melting point", "Boiling point", "Flash point",
            "Density", "Solubility in water", "Solubility in other solvents", "Vapor pressure",
            "Autoignition temperature", "Decomposition temperature"
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
#     "Chemical name": "Please provide the actual chemical name you'd like to extract, and I'll be happy to help.",
#     "CAS number": "12. Ecological Information\nECOLOGICAL INFORMATION: Not available.\n13. Disposal Considerations\nDISPOSAL METHODS: Dispose of in accordance with applicable regulations.  Dispose of in a sealed container.\n14. Transport Information\nTRANSPORTATION: Not regulated for transport.\n15. Regulatory Information\nOSHA HAZARD COMMUNICATION STANDARD (29 CFR 1910.1200):\nThis product is covered by the OSHA Hazard Communication Standard.\n\n16. Other Information\nABBREVIATIONS USED IN THIS SDS:\nGHS: Globally Harmonized System of Classification and Labeling of Chemicals\nACGIH: American Conference of Governmental Industrial Hygienists\nOSHA: Occupational Safety and Health Administration\nTLV-TWA: Threshold Limit Value - Time Weighted Average\nSTEL: Short Term Exposure Limit\nPEL-TWA: Permissible Exposure Limit - Time Weighted Average\nPEL-CEILING: Permissible Exposure Limit - Ceiling\nNIOSH: National Institute for Occupational Safety and Health\n\n17. Revision History\nRevision Date:  3/5/2019\nRevision Number:  00077182001\n\n18. Additional Information\nNone.\n\n19. Emergency Contact Information\nEmergency Telephone: 1-800-535-5053,\n1-352-323-3500, 1-800-222-122",
#     "EINECS number": "Please provide the EINECS number extracted from the given text:",
#     "RTECS number": "Please enter the RTECS number:",
#     "Molecular formula": "The molecular formula for the product is not explicitly stated in the provided SDS. However, the chemical names and CAS numbers of the ingredients are listed:\n\n* Dimethyl glutarate (CAS-No. 1119-40-0)\n* Dimethyl succinate (CAS-No. 106-65-0)\n* Dimethyl adipate (CAS-No. 627-93-0)\n* Diethanolamine (CAS-No. 111-42-2)\n\nTherefore, the molecular formula for the product cannot be determined from the provided SDS.",
#     "Molecular weight": "Please provide the molecular weight of the product described in the SDS.\n\nNote: The molecular weight can be found in the section 3, Composition/Information on Ingredients.",
#     "Physical state (solid, liquid, gas)": "Please provide the actual physical state of the substance described in the SDS.",
#     "Appearance": "The appearance of the text is as follows:\n\n* The text is written in a formal and professional tone.\n* It uses technical language and jargon related to chemistry and safety.\n* It includes various sections and subsections, each with its own specific purpose and content.\n* It includes tables, lists, and bullet points to organize and present information in a clear and concise manner.\n* It uses abbreviations and acronyms to represent technical terms and regulations.\n* It includes references to external sources, such as regulations and standards.\n* It includes a disclaimer and a statement of liability.\n\nOverall, the appearance of the text suggests that it is a technical document intended for use by professionals in a scientific or industrial setting.",
#     "Odor": "The odor of the product is described as \"fruity\".",
#     "pH": "Please provide the pH of the product described in the SDS.\n\nNote: The pH of a product is a measure of its acidity or basicity. A pH of 7 is neutral, while a pH less than 7 is acidic and a pH greater than 
# 7 is basic.",
#     "Melting point": "Please enter the Melting point of the substance:",
#     "Boiling point": "Please enter the boiling point of the product in degrees Celsius:\n\n100-100",
#     "Flash point": "Please enter the flash point of the substance in degrees Celsius:\n\n100",
#     "Density": "Please provide the actual density value instead of the range.\nThe density of Caulk Be Gone is 1.04 g/cm3.",
#     "Solubility in water": "Please provide the actual solubility value in water, if it's not mentioned in the text, put \"Not mentioned\"",
#     "Solubility in other solvents": "Please provide the solubility information for the product.\n\nThe solubility information for the product is not explicitly stated in the provided SDS. However, it can be inferred that the product is soluble in water to some extent, as it is stated that the product is a \"thick liquid\" with a \"fruity\" odor, and it has a low viscosity. Additionally, the product is stated to be \"not likely to 
# present an inhalation hazard at ambient conditions,\" which suggests that it is not highly volatile and may be soluble in water. However, the exact solubility of the product in water is not provided in the SDS.\n\nTherefore, the solubility information for the product is:\n\nSolubility in water: Not explicitly stated, but likely soluble to some extent.",
#     "Vapor pressure": "Please provide the actual vapor pressure value in mmHg.",
#     "Autoignition temperature": "Please provide the Autoignition temperature in degrees Celsius.",
#     "Decomposition temperature": "Please provide the Decomposition temperature in Celsius."
# }