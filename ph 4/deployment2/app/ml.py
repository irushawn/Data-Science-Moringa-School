"""
ML Model loading and prediction logic
"""

import joblib
import numpy as np
from schemas import IrisInput

model = joblib.load("iris_model.joblib")

def predict_iris(data: IrisInput):
    features = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])
    prediction = model.predict(features)
    return {"predicted_class": int(prediction[0])}
