import pandas as pd

class DataExt:
    def __init__(self,file_path:str):
        self.file_path = file_path

    def fetch_text(self,separator:str):
        df = pd.read_csv(self.file_path, sep=separator)
        print(df.head())
    def fetch_json(self):
       df = pd.read_json(self.file_path)
       print(df.head())
    def fetch_parquet(self):
        df = pd.read_parquet(self.file_path)
        print(df.head())
obj = DataExt("data.csv")
obj.fetch_text(",")