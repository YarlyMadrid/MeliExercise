import pandas as pd
import numpy as np

class DataCleaner():

    def __init__(self,data_set):
        self.data_set = data_set

    def clean_data(self):

        # Add shipping information
        df_shipping = self.data_set['shipping'].apply(pd.Series)
        self.data_set = pd.concat([self.data_set, df_shipping], axis=1)

        # Add seller id information
        df_seller_id = pd.DataFrame(self.data_set.seller_id.value_counts()).reset_index().rename(columns={'count': 'count_seller_id'})
        self.data_set = self.data_set.merge(df_seller_id, on = "seller_id")

        # Clean listing type id
        condiciones_type = [self.data_set['listing_type_id'].str.contains('bronze', case=False, na=False),
                            self.data_set['listing_type_id'].str.contains('free', case=False, na=False),
                            self.data_set['listing_type_id'].str.contains('silver', case=False, na=False),
                            self.data_set['listing_type_id'].str.contains('gold', case=False, na=False)]

        opciones_type = ["bronze", "free", "silver", "gold"]

        self.data_set["listing_type_id_final"] = np.select(condiciones_type, opciones_type, default="Otro")

        # Clean outliers: initial_quantity and condition variables
        self.data_set = self.data_set[~((self.data_set['initial_quantity'] > 9990) & (self.data_set['condition'] == 'used'))]

        # Clean outlier: price variable
        self.data_set = self.data_set[self.data_set['price'] < 4000000]

        return self.data_set


