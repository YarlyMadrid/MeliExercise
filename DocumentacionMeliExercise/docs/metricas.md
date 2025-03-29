# Metricas

## Métrica inicial

### Accuracy

Para el desarrollo del ejercicio se propuso trabajar con el Accuracy y alcanzar un minimo de 0.86. 

Las siguientes fueron las métricas calculadas con los modelos iniciales

| Modelo              | Accuracy | Precision | Error tipo 1 |
|---------------------|----------|-----------|--------------|
| Logistic Regression | 0.7864   | 0.754514  | 0.245486     |
| Random Forest       | 0.8467   | 0.878444  | 0.121556     |
| Gradient Boosting   | 0.8390   | 0.846730  | 0.153270     |
| XGBoost             | 0.8569   | 0.865282  | 0.134718     |
| LightGBM            | 0.8540   | 0.860168  | 0.139832     |

## Metrica Adicional

### Error tipo 1

Para la segunda metrica se escogió el error tipo 1 (1-precision o tasa de falsos positivos), que ocurre cuando el modelo predice la clase positiva (nuevo) pero en realidad es negativa (usado).

#### ¿Por qué es importante?

En el contexto de Mercado Libre, lo más importante es garantizar una excelente experiencia para los usuarios al momento de realizar una compra. Un error crítico sería clasificar un producto como nuevo cuando en realidad es usado, generando al final posible frustración, pérdida de confianza y reclamos por parte del comprador.
Este tipo de error corresponde a un falso positivo (Error Tipo I), donde el modelo predice que el artículo es nuevo pero en realidad no lo es. Para minimizar este riesgo, es fundamental no solo enfocarse en la exactitud general del modelo, sino también en que esta tasa sea mínima.

Aunque el error tipo 1 es minimo en el modelo de Random Forest, si se compara con el modelo XGBoost la diferencia es poca; y este último presenta un mejor Accuracy.
Se recomienda escoger el modelo XGBoost y continuar probando mejores variables e ir iterarando en los datos en el tiempo.

