import pandas as pd
import numpy as np

# Preprocessing
from sklearn.preprocessing import OneHotEncoder, StandardScaler

class FeatureEngineer():

    def __init__(self,data_set):
        self.data_set = data_set

    def feature_engineer(self):

        # Encode Condition Variable
        self.data_set['condition'] = self.data_set['condition'].map({'new': 1, 'used': 0})

        # Create Sold Ratio
        self.data_set['sold_ratio'] = self.data_set.apply(
            lambda x: x['sold_quantity'] / x['initial_quantity'] if x['initial_quantity'] > 0 else 0,
            axis=1
        )

        # Create Available Ratio
        # self.data_set['available_ratio'] = self.data_set.apply(
        #     lambda x: x['available_quantity'] / x['initial_quantity'] if x['initial_quantity'] > 0 else 0,
        #     axis=1
        # )

        # Logarithmic transformations
        self.data_set['price_log'] = np.log1p(self.data_set['price'])
        # self.data_set['sold_log'] = np.log1p(self.data_set['sold_quantity'])

        data_modelo = self.data_set[["condition","listing_type_id_final","initial_quantity","sold_quantity",
                                    "available_quantity","sold_ratio","price_log","count_seller_id"]]

        # Set numeric columns
        columnas_numericas = ["initial_quantity", "sold_quantity",
                              "available_quantity", "sold_ratio",
                              "price_log","count_seller_id"]

        # Set categorical columns
        columnas_categoricas = ["listing_type_id_final"]

        # Separate the subsets
        X_numericas = data_modelo[columnas_numericas]
        X_categoricas = data_modelo[columnas_categoricas]

        # Scaling numeric variables
        scaler = StandardScaler()
        X_numericas_scaled = scaler.fit_transform(X_numericas)

        # Coding categorical variables
        encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
        X_categoricas_encoded = encoder.fit_transform(X_categoricas)

        # Get the names of the encoded columns
        columnas_categoricas_encoded = encoder.get_feature_names_out(columnas_categoricas)

        # Create DataFrames with the results
        df_numericas_scaled = pd.DataFrame(X_numericas_scaled, columns=columnas_numericas, index=data_modelo.index)
        df_categoricas_encoded = pd.DataFrame(X_categoricas_encoded, columns=columnas_categoricas_encoded,
                                              index=data_modelo.index)

        # Concat all transformed data into a new DataFrame
        X_transformado = pd.concat([df_numericas_scaled, df_categoricas_encoded], axis=1)

        # Final Data
        data_set_transformado = pd.concat([X_transformado, data_modelo["condition"]], axis=1)

        return data_set_transformado
