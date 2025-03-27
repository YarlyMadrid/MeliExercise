import pandas as pd

class DataCleaner():

    def __init__(self,data_set):
        self.data_set = data_set

    def clean_data(self):

        # Add shipping informatio
        df_shipping = self.data_set['shipping'].apply(pd.Series)
        self.data_set = pd.concat([self.data_set, df_shipping], axis=1)


