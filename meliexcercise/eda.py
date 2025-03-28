# Librerias
from meliexcercise.classes.exploration import EDA
ruta = "C:/Users/ykmi2241/Documents/Proyectos Pycharm/MeliExercise/data/raw/"

instanciaEDA = EDA(file_path=ruta)

dataset = instanciaEDA.load()

descriptivas = instanciaEDA.descriptivas()

print(descriptivas)

# Descriptivas generales
descriptivas = descriptivas[['price','initial_quantity','sold_quantity', 'available_quantity']]

# Descriptivas agrupadas por condición
agrupacion_condition = dataset.groupby('condition')[['price','initial_quantity','sold_quantity', 'available_quantity']].agg([
        ('Q1', lambda x: x.quantile(0.25)),
        ('Mediana', 'median'),
        ('Promedio', 'mean'),
        ('Desviación', 'std'),
        ('Q3', lambda x: x.quantile(0.75))
    ])

agrupacion_condition = dataset.groupby('condition')[['price']].agg([
        ('Q1', lambda x: x.quantile(0.25)),
        ('Mediana', 'median'),
        ('Promedio', 'mean'),
        ('Desviación', 'std'),
        ('Q3', lambda x: x.quantile(0.75))
    ])