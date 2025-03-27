from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

from lightgbm import LGBMClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

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
        for nombre, modelo in modelos.items():
            modelo.fit(self.X_train, self.y_train)
            y_pred = modelo.predict(self.X_test)
            acc = accuracy_score(self.y_test, y_pred)
            print(f"{nombre}: Accuracy = {acc:.4f}")










