import pandas as pd
import os

def controller(file):
    if is_exists_file(file):
        extension = os.path.splitext(file)
        extension = extension[1]
    
        if extension == ".csv":
            df = pd.read_csv(file) # Extract from CSV to a DF
        
        elif extension == ".xlsx":
            df = pd.read_excel(file) # Extract from XLSX to a DF
        
        elif extension == ".json":
            df = pd.read_json(file) # Extract from JSON to a DF
        
        else:
            print("[!] File Not Supported")
            return None
        
        return df

    else:
        return None


# is there an file?
def is_exists_file(file_path):
    return os.path.exists(file_path)