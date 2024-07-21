#------------------------------------------ FIND NAME AND EMAIL FROM PDF --------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------


import fitz 
import json
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ibm import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes


credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
}

try:
    project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"
except KeyError:
    project_id = input("Please enter your project_id (hit enter): ")


embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')


persist_directory = "C:/Users/RiGupta/Desktop/27_may/persist_directory"


docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

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


def extract_info_from_text_usellm(llm_model, text):
    try:
        
        prompt = (
            "Extract names and emails from the following text and return the result in JSON format:\n\n"
            f"{text}\n\n"
            "Return the result as a JSON array of objects with 'Name' and 'Email' fields:"
        )
       
        extracted_info = llm_model.invoke(prompt)
        return extracted_info
    except Exception as e:
        print(f"Error occurred during text extraction: {str(e)}")
        return None


pdf_path = "sampleee.pdf"


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

pdf_text = extract_text_from_pdf(pdf_path)


extracted_info = extract_info_from_text_usellm(llama, pdf_text)


try:
    output_json = json.loads(extracted_info)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {str(e)}")
    output_json = {"Extracted_Info": None}


print(json.dumps(output_json, indent=4))


# [
#     {
#         "Name": "Emily Thompson",
#         "Email": "emily.thompson@gmail.com"
#     },
#     {
#         "Name": "Lisa Harper",
#         "Email": "lisa.harper@gmail.com"   
#     },
#     {
#         "Name": "Sarah Jenkins",
#         "Email": "sarah.jenkins@pixeldreams.com"
#     },
#     {
#         "Name": "Mark Williamson",
#         "Email": "mark.williamson@pixeldreams.com"
#     },
#     {
#         "Name": "Robert Sterling",
#         "Email": "robert.sterling@pixeldreams.com"
#     },
#     {
#         "Name": "John Miller",
#         "Email": "john.miller@meadowbrookfarm.com"
#     },
#     {
#         "Name": "Mrs. Evelyn Parker",
#         "Email": "evelyn.parker@booknook.com"
#     },
#     {
#         "Name": "Jacob Riley",
#         "Email": "jacob.riley.art@gmail.com"
#     },
#     {
#         "Name": "Mary Davis",
#         "Email": "mary.davis@cozyinn.com"
#     }
# ]



