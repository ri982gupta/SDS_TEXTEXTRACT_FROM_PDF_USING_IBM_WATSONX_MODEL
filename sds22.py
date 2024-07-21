#----------------------------------------------------------------------------EXTRACT ALL SDS PARAMETERS----------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# import json
# import fitz
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Initialize LLM model
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

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

# # Function to extract text from the PDF
# def extract_text_from_pdf(pdf_path):
#     try:
#         with fitz.open(pdf_path) as doc:
#             text = ""
#             for page in doc:
#                 text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"Error occurred while extracting text from PDF: {str(e)}")
#         return None

# # Function to extract information from a specific section using LLM model
# def extract_section_info(llm_model, section_text):
#     try:
#         # Process section text through LLM model to extract information
#         response = llm_model.invoke(section_text)
#         extracted_info = response.strip()
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during LLM extraction: {str(e)}")
#         return None

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Extract information for each section
#     section_info = {}

#     # General Information section
#     general_info_section_text = "Text extracted from the General Information section"
#     general_info = extract_section_info(llama, general_info_section_text)
#     section_info["General Information"] = general_info

#     # Hazards section
#     hazards_section_text = "Text extracted from the Hazards section"
#     hazards_info = extract_section_info(llama, hazards_section_text)
#     section_info["Hazards"] = hazards_info

#     # Emergency Response section
#     emergency_response_section_text = "Text extracted from the Emergency Response section"
#     emergency_response_info = extract_section_info(llama, emergency_response_section_text)
#     section_info["Emergency Response"] = emergency_response_info

#     # Transport Information section
#     transport_info_section_text = "Text extracted from the Transport Information section"
#     transport_info = extract_section_info(llama, transport_info_section_text)
#     section_info["Transport Information"] = transport_info

#     # Regulatory Information section
#     regulatory_info_section_text = "Text extracted from the Regulatory Information section"
#     regulatory_info = extract_section_info(llama, regulatory_info_section_text)
#     section_info["Regulatory Information"] = regulatory_info

#     # Miscellaneous section
#     miscellaneous_section_text = "Text extracted from the Miscellaneous section"
#     miscellaneous_info = extract_section_info(llama, miscellaneous_section_text)
#     section_info["Miscellaneous"] = miscellaneous_info

#     # Construct JSON output
#     json_output = json.dumps(section_info, indent=4)
#     print(json_output)
# else:
#     print("No text extracted from the PDF.")




# {
#     "General Information": "of the report:\n\nThe report provides an overview of the current state of the global energy storage market, highlighting key trends, challenges, and opportunities. It covers various energy storage technologies, including batteries, pumped hydro storage, compressed air energy storage, and flywheels. The report also discusses the role of energy storage in various applications, such as grid-scale energy storage, residential energy storage, and electric vehicles.\n\nThe report highlights the growing demand for energy storage, driven by the increasing penetration of renewable energy sources and the need for grid flexibility. It also discusses the declining costs of energy storage technologies, which are making them more competitive with traditional energy sources. The report notes that the energy storage market is expected to continue to grow rapidly in the coming years, with a compound annual growth rate of 27% from 2020 to 2025.\n\nThe report also highlights the importance of energy storage for achieving a low-carbon energy system. It notes that energy storage can help to mitigate the intermittency of renewable energy sources, such as solar and wind, and can provide a source of clean energy for transportation and industry. The report emphasizes the need for continued research and development to improve the efficiency, cost-effectiveness, and scalability of energy storage technologies.\n\nThe report concludes by highlighting the key challenges facing the energy storage industry, including the need for better regulations and incentives, the need for more effective energy storage systems, and the need for more research and development. It also highlights the opportunities for energy storage, including its potential to enable a low-carbon energy system, its potential to provide grid resilience and reliability, and its potential to create new jobs and economic opportunities.",
#     "Hazards": "of the relevant Wikipedia article. * '''Fatality rate:''' The number of fatalities resulting from the disaster, expressed as a rate per 100,000 people. * '''Injury rate:''' The number of injuries resulting from the disaster, expressed as a rate per 100,000 people. * '''Economic loss:''' An estimate of the total economic loss resulting from the disaster, expressed in millions of US dollars. * '''Affected area:''' A description of the area affected by the 
# disaster, including the location, size, and population density of the affected region. * '''Cause:''' A brief description of the cause of the disaster, including any relevant background information or contributing factors. * '''Response:''' A brief description of the response to the disaster, including any notable relief efforts or rescue operations. * '''Notes:''' Any additional information or notable facts about the disaster. The data was collected from various sources, including news articles, government reports, and non-profit organizations. The data is presented in a table format, with each row representing a different disaster and each column representing a different variable. The data can be used to analyze and compare the different disasters, and to identify patterns or trends in the data. For example, the data can be used to compare the fatality rates and economic losses of different disasters, or to identify the most common 
# causes of disasters. The data can also be used to evaluate the effectiveness of different response efforts and to identify areas for improvement.",
#     "Emergency Response": "of the website.\n\nThe Emergency Response Plan (ERP) is a comprehensive guide that outlines the roles, responsibilities, and procedures for responding to emergencies at [University Name]. The plan is designed to ensure that the university is prepared to respond quickly and effectively in the event of an emergency, and to minimize the impact on students, faculty, staff, and the surrounding community.\n\nThe ERP covers a wide range of emergency 
# situations, including natural disasters, fires, hazardous materials incidents, medical emergencies, and security threats. It outlines the steps that should be taken in each situation, including evacuation procedures, communication protocols, and response strategies. The plan also identifies the key personnel and teams that are responsible for implementing the plan, and provides contact information for emergency response teams, first responders, and local authorities.\n\nIn addition to the ERP, [University Name] has established an Emergency Management Team (EMT) that is responsible for coordinating the university's response to emergencies. The EMT is composed of representatives from various departments, including Campus Safety, Facilities, Student Affairs, and Communications. The team meets regularly to review the ERP, discuss emergency response strategies, and coordinate training and drills.\n\n[University Name] also has a comprehensive emergency alert system that is used to notify the university community of emergencies and provide instructions on how to respond. The system includes text messaging, email, and social media, and can be activated quickly in the event of an emergency.\n\nOverall, the ERP and emergency management processes at [University Name] are designed to ensure that the university is well-prepared to respond to emergencies and protect the safety and well-being of the university community.",
#     "Transport Information": "of the London 2012 Olympic Games website.\n\nThe Olympic Park is located in Stratford, East London, and is easily accessible by public transport. The park is served by several bus routes, including the Olympic Park bus, which runs from Stratford Station to the Olympic Park. Additionally, there are several train stations nearby, including Stratford Station, which is served by the Jubilee and Central lines, as well as the Docklands Light Railway.\n\nVisitors can also use the London Overground, which runs from Liverpool Street Station to Stratford Station, and the Eurostar, which runs from St Pancras International to Stratford International. There are also several cycle routes that run through the Olympic Park, and visitors can use the Barclays Cycle Hire scheme to rent bikes.\n\nFor those driving, there are several car parks located near the Olympic Park, and visitors can use the Park & Ride facility at Ebbsfleet International Station, which offers direct train services to Stratford Station.\n\nFinally, the Olympic Park is also accessible by river, with several boat services running from central London to the Olympic Park.\n\nOverall, the 
# Olympic Park is well connected to the rest of London and the surrounding area, with a range of transport options available to visitors.",
#     "Regulatory Information": "of the Federal Register document.\n\nThe Regulatory Flexibility Act (RFA) requires that agencies consider the impact of their regulations on small entities, including small businesses, small governmental jurisdictions, and small organizations. The RFA requires agencies to assess the impact of their regulations on these entities and to consider alternatives that would minimize any significant economic impact.\n\nThe FCC has prepared an Initial Regulatory Flexibility Analysis (IRFA) for this rulemaking, which is included in the Proposed Rule. The IRFA identifies the small entities that may be affected by the proposed rules and describes the impact of the proposed rules on these entities. The IRFA also discusses possible alternatives that could minimize the impact of the proposed rules on small entities.\n\nThe FCC invites comments on the IRFA and on any other aspects of the proposed rules that may affect small entities. The FCC will consider these comments in developing the Final Rule.\n\nA copy of the IRFA is available for public inspection during regular business hours in the FCC's Reference Information Center, Room CY-A257, 445 12th Street, SW., Washington, DC 20554. The IRFA is also available on the FCC's website at <http://www.fcc.gov/wcb/tribal-lands-nprm/>.\n\nTo request materials in accessible formats for people with disabilities (Braille, large print, electronic files, audio format), send an email to [fcc504@fcc.gov](mailto:fcc504@fcc.gov) or call the FCC's Consumer Center at (888) 225-5322 (voice), (888) 835-5322",
#     "Miscellaneous": "of the 1911 Census of England and Wales, giving details of the institution, its location, and the numbers of patients, staff, and visitors. The institutions covered include workhouses, hospitals, homes for the sick, and other institutions providing care.\n\n### 1911 Census of England and Wales, County Report (1911)\n\nThe County Reports were published by the Registrar General and provide a summary of the census returns for each county in England and Wales. They include information on population, area, birthplaces, occupations, and industry.\n\n### 1911 Census of England and Wales, Enumerators' Summary Books (1911)\n\nThe Enumerators' Summary Books were used by the enumerators to record the details of the households they visited. They provide a summary of the information collected in the census, including the number of people in each household, their ages, sexes, occupations, and birthplaces.\n\n### 1911 Census of England and Wales, Institutions (1911)\n\nThe Institutions collection contains the census returns for institutions such as workhouses, hospitals, barracks, and schools. The records provide information about the staff and inmates of these institutions, including their names, ages, sexes, occupations, and birthplaces.\n\n### 1911 Census of England and Wales, Military (1911)\n\nThe Military collection contains the census returns for military personnel stationed in England and Wales. The records provide information about the soldiers, including their names, ages, ranks, and birthplaces.\n\n### 1911 Census of England and Wales, Merchant Navy (1911)\n\nThe Merchant Navy collection contains the census returns for merchant se"
# }

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# import json
# import fitz
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Initialize LLM model
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

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

# # Function to extract text from the PDF
# def extract_text_from_pdf(pdf_path):
#     try:
#         with fitz.open(pdf_path) as doc:
#             text = ""
#             for page in doc:
#                 text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"Error occurred while extracting text from PDF: {str(e)}")
#         return None

# # Function to extract information from a specific section using LLM model
# def extract_section_info(llm_model, section_text):
#     try:
#         # Process section text through LLM model to extract information
#         response = llm_model.invoke(section_text)
#         extracted_info = response.strip()
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during LLM extraction: {str(e)}")
#         return None

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Extract information for each section
#     section_info = {}

#     # General Information section
#     general_info_section_text = "Text extracted from the General Information section"
#     general_info = extract_section_info(llama, general_info_section_text)
#     section_info["General Information"] = general_info

#     # Hazards section
#     hazards_section_text = "Text extracted from the Hazards section"
#     hazards_info = extract_section_info(llama, hazards_section_text)
#     section_info["Hazards"] = hazards_info

#     # Emergency Response section
#     emergency_response_section_text = "Text extracted from the Emergency Response section"
#     emergency_response_info = extract_section_info(llama, emergency_response_section_text)
#     section_info["Emergency Response"] = emergency_response_info

#     # Transport Information section
#     transport_info_section_text = "Text extracted from the Transport Information section"
#     transport_info = extract_section_info(llama, transport_info_section_text)
#     section_info["Transport Information"] = transport_info

#     # Regulatory Information section
#     regulatory_info_section_text = "Text extracted from the Regulatory Information section"
#     regulatory_info = extract_section_info(llama, regulatory_info_section_text)
#     section_info["Regulatory Information"] = regulatory_info

#     # Miscellaneous section
#     miscellaneous_section_text = "Text extracted from the Miscellaneous section"
#     miscellaneous_info = extract_section_info(llama, miscellaneous_section_text)
#     section_info["Miscellaneous"] = miscellaneous_info

#     # Construct JSON output with separate curly braces for each section
#     json_output = json.dumps(section_info, indent=4)
#     print(json_output)
# else:
#     print("No text extracted from the PDF.")



# {
#     "General Information": "of the report:\n\nThe report provides an overview of the current state of the global energy storage market, highlighting key trends, challenges, and opportunities. It covers various energy storage technologies, including batteries, pumped hydro storage, compressed air energy storage, and flywheels. The report also discusses the role of energy storage in various applications, such as grid-scale energy storage, residential energy storage, and electric vehicles.\n\nThe report highlights the growing demand for energy storage, driven by the increasing penetration of renewable energy sources and the need for grid flexibility. It also discusses the declining costs of energy storage technologies, which are making them more competitive with traditional energy sources. The report notes that the energy storage market is expected to continue to grow rapidly in the coming years, with a compound annual growth rate of 27% from 2020 to 2025.\n\nThe report also highlights the importance of energy storage for achieving a low-carbon energy system. It notes that energy storage can help to mitigate the intermittency of renewable energy sources, such as solar and wind, and can provide a source of clean energy for transportation and industry. The report emphasizes the need for continued research and development to improve the efficiency, cost-effectiveness, and scalability of energy storage technologies.\n\nThe report concludes by highlighting the key challenges facing the energy storage industry, including the need for better regulations and incentives, the need for more effective energy storage systems, and the need for more research and development. It also highlights the opportunities for energy storage, including its potential to enable a low-carbon energy system, its potential to provide grid resilience and reliability, and its potential to create new jobs and economic opportunities.",
#     "Hazards": "of the relevant Wikipedia article. * '''Fatality rate:''' The number of fatalities resulting from the disaster, expressed as a rate per 100,000 people. * '''Injury rate:''' The number of injuries resulting from the disaster, expressed as a rate per 100,000 people. * '''Economic loss:''' An estimate of the total economic loss resulting from the disaster, expressed in millions of US dollars. * '''Affected area:''' A description of the area affected by the 
# disaster, including the location, size, and population density of the affected region. * '''Cause:''' A brief description of the cause of the disaster, including any relevant background information or contributing factors. * '''Response:''' A brief description of the response to the disaster, including any notable relief efforts or rescue operations. * '''Notes:''' Any additional information or notable facts about the disaster. The data was collected from various sources, including news articles, government reports, and non-profit organizations. The data is presented in a table format, with each row representing a different disaster and each column representing a different variable. The data can be used to analyze and compare the different disasters, and to identify patterns or trends in the data. For example, the data can be used to compare the fatality rates and economic losses of different disasters, or to identify the most common 
# causes of disasters. The data can also be used to evaluate the effectiveness of different response efforts and to identify areas for improvement.",
#     "Emergency Response": "of the website.\n\nThe Emergency Response Plan (ERP) is a comprehensive guide that outlines the roles, responsibilities, and procedures for responding to emergencies at [University Name]. The plan is designed to ensure that the university is prepared to respond quickly and effectively in the event of an emergency, and to minimize the impact on students, faculty, staff, and the surrounding community.\n\nThe ERP covers a wide range of emergency 
# # situations, including natural disasters, fires, hazardous materials incidents, medical emergencies, and security threats. It outlines the steps that should be taken in each situation, including evacuation procedures, communication protocols, and response strategies. The plan also identifies the key personnel and teams that are responsible for implementing the plan, and provides contact information for emergency response teams, first responders, and local authorities.\n\nIn addition to the ERP, [University Name] has established an Emergency Management Team (EMT) that is responsible for coordinating the university's response to emergencies. The EMT is composed of representatives from various departments, including Campus Safety, Facilities, Student Affairs, and Communications. The team meets regularly to review the ERP, discuss emergency response strategies, and coordinate training and drills.\n\n[University Name] also has a comprehensive emergency alert system that is used to notify the university community of emergencies and provide instructions on how to respond. The system includes text messaging, email, and social media, and can be activated quickly in the event of an emergency.\n\nOverall, the ERP and emergency management processes at [University Name] are designed to ensure that the university is well-prepared to respond to emergencies and protect the safety and well-being of the university community.",
# #     "Transport Information": "of the London 2012 Olympic Games website.\n\nThe Olympic Park is located in Stratford, East London, and is easily accessible by public transport. The park is served by several bus routes, including the Olympic Park bus, which runs from Stratford Station to the Olympic Park. Additionally, there are several train stations nearby, including Stratford Station, which is served by the Jubilee and Central lines, as well as the Docklands Light Railway.\n\nVisitors can also use the London Overground, which runs from Liverpool Street Station to Stratford Station, and the Eurostar, which runs from St Pancras International to Stratford International. There are also several cycle routes that run through the Olympic Park, and visitors can use the Barclays Cycle Hire scheme to rent bikes.\n\nFor those driving, there are several car parks located near the Olympic Park, and visitors can use the Park & Ride facility at Ebbsfleet International Station, which offers direct train services to Stratford Station.\n\nFinally, the Olympic Park is also accessible by river, with several boat services running from central London to the Olympic Park.\n\nOverall, the 
# # Olympic Park is well connected to the rest of London and the surrounding area, with a range of transport options available to visitors.",
# #     "Regulatory Information": "of the Federal Register document.\n\nThe Regulatory Flexibility Act (RFA) requires that agencies consider the impact of their regulations on small entities, including small businesses, small governmental jurisdictions, and small organizations. The RFA requires agencies to assess the impact of their regulations on these entities and to consider alternatives that would minimize any significant economic impact.\n\nThe FCC has prepared an Initial Regulatory Flexibility Analysis (IRFA) for this rulemaking, which is included in the Proposed Rule. The IRFA identifies the small entities that may be affected by the proposed rules and describes the impact of the proposed rules on these entities. The IRFA also discusses possible alternatives that could minimize the impact of the proposed rules on small entities.\n\nThe FCC invites comments on the IRFA and on any other aspects of the proposed rules that may affect small entities. The FCC will consider these comments in developing the Final Rule.\n\nA copy of the IRFA is available for public inspection during regular business hours in the FCC's Reference Information Center, Room CY-A257, 445 12th Street, SW., Washington, DC 20554. The IRFA is also available on the FCC's website at <http://www.fcc.gov/wcb/tribal-lands-nprm/>.\n\nTo request materials in accessible formats for people with disabilities (Braille, large print, electronic files, audio format), send an email to [fcc504@fcc.gov](mailto:fcc504@fcc.gov) or call the FCC's Consumer Center at (888) 225-5322 (voice), (888) 835-5322",
# #     "Miscellaneous": "of the 1911 Census of England and Wales, giving details of the institution, its location, and the numbers of patients, staff, and visitors. The institutions covered include workhouses, hospitals, homes for the sick, and other institutions providing care.\n\n### 1911 Census of England and Wales, County Report (1911)\n\nThe County Reports were published by the Registrar General and provide a summary of the census returns for each county in England and Wales. They include information on population, area, birthplaces, occupations, and industry.\n\n### 1911 Census of England and Wales, Enumerators' Summary Books (1911)\n\nThe Enumerators' Summary Books were used by the enumerators to record the details of the households they visited. They provide a summary of the information collected in the census, including the number of people in each household, their ages, sexes, occupations, and birthplaces.\n\n### 1911 Census of England and Wales, Institutions (1911)\n\nThe Institutions collection contains the census returns for institutions such as workhouses, hospitals, barracks, and schools. The records provide information about the staff and inmates of these institutions, including their names, ages, sexes, occupations, and birthplaces.\n\n### 1911 Census of England and Wales, Military (1911)\n\nThe Military collection contains the census returns for military personnel stationed in England and Wales. The records provide information about the soldiers, including their names, ages, ranks, and birthplaces.\n\n### 1911 Census of England and Wales, Merchant Navy (1911)\n\nThe Merchant Navy collection contains the census returns for merchant se"
# # }





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


import json
import fitz
from langchain_ibm import WatsonxLLM  # Hypothetical import, replace with actual implementation
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes  # Hypothetical import, replace with actual implementation

# Initialize LLM model
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
}

project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 400,
    "temperature": 0.2,
    "stop_sequences": ["conclusion"]
}

model_id = ModelTypes.LLAMA_2_70B_CHAT  # Hypothetical enum value, replace with actual model ID
llama = WatsonxLLM(
    model_id=model_id.value,
    url=credentials.get("url"),
    apikey=credentials.get("apikey"),
    project_id=project_id,
    params=parameters
)

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error occurred while extracting text from PDF: {str(e)}")
        return None

# Adjusted function to extract information from a specific section using LLM model
def extract_section_info(llm_model, section_text):
    try:
        # Process section text through LLM model to extract information
        response = llm_model.invoke(section_text)
        # Explicitly adding curly braces around the extracted information
        extracted_info = " { " + response.strip() + " } "
        return extracted_info
    except Exception as e:
        print(f"Error occurred during LLM extraction: {str(e)}")
        return None

# Path to the PDF file
pdf_path = "GHS Rev10e.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

if pdf_text:
    # Initialize main section info dictionary
    section_info = {}

    # Example sections - replace with actual section texts
    section_texts = {
        "General Information": "Text extracted from the General Information section",
        "Hazards": "Text extracted from the Hazards section",
        "Emergency Response": "Text extracted from the Emergency Response section",
        "Transport Information": "Text extracted from the Transport Information section",
        "Regulatory Information": "Text extracted from the Regulatory Information section",
        "Miscellaneous": "Text extracted from the Miscellaneous section"
    }

    for section_name, section_text in section_texts.items():
        formatted_section_text = f"{ extract_section_info(llama, section_text) } "
        section_info[section_name] = formatted_section_text


    # Construct JSON output with separate curly braces for each section
    json_output = json.dumps(section_info, indent=4)
    print(json_output)
else:
    print("No text extracted from the PDF.")




# {
#     "General Information": " { of the report:\n\nThe report provides an overview of the current state of the global energy storage market, highlighting key trends, challenges, and opportunities. It covers various energy storage technologies, including batteries, pumped hydro storage, compressed air energy storage, and flywheels. The report also discusses the role of energy storage in various applications, such as grid-scale energy storage, residential energy storage, and electric vehicles.\n\nThe report highlights the growing demand for energy storage, driven by the increasing penetration of renewable energy sources and the need for grid flexibility. It also discusses the declining costs of energy storage technologies, which are making them more competitive with traditional energy sources. The report notes that the energy storage market is expected to continue to grow rapidly in the coming years, with a compound annual growth rate of 
# 27% from 2020 to 2025.\n\nThe report also highlights the importance of energy storage for achieving a low-carbon energy system. It notes that energy storage can help to mitigate the intermittency of renewable energy sources, such as solar and wind, and can provide a source of clean energy for transportation and industry. The report emphasizes the need for continued research and development to improve the efficiency, cost-effectiveness, and scalability of energy storage 
# technologies.\n\nThe report concludes by highlighting the key challenges facing the energy storage industry, including the need for better regulations and incentives, the need for more effective energy storage systems, and the need for more research and development. It also highlights the opportunities for energy storage, including its potential to enable a low-carbon energy system, its potential to provide grid resilience and reliability, and its potential to create new jobs and economic opportunities. }  ",
#     "Hazards": " { of the relevant Wikipedia article. * '''Fatality rate:''' The number of fatalities resulting from the disaster, expressed as a rate per 100,000 people. * '''Injury rate:''' The number of injuries resulting from the disaster, expressed as a rate per 100,000 people. * '''Economic loss:''' An estimate of the total economic loss resulting from the disaster, expressed in millions of US dollars. * '''Affected area:''' A description of the area affected by the disaster, including the location, size, and population density of the affected region. * '''Cause:''' A brief description of the cause of the disaster, including any relevant background information or contributing factors. * '''Response:''' A brief description of the response to the disaster, including any notable relief efforts or rescue operations. * '''Notes:''' Any additional information or notable facts about the disaster. The data was collected from various sources, including news articles, government reports, and non-profit organizations. The data is presented in a table format, with each row representing a different disaster and each column representing a different variable. The data can be 
# used to analyze and compare the different disasters, and to identify patterns or trends in the data. For example, the data can be used to compare the fatality rates and economic losses of different disasters, or to identify the most common causes of disasters. The data can also be used to evaluate the effectiveness of different response efforts and to identify areas for improvement. }  ",
#     "Emergency Response": " { of the website.\n\nThe Emergency Response Plan (ERP) is a comprehensive guide that outlines the roles, responsibilities, and procedures for responding to emergencies at [University Name]. The plan is designed to ensure that the university is prepared to respond quickly and effectively in the event of an emergency, and to minimize the impact on students, faculty, staff, and the surrounding community.\n\nThe ERP covers a wide range of emergency situations, including natural disasters, fires, hazardous materials incidents, medical emergencies, and security threats. It outlines the steps that should be taken in each situation, including evacuation procedures, communication protocols, and response strategies. The plan also identifies the key personnel and teams that are responsible for implementing the plan, and provides contact information for emergency response teams, first responders, and local authorities.\n\nIn addition to the ERP, [University Name] has established an Emergency Management Team (EMT) that is responsible for coordinating the university's response to emergencies. The EMT is composed of representatives from various departments, including Campus Safety, Facilities, Student Affairs, and Communications. The team meets regularly to review the ERP, discuss emergency response strategies, and coordinate training and drills.\n\n[University Name] also has a comprehensive emergency alert system that is used to notify the university community of emergencies and provide instructions on how to respond. The system includes text messaging, email, and social media, and can be activated quickly in the event of an emergency.\n\nOverall, the ERP and emergency management processes at [University Name] are designed to ensure that the university is well-prepared to respond to emergencies and protect the safety and well-being of the university 
# community. }  ",
#     "Transport Information": " { of the London 2012 Olympic Games website.\n\nThe Olympic Park is located in Stratford, East London, and is easily accessible by public transport. The park is served by several bus routes, including the Olympic Park bus, which runs from Stratford Station to the Olympic Park. Additionally, there are several train stations nearby, including Stratford Station, which is served by the Jubilee and Central lines, as well as the Docklands Light Railway.\n\nVisitors can also use the London Overground, which runs from Liverpool Street Station to Stratford Station, and the Eurostar, which runs from St Pancras International to Stratford International. There are also several cycle routes that run through the Olympic Park, and visitors can use the Barclays Cycle Hire scheme to rent bikes.\n\nFor those driving, there are several car parks located near the Olympic Park, and visitors can use the Park & Ride facility at 
# Ebbsfleet International Station, which offers direct train services to Stratford Station.\n\nFinally, the Olympic Park is also accessible by river, with several boat services running from central London to the Olympic Park.\n\nOverall, the Olympic Park is well connected to the rest of London and the surrounding area, with a range of transport options available to visitors. }  ",
#     "Regulatory Information": " { of the Federal Register document.\n\nThe Regulatory Flexibility Act (RFA) requires that agencies consider the impact of their regulations on small entities, including small businesses, small governmental jurisdictions, and small organizations. The RFA requires agencies to assess the impact of their regulations on these entities and to consider alternatives that would minimize any significant economic impact.\n\nThe FCC has prepared an Initial Regulatory Flexibility Analysis (IRFA) for this rulemaking, which is included in the Proposed Rule. The IRFA identifies the small entities that may be affected by the proposed rules and describes the impact of the proposed rules on these entities. The IRFA also discusses possible alternatives that could minimize the impact of the proposed rules on small entities.\n\nThe FCC invites comments on the IRFA and on any other aspects of the proposed rules that may affect small entities. The FCC will consider these comments in developing the Final Rule.\n\nA copy of the IRFA is available for public inspection during regular business hours in the FCC's Reference Information Center, Room CY-A257, 445 12th Street, SW., Washington, DC 20554. The IRFA is also available on the FCC's website at <http://www.fcc.gov/wcb/tribal-lands-nprm/>.\n\nTo request materials in accessible formats for people with disabilities (Braille, large print, electronic files, audio format), send an email to [fcc504@fcc.gov](mailto:fcc504@fcc.gov) or call the FCC's Consumer Center at (888) 225-5322 (voice), (888) 835-5322 }  ",
#     "Miscellaneous": " { of the 1911 Census of England and Wales, giving details of the institution, its location, and the numbers of patients, staff, and visitors. The institutions covered include workhouses, hospitals, homes for the sick, and other institutions providing care.\n\n### 1911 Census of England and Wales, County Report (1911)\n\nThe County Reports were produced by the Registrar General's office and provide a summary of the census returns for each county in England and Wales. They include information on population, area, birthplaces, occupations, and industry.\n\n### 1911 Census of England and Wales, Enumerators' Summary Books (1911)\n\nThe Enumerators' Summary Books were produced by the enumerators who collected the census returns. They provide a summary of the returns for each enumeration district, including the number of households, population, and occupation.\n\n### 1911 Census of England and Wales, Institutions (1911)\n\nThe Institutions collection contains the census returns for institutions such as workhouses, hospitals, barracks, and schools. The records provide information about the staff and inmates of the institutions, including their age, sex, occupation, and place of birth.\n\n### 1911 Census of England and Wales, Military (1911)\n\nThe Military collection contains the census returns for military personnel stationed in England and Wales. The records provide information about the soldiers, including their age, rank, occupation, and place of birth.\n\n### 1911 Census of England and Wales, Merchant Navy (1911)\n\nThe Merchant Navy collection contains the census returns for merchant seamen stationed in England and Wales. The records provide information about the seamen }  "
# }





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# correct json format of previous output

# import json
# import fitz
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
# import time

# # Initialize LLM model
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

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

# # Function to extract text from the PDF
# def extract_text_from_pdf(pdf_path):
#     try:
#         with fitz.open(pdf_path) as doc:
#             text = ""
#             for page in doc:
#                 text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"Error occurred while extracting text from PDF: {str(e)}")
#         return None

# # Function to split text into smaller chunks
# def chunk_text(text, max_tokens=1000):
#     words = text.split()
#     chunks = []
#     current_chunk = []

#     for word in words:
#         current_chunk.append(word)
#         # Check if the current chunk exceeds the maximum token limit
#         if len(" ".join(current_chunk)) >= max_tokens:
#             chunks.append(" ".join(current_chunk))
#             current_chunk = []

#     # Add any remaining words as the last chunk
#     if current_chunk:
#         chunks.append(" ".join(current_chunk))
    
#     return chunks

# # Function to extract specific information using LLM model with retry logic
# def extract_specific_info(llm_model, text_chunks, prompt_template, retries=3):
#     extracted_info = []
#     for chunk in text_chunks:
#         for attempt in range(retries):
#             try:
#                 prompt = prompt_template.format(text=chunk)
#                 response = llm_model.invoke([prompt])
#                 extracted_info.append(response[0].strip())
#                 break
#             except Exception as e:
#                 print(f"Error occurred during LLM extraction: {str(e)}")
#                 if attempt < retries - 1:
#                     print("Retrying...")
#                     time.sleep(5)  # Wait before retrying
#                 else:
#                     print("Max retries reached. Skipping this chunk.")
#     return extracted_info

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Chunk the text to stay within the token limit
#     text_chunks = chunk_text(pdf_text, max_tokens=1000)

#     # Define prompts for specific information
#     prompts = {
#         "General Information": {
#             "Chemical Name": "Extract the Chemical Name from the following text:\n\n{text}\n\n",
#             "CAS Number": "Extract the CAS Number from the following text:\n\n{text}\n\n",
#             "EINECS Number": "Extract the EINECS Number from the following text:\n\n{text}\n\n"
#         },
#         "Hazards": {
#             "Acute Toxicity": "Extract the Acute Toxicity information from the following text:\n\n{text}\n\n",
#             "Skin Irritation": "Extract the Skin Irritation information from the following text:\n\n{text}\n\n",
#             "Eye Irritation": "Extract the Eye Irritation information from the following text:\n\n{text}\n\n"
#             # Add more prompts as needed
#         },
#         "Emergency Response": {
#             "First-aid Measures": "Extract the First-aid Measures from the following text:\n\n{text}\n\n",
#             "Firefighting Measures": "Extract the Firefighting Measures from the following text:\n\n{text}\n\n",
#             "Accidental Release Measures": "Extract the Accidental Release Measures from the following text:\n\n{text}\n\n"
#         },
#         "Transport Information": {
#             "UN Number": "Extract the UN Number from the following text:\n\n{text}\n\n",
#             "Proper Shipping Name": "Extract the Proper Shipping Name from the following text:\n\n{text}\n\n",
#             "Transport Hazard Class": "Extract the Transport Hazard Class from the following text:\n\n{text}\n\n"
#         },
#         "Regulatory Information": {
#             "OSHA Classification": "Extract the OSHA Classification from the following text:\n\n{text}\n\n",
#             "European CLP Regulation": "Extract the European CLP Regulation from the following text:\n\n{text}\n\n",
#             "Canadian WHMIS Classification": "Extract the Canadian WHMIS Classification from the following text:\n\n{text}\n\n"
#         },
#         "Miscellaneous": {
#             "Chemical Structure": "Extract the Chemical Structure from the following text:\n\n{text}\n\n",
#             "Synonyms": "Extract the Synonyms from the following text:\n\n{text}\n\n",
#             "Trade Names": "Extract the Trade Names from the following text:\n\n{text}\n\n"
#         }
#     }

#     # Extract information for each section
#     section_info = {}

#     # General Information section
#     general_info = {}
#     for key, prompt_template in prompts["General Information"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         general_info[key] = extracted_info
#     section_info["General Information"] = general_info

#     # Hazards section
#     hazards_info = {}
#     for key, prompt_template in prompts["Hazards"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         hazards_info[key] = extracted_info
#     section_info["Hazards"] = hazards_info

#     # Emergency Response section
#     emergency_response_info = {}
#     for key, prompt_template in prompts["Emergency Response"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         emergency_response_info[key] = extracted_info
#     section_info["Emergency Response"] = emergency_response_info

#     # Transport Information section
#     transport_info = {}
#     for key, prompt_template in prompts["Transport Information"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         transport_info[key] = extracted_info
#     section_info["Transport Information"] = transport_info

#     # Regulatory Information section
#     regulatory_info = {}
#     for key, prompt_template in prompts["Regulatory Information"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         regulatory_info[key] = extracted_info
#     section_info["Regulatory Information"] = regulatory_info

#     # Miscellaneous section
#     miscellaneous_info = {}
#     for key, prompt_template in prompts["Miscellaneous"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         miscellaneous_info[key] = extracted_info
#     section_info["Miscellaneous"] = miscellaneous_info

#     # Construct JSON output with separate curly braces for each section
#     json_output = json.dumps(section_info, indent=4)
#     print(json_output)
# else:
#     print("No text extracted from the PDF.")



# Error occurred during LLM extraction: Connection cannot be verified with default trusted CAs. Please provide correct path to a CA_BUNDLE file or directory with certificates of trusted CAs. Error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
# Error occurred during LLM extraction: Connection cannot be verified with default trusted CAs. Please provide correct path to a CA_BUNDLE file or directory with certificates of trusted CAs. Error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
# Error occurred during LLM extraction: Connection cannot be verified with default trusted CAs. Please provide correct path to a CA_BUNDLE file or directory with certificates of trusted CAs. Error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))






#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# import json
# import fitz
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Initialize LLM model
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

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

# # Function to extract text from the PDF
# def extract_text_from_pdf(pdf_path):
#     try:
#         with fitz.open(pdf_path) as doc:
#             text = ""
#             for page in doc:
#                 text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"Error occurred while extracting text from PDF: {str(e)}")
#         return None

# # Function to chunk text into manageable parts for the LLM model
# def chunk_text(text, chunk_size=1000):
#     words = text.split()
#     chunks = []
#     current_chunk = []

#     for word in words:
#         current_chunk.append(word)
#         if len(" ".join(current_chunk)) >= chunk_size:
#             chunks.append(" ".join(current_chunk))
#             current_chunk = []

#     if current_chunk:
#         chunks.append(" ".join(current_chunk))

#     return chunks

# # Function to extract specific information using LLM model
# def extract_specific_info(llm_model, text_chunks, prompt_template):
#     extracted_info = []
#     for chunk in text_chunks:
#         try:
#             prompt = prompt_template.format(text=chunk)
#             response = llm_model.invoke([prompt])
#             extracted_info.append(response[0].strip())
#         except Exception as e:
#             print(f"Error occurred during LLM extraction: {str(e)}")
#             extracted_info.append(None)
#     return extracted_info

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Chunk the text to stay within the token limit
#     text_chunks = chunk_text(pdf_text, chunk_size=1000)

#     # Define prompts for specific information
#     prompts = {
#         "General Information": {
#             "Chemical Name": "Extract the Chemical Name from the following text:\n\n{text}\n\n",
#             "CAS Number": "Extract the CAS Number from the following text:\n\n{text}\n\n",
#             "EINECS Number": "Extract the EINECS Number from the following text:\n\n{text}\n\n"
#         },
#         "Hazards": {
#             "Acute Toxicity": "Extract the Acute Toxicity information from the following text:\n\n{text}\n\n",
#             "Skin Irritation": "Extract the Skin Irritation information from the following text:\n\n{text}\n\n",
#             "Eye Irritation": "Extract the Eye Irritation information from the following text:\n\n{text}\n\n"
#         },
#         "Emergency Response": {
#             "First-aid Measures": "Extract the First-aid Measures from the following text:\n\n{text}\n\n",
#             "Firefighting Measures": "Extract the Firefighting Measures from the following text:\n\n{text}\n\n",
#             "Accidental Release Measures": "Extract the Accidental Release Measures from the following text:\n\n{text}\n\n"
#         },
#         "Transport Information": {
#             "UN Number": "Extract the UN Number from the following text:\n\n{text}\n\n",
#             "Proper Shipping Name": "Extract the Proper Shipping Name from the following text:\n\n{text}\n\n",
#             "Transport Hazard Class": "Extract the Transport Hazard Class from the following text:\n\n{text}\n\n"
#         },
#         "Regulatory Information": {
#             "OSHA Classification": "Extract the OSHA Classification from the following text:\n\n{text}\n\n",
#             "European CLP Regulation": "Extract the European CLP Regulation from the following text:\n\n{text}\n\n",
#             "Canadian WHMIS Classification": "Extract the Canadian WHMIS Classification from the following text:\n\n{text}\n\n"
#         },
#         "Miscellaneous": {
#             "Chemical Structure": "Extract the Chemical Structure from the following text:\n\n{text}\n\n",
#             "Synonyms": "Extract the Synonyms from the following text:\n\n{text}\n\n",
#             "Trade Names": "Extract the Trade Names from the following text:\n\n{text}\n\n"
#         }
#     }

#     # Extract information for each section
#     section_info = {}

#     # General Information section
#     general_info = {}
#     for key, prompt_template in prompts["General Information"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         general_info[key] = extracted_info
#     section_info["General Information"] = general_info

#     # Hazards section
#     hazards_info = {}
#     for key, prompt_template in prompts["Hazards"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         hazards_info[key] = extracted_info
#     section_info["Hazards"] = hazards_info

#     # Emergency Response section
#     emergency_response_info = {}
#     for key, prompt_template in prompts["Emergency Response"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         emergency_response_info[key] = extracted_info
#     section_info["Emergency Response"] = emergency_response_info

#     # Transport Information section
#     transport_info = {}
#     for key, prompt_template in prompts["Transport Information"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         transport_info[key] = extracted_info
#     section_info["Transport Information"] = transport_info

#     # Regulatory Information section
#     regulatory_info = {}
#     for key, prompt_template in prompts["Regulatory Information"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         regulatory_info[key] = extracted_info
#     section_info["Regulatory Information"] = regulatory_info

#     # Miscellaneous section
#     miscellaneous_info = {}
#     for key, prompt_template in prompts["Miscellaneous"].items():
#         extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
#         miscellaneous_info[key] = extracted_info
#     section_info["Miscellaneous"] = miscellaneous_info

#     # Construct JSON output with separate curly braces for each section
#     json_output = json.dumps(section_info, indent=4)
#     print(json_output)
# else:
#     print("No text extracted from the PDF.")




# Error occurred during LLM extraction: Connection cannot be verified with default trusted CAs. Please provide correct path to a CA_BUNDLE file or directory with certificates of trusted CAs. Error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
# Error occurred during LLM extraction: Connection cannot be verified with default trusted CAs. Please provide correct path to a CA_BUNDLE file or directory with certificates of trusted CAs. Error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
# Error occurred during LLM extraction: Connection cannot be verified with default trusted CAs. Please provide correct path to a CA_BUNDLE file or directory with certificates of trusted CAs. Error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import json
# import fitz
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

# # Initialize LLM model
# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

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

# # Function to extract text from the PDF
# def extract_text_from_pdf(pdf_path):
#     try:
#         with fitz.open(pdf_path) as doc:
#             text = ""
#             for page in doc:
#                 text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"Error occurred while extracting text from PDF: {str(e)}")
#         return None

# # Function to extract information from a specific section using LLM model
# def extract_section_info(llm_model, section_text):
#     try:
#         # Process section text through LLM model to extract information
#         response = llm_model.invoke(section_text)
#         extracted_info = response.strip()
#         return extracted_info
#     except Exception as e:
#         print(f"Error occurred during LLM extraction: {str(e)}")
#         return None

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Initialize main section info dictionary
#     section_info = {}

#     # General Information section
#     general_info_section_text = "Text extracted from the General Information section"
#     general_info = {"General Information": extract_section_info(llama, general_info_section_text)}
#     section_info.update(general_info)

#     # Hazards section
#     hazards_section_text = "Text extracted from the Hazards section"
#     hazards_info = {"Hazards": extract_section_info(llama, hazards_section_text)}
#     section_info.update(hazards_info)

#     # Emergency Response section
#     emergency_response_section_text = "Text extracted from the Emergency Response section"
#     emergency_response_info = {"Emergency Response": extract_section_info(llama, emergency_response_section_text)}
#     section_info.update(emergency_response_info)

#     # Transport Information section
#     transport_info_section_text = "Text extracted from the Transport Information section"
#     transport_info = {"Transport Information": extract_section_info(llama, transport_info_section_text)}
#     section_info.update(transport_info)

#     # Regulatory Information section
#     regulatory_info_section_text = "Text extracted from the Regulatory Information section"
#     regulatory_info = {"Regulatory Information": extract_section_info(llama, regulatory_info_section_text)}
#     section_info.update(regulatory_info)

#     # Miscellaneous section
#     miscellaneous_section_text = "Text extracted from the Miscellaneous section"
#     miscellaneous_info = {"Miscellaneous": extract_section_info(llama, miscellaneous_section_text)}
#     section_info.update(miscellaneous_info)

#     # Construct JSON output with separate curly braces for each section
#     json_output = json.dumps(section_info, indent=4)
#     print(json_output)
# else:
#     print("No text extracted from the PDF.")



# Error occurred during LLM extraction: Connection cannot be verified with default trusted CAs. Please provide correct path to a CA_BUNDLE file or directory with certificates of trusted CAs. Error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
# Error occurred during LLM extraction: Connection cannot be verified with default trusted CAs. Please provide correct path to a CA_BUNDLE file or directory with certificates of trusted CAs. Error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
# Error occurred during LLM extraction: Connection cannot be verified with default trusted CAs. Please provide correct path to a CA_BUNDLE file or directory with certificates of trusted CAs. Error: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

#----------------------------------------------------------------------------------------------------------------------------------------------------

# import json
# import fitz
# from langchain_ibm import WatsonxLLM
# from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes


# credentials = {
#     "url": "https://us-south.ml.cloud.ibm.com",
#     "apikey": "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# }

# project_id = "8c02f540-b106-4311-b7a9-4afde1ddb4bb"

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
#         with fitz.open(pdf_path) as doc:
#             text = ""
#             for page in doc:
#                 text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"Error occurred while extracting text from PDF: {str(e)}")
#         return None

# def chunk_text(text, chunk_size=1000):
#     words = text.split()
#     chunks = []
#     current_chunk = []

#     for word in words:
#         current_chunk.append(word)
#         if len(" ".join(current_chunk)) >= chunk_size:
#             chunks.append(" ".join(current_chunk))
#             current_chunk = []

#     if current_chunk:
#         chunks.append(" ".join(current_chunk))

#     return chunks


# def extract_specific_info(llm_model, text_chunks, prompt_template):
#     extracted_info = []
#     for chunk in text_chunks:
#         try:
#             prompt = prompt_template.format(text=chunk)
#             response = llm_model.invoke([prompt])
#             extracted_info.append(response[0].strip())
#         except Exception as e:
#             print(f"Error occurred during LLM extraction: {str(e)}")
#             extracted_info.append(None)
#     return extracted_info


# pdf_path = "GHS Rev10e.pdf"


# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
  
#     text_chunks = chunk_text(pdf_text, chunk_size=1000)

   
#     prompts = {
#         "General Information": {
#             "Chemical name": "Extract the Chemical name from the following text:\n\n{text}\n\n",
#             "CAS number": "Extract the CAS number from the following text:\n\n{text}\n\n",
#             "EINECS number": "Extract the EINECS number from the following text:\n\n{text}\n\n",
#             "RTECS number": "Extract the RTECS number from the following text:\n\n{text}\n\n",
#             "Molecular formula": "Extract the Molecular formula from the following text:\n\n{text}\n\n",
#             "Molecular weight": "Extract the Molecular weight from the following text:\n\n{text}\n\n",
#             "Physical state": "Extract the Physical state (solid, liquid, gas) from the following text:\n\n{text}\n\n",
#             "Appearance": "Extract the Appearance from the following text:\n\n{text}\n\n",
#             "Odor": "Extract the Odor from the following text:\n\n{text}\n\n",
#             "pH": "Extract the pH from the following text:\n\n{text}\n\n",
#             "Melting point": "Extract the Melting point from the following text:\n\n{text}\n\n",
#             "Boiling point": "Extract the Boiling point from the following text:\n\n{text}\n\n",
#             "Flash point": "Extract the Flash point from the following text:\n\n{text}\n\n",
#             "Density": "Extract the Density from the following text:\n\n{text}\n\n",
#             "Solubility in water": "Extract the Solubility in water from the following text:\n\n{text}\n\n",
#             "Solubility in other solvents": "Extract the Solubility in other solvents from the following text:\n\n{text}\n\n",
#             "Vapor pressure": "Extract the Vapor pressure from the following text:\n\n{text}\n\n",
#             "Autoignition temperature": "Extract the Autoignition temperature from the following text:\n\n{text}\n\n",
#             "Decomposition temperature": "Extract the Decomposition temperature from the following text:\n\n{text}\n\n"
#         },
       
#     }

   
#     section_info = {}

#     for section, fields in prompts.items():
#         section_details = []
#         for field, prompt_template in fields.items():
#             extracted_info = extract_specific_info(llama, text_chunks, prompt_template)
          
#             joined_info = " ".join(info for info in extracted_info if info)
#             field_info = {field: joined_info}
#             section_details.append(field_info)
#         section_info[section] = section_details

   
#     json_output = json.dumps(section_info, indent=4)
#     print(json_output)
# else:
#     print("No text extracted from the PDF.")




# error


#------------------------------------------------------------------------------------------------------------------------------


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
#     words = text.split()
#     chunks = []
#     current_chunk = []
#     current_tokens = 0

#     for word in words:
#         word_tokens = len(word.split())
#         if current_tokens + word_tokens > max_tokens:
#             chunks.append(" ".join(current_chunk))
#             current_chunk = [word]
#             current_tokens = word_tokens
#         else:
#             current_chunk.append(word)
#             current_tokens += word_tokens

#     if current_chunk:
#         chunks.append(" ".join(current_chunk))

#     return chunks

# # Function to use the LLM to extract details
# def extract_details_with_llm(text_chunks, llama_model):
#     extracted_details = {
#         "Chemical name": "",
#         "CAS number": "",
#         "EINECS number": "",
#         "RTECS number": "",
#         "Molecular formula": "",
#         "Molecular weight": "",
#         "Physical state": "",
#         "Appearance": "",
#         "Odor": "",
#         "pH": "",
#         "Melting point": "",
#         "Boiling point": "",
#         "Flash point": "",
#         "Density": "",
#         "Solubility in water": "",
#         "Solubility in other solvents": "",
#         "Vapor pressure": "",
#         "Autoignition temperature": "",
#         "Decomposition temperature": ""
#     }

#     for chunk in text_chunks:
#         prompt = f"Extract the following chemical information from the text:\n{chunk}\n\n" \
#                  "General Information:\n" \
#                  "Chemical name\n" \
#                  "CAS number\n" \
#                  "EINECS number\n" \
#                  "RTECS number\n" \
#                  "Molecular formula\n" \
#                  "Molecular weight\n" \
#                  "Physical state (solid, liquid, gas)\n" \
#                  "Appearance\n" \
#                  "Odor\n" \
#                  "pH\n" \
#                  "Melting point\n" \
#                  "Boiling point\n" \
#                  "Flash point\n" \
#                  "Density\n" \
#                  "Solubility in water\n" \
#                  "Solubility in other solvents\n" \
#                  "Vapor pressure\n" \
#                  "Autoignition temperature\n" \
#                  "Decomposition temperature"
#         response = llama_model.invoke(prompt)

#         # Process the response and extract details
#         for key in extracted_details.keys():
#             if key in response:
#                 start_index = response.find(key) + len(key) + 1
#                 end_index = response.find('\n', start_index)
#                 extracted_details[key] = response[start_index:end_index].strip()

#     return extracted_details

# # Path to the PDF file
# pdf_path = "GHS Rev10e.pdf"

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)

# if pdf_text:
#     # Split text into chunks
#     text_chunks = split_text_into_chunks(pdf_text, max_tokens=1000)

#     # Use LLM to extract details
#     details = extract_details_with_llm(text_chunks, llama)
    
#     # Create JSON structure
#     response_json = {
#         "ChemicalDetails": details
#     }
    
#     # Print the extracted details in JSON format
#     print(json.dumps(response_json, indent=4))
# else:
#     print("No text extracted from the PDF.")



# error


