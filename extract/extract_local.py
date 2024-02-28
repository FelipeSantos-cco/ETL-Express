import pandas as pd
import os

def controller(file):
    if is_exists_file(file):
        extension = os.path.splitext(file)
        extension = extension[1]
    
        if extension == ".csv":
            return csv_to_df(file)
        
        elif extension == ".xlsx":
            return xlsx_to_df(file)
        
        elif extension == ".json":
            return json_to_df(file)
        
        else:
            print("[!] File Not Supported")

    else:
        return None

# Extract from CSV to a DF
def csv_to_df(csv_path):

    if is_exists_file(csv_path):
        df = pd.read_csv(csv_path)
        return df
    else:
        return None 

# Extract from XLSX to a DF
def xlsx_to_df(xlsx_path):

    if is_exists_file(xlsx_path):
        df = pd.read_excel(xlsx_path)
        return df
    
    else:
        return None  

# Extract from JSON to a DF
def json_to_df(json_path):
    
    if is_exists_file(json_path):
        return  pd.read_json(json_path)
        
    else:
        return None  

# is there an file?
def is_exists_file(file_path):
    return os.path.exists(file_path)