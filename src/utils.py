import os
import sys
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV # Import GridSearchCV
from src.logger import logging # Import logging


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
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for model_name, model_instance in models.items():
            logging.info(f"Evaluating model: {model_name}")
            parameters = param.get(model_name, {}) # Use .get() for safety, default to empty dict

            if parameters:
                logging.info(f"Performing GridSearchCV for {model_name} with parameters: {parameters}")
                # Initialize GridSearchCV with the unfitted model instance and parameters
                gs = GridSearchCV(model_instance, parameters, cv=3, n_jobs=-1, verbose=0)
                gs.fit(X_train, y_train) # GridSearchCV will fit the best model
                
                best_model = gs.best_estimator_ # Get the best fitted model from GridSearchCV
                logging.info(f"Best parameters for {model_name}: {gs.best_params_}")
            else:
                logging.info(f"No GridSearchCV parameters for {model_name}. Fitting directly.")
                best_model = model_instance
                best_model.fit(X_train, y_train) # Fit the model directly if no grid search

            # Make predictions using the best_model
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            # Calculamos el R2 score para entrenamiento y prueba
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_score  # Store the test score
            logging.info(f"Model {model_name} - Train R2: {train_score:.4f}, Test R2: {test_score:.4f}")

        return report

    except Exception as e:
        raise CustomException(e, sys)