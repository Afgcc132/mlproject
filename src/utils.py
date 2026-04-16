import os
import sys
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        # Creamos la carpeta si no existe
        os.makedirs(dir_path, exist_ok=True)

        # Guardamos el objeto en modo 'wb' (write binary)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(X_train, y_train)  # Entrenamos el modelo

            # Hacemos predicciones
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Calculamos el R2 score para entrenamiento y prueba
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_score  # Guardamos solo el score de prueba

        return report

    except Exception as e:
        raise CustomException(e, sys)