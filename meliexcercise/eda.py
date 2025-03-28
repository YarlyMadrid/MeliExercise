# Librerias
from meliexcercise.classes.exploration import EDA
ruta = '././data/raw/'
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

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

# Matriz de correlación
matriz = instanciaEDA.correlacion()

# Variable objetivo

# Crear el gráfico
ax = dataset["condition"].value_counts().plot(kind='bar')

# Agregar etiquetas a cada barra
for p in ax.patches:
    ax.annotate(
        str(p.get_height()),               # texto de la etiqueta
        (p.get_x() + p.get_width() / 2, p.get_height()),  # posición (x, y)
        ha='center', va='bottom'          # alineación horizontal y vertical
    )

# Etiquetas y título opcionales
plt.xlabel('Condición')
plt.ylabel('Cantidad')
plt.title('Distribución de Condición')

plt.show()