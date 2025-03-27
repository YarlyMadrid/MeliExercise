from meliexcercise.classes.data_loader import DataLoader
from meliexcercise.classes.data_cleaner import DataCleaner
from meliexcercise.classes.feature_engineer import FeatureEngineer

class DatasetBuilder():

    def __init__(self, file_path):
        self.file_path = file_path

    def build_dataset(self):
        # Create an instance of the DataLoader class
        instanciaDataLoader = DataLoader(file_path=self.file_path)
        objJson = instanciaDataLoader.load_data()

        # Create an instance of the DataCleaner class
        instanciaDataCleaner = DataCleaner(data_set=objJson)
        DatosLimpios = instanciaDataCleaner.clean_data()

        # Create an instance of the FeatureEngineer class
        instanciaFeatureEngineer = FeatureEngineer(data_set=DatosLimpios)
        DatosTransformados = instanciaFeatureEngineer.feature_engineer()

        N = -10000
        X_train = DatosTransformados[:N].drop(columns=['condition'])
        X_test = DatosTransformados[N:].drop(columns=['condition'])
        y_train = DatosTransformados[:N]["condition"]
        y_test = DatosTransformados[N:]["condition"]

        return X_train, y_train, X_test, y_test

