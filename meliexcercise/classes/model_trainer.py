import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

from lightgbm import LGBMClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

class ModelTrainer():

    def __init__(self,X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test

    def initial_train(self):

        # Dictionary with the models to train
        modelos = {
            "Logistic Regression": LogisticRegression(max_iter=1000, random_state=950),
            "Random Forest": RandomForestClassifier(random_state=950),
            "Gradient Boosting": GradientBoostingClassifier(random_state=950),
            "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=950),
            "LightGBM": LGBMClassifier(random_state=950)
        }

        # Entrenar y evaluar cada modelo

        resultados = []

        for nombre, modelo in modelos.items():
            modelo.fit(self.X_train, self.y_train)
            y_pred = modelo.predict(self.X_test)
            acc = accuracy_score(self.y_test, y_pred)
            prec = precision_score(self.y_test, y_pred)
            resultados.append(
                {
                    "Modelo":nombre,
                    "Accuracy": acc,
                    "Precision": prec,
                    "Error tipo 1": 1 - prec
                }
            )
        return pd.DataFrame(resultados)

    def tuning_XGBoost(self, n_iter=30, cv=5, scoring='accuracy', random_state=950):

        param_dist = {
            'n_estimators': [100, 200, 300, 500],
            'max_depth': [3, 4, 5, 6, 7, 10],
            'learning_rate': [0.01, 0.05, 0.1, 0.2],
            'subsample': [0.6, 0.7, 0.8, 1.0],
            'colsample_bytree': [0.6, 0.7, 0.8, 1.0],
            'gamma': [0, 0.1, 0.2, 0.5, 1],
            'reg_alpha': [0, 0.01, 0.1, 1],
            'reg_lambda': [0.1, 0.5, 1, 2]
        }

        xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=950)

        search = RandomizedSearchCV(
            estimator=xgb,
            param_distributions=param_dist,
            n_iter=n_iter,
            cv=cv,
            scoring=scoring,
            verbose=1,
            n_jobs=-1,
            random_state=random_state
        )

        search.fit(self.X_train, self.y_train)

        self.best_model = search.best_estimator_

        resultados = {
            "best_params:": search.best_params_,
            "scoring": search.best_score_
        }

        return resultados,  search.best_params_

    def plot_feature_importance(self, top_n = 20):

        if not hasattr(self, 'best_model'):
            raise ValueError("Primero debes ejecutar el método 'tuning' para obtener el mejor modelo.")

        model = self.best_model

        if not hasattr(model, 'feature_importances_'):
            raise ValueError(
                "El modelo no tiene atributo 'feature_importances_' (¿es un modelo compatible como XGBoost o RandomForest?).")

        # Get variables name
        feature_names = (self.X_train.columns
                         if hasattr(self.X_train, 'columns')
                         else [f'feature_{i}' for i in range(self.X_train.shape[1])])

        importancias = model.feature_importances_
        importancia_df = pd.DataFrame({
            'Variable': feature_names,
            'Importancia': importancias
        }).sort_values(by='Importancia', ascending=False).head(top_n)

        # Graficar
        plt.figure(figsize=(10, 6))
        plt.barh(importancia_df['Variable'][::-1], importancia_df['Importancia'][::-1])
        plt.xlabel("Importancia")
        plt.title("Importancia de las variables (top {})".format(top_n))
        plt.tight_layout()
        plt.show()





