
from meliexcercise.classes.data_loader import DataLoader
from meliexcercise.classes.data_cleaner import DataCleaner

import os
import numpy as np
import pandas as pd
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
warnings.filterwarnings("ignore")
pd.set_option("display.max_rows",None)
from sklearn import preprocessing
import matplotlib
matplotlib.use('TkAgg')
matplotlib.style.use('ggplot')
from sklearn.preprocessing import LabelEncoder

class EDA():

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):

        instanciaDataLoader = DataLoader(file_path=self.file_path)
        objJson = instanciaDataLoader.load_data()

        # Create an instance of the DataCleaner class
        instanciaDataCleaner = DataCleaner(data_set=objJson)
        self.DatosLimpios = instanciaDataCleaner.clean_data()

        return self.DatosLimpios

    def descriptivas(self):
        if self.DatosLimpios is None:
            raise ValueError("Primero debes ejecutar el método 'load' para cargar y limpiar los datos.")

        return self.DatosLimpios.describe()
