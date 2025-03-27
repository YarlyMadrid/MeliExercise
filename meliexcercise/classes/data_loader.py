import pandas as pd

class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        jsonObj = pd.read_json(path_or_buf=self.file_path + "MLA_100k_checked_v3.jsonlines", lines=True)
        return jsonObj



