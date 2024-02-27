import pandas as pd
import os

# Extract from CSV to a DF
def csv_to_df(csv_path):

    if is_exists_file(csv_path):
        df = pd.read_csv(csv_path)
        return df
    else:
        return None 

def xlsx_to_df(xlsx_path):

    if is_exists_file(xlsx_path):
        df = pd.read_csv(xlsx_path)
        return df
    
    else:
        return None  


# is there an file?
def is_exists_file(file_path):
    return os.path.exists(file_path)