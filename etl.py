import glob
import pandas as pd
from pandas import DataFrame
import xml.etree.ElementTree as ET
from datetime import datetime

# file paths available globaly
log_file: str = "log_file.txt"
target_file: str = "transformed_data.csv"

# constants available globaly
IN_TO_M: float = 0.0254 # const. for converting inches to meters
LB_TO_K: float = 0.45359237 # const. for converting pound to kilograms

def extract_from_csv(file_to_process: str) -> DataFrame:
    dataframe = pd.read_csv(file_to_process)
    
    return dataframe

def extract_from_json(file_to_process: str) -> DataFrame:
    dataframe = pd.read_json(file_to_process, lines=True)
    
    return dataframe

def extract_from_xml(file_to_process: str) -> DataFrame:
    dataframe = DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process) # read and parses XML file
    root = tree.getroot() # gets root element of XML tree, all <person> el.

    for person in root:
        name = person.find("name").text
        weight = float(person.find("weight").text)
        height = float(person.find("height").text)
        dataframe = pd.concat([dataframe, DataFrame([{
            "name": name,
            "height": height,
            "weight": weight
        }])], ignore_index=True)

    return dataframe

def extract() -> DataFrame:
    extracted_data: DataFrame = DataFrame(columns=['name', 'height', 'weight'])

    # process all CSV files except target file
    for csvfile in glob.glob("*.csv"):
        if csvfile != target_file:
            extracted_data = pd.concat([
                extracted_data, 
                DataFrame(extract_from_csv(csvfile))
            ], ignore_index=True)

     # process all JSON files
    for jsonfile in glob.glob("*.json"):
        extracted_data = pd.concat([
            extracted_data, 
            DataFrame(extract_from_json(jsonfile))
        ], ignore_index=True)

    # process all XML files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat([
            extracted_data,
            DataFrame(extract_from_xml(xmlfile))
        ], ignore_index=True)

    return extracted_data

def transform(data: DataFrame) -> DataFrame:
    data['height'] = round(data.height * IN_TO_M, 2)

    data['weight'] = round(data.weight * LB_TO_K, 2)

    return data

def load_data(target_file: str, transformed_data: DataFrame) -> None:
    transformed_data.to_csv(target_file)

def log_progress(message) -> None:
    timestamp_format = '%d-%h-%Y-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open(log_file, "a") as file:
        file.write(timestamp + ', ' + message + '\n')

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 