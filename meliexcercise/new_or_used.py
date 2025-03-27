import pandas as pd

from meliexcercise.classes.data_loader import DataLoader
from meliexcercise.classes.data_cleaner import DataCleaner
from meliexcercise.classes.feature_engineer import FeatureEngineer

ObjDataLoader = DataLoader(file_path="./data/raw/")

objJson = ObjDataLoader.load_data()

objDataCleaner = DataCleaner(data_set=objJson)

DatosLimpios = objDataCleaner.clean_data()

objTransformer = FeatureEngineer(data_set=DatosLimpios)

DatosTransformados = objTransformer.feature_engineer()

DatosTransformados.condition.value_counts()