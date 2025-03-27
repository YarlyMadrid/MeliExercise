"""
Exercise description
--------------------

Description:
In the context of Mercadolibre's Marketplace an algorithm is needed to predict if an item listed in the markeplace is new or used.

Your tasks involve the data analysis, designing, processing and modeling of a machine learning solution
to predict if an item is new or used and then evaluate the model over held-out test data.

To assist in that task a dataset is provided in `MLA_100k_checked_v3.jsonlines` and a function to read that dataset in `build_dataset`.

For the evaluation, you will use the accuracy metric in order to get a result of 0.86 as minimum.
Additionally, you will have to choose an appropiate secondary metric and also elaborate an argument on why that metric was chosen.

The deliverables are:
--The file, including all the code needed to define and evaluate a model.
--A document with an explanation on the criteria applied to choose the features,
  the proposed secondary metric and the performance achieved on that metrics.
  Optionally, you can deliver an EDA analysis with other formart like .ipynb

"""


import pandas as pd

from meliexcercise.classes.dataset_builder import DatasetBuilder

if __name__ == "__main__":
    print("Loading dataset...")
    # Train and test data following sklearn naming conventions
    # X_train (X_test too) is a list of dicts with information about each item.
    # y_train (y_test too) contains the labels to be predicted (new or used).
    # The label of X_train[i] is y_train[i].
    # The label of X_test[i] is y_test[i].
    ruta = "C:/Users/ykmi2241/Documents/Proyectos Pycharm/MeliExercise/data/raw/"

    instanciaDataSetBuilder = DatasetBuilder(file_path = ruta)

    X_train, y_train, X_test, y_test = instanciaDataSetBuilder.build_dataset()

    print(X_train)






