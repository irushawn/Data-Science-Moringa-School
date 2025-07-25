from fastapi import FastAPI
from schemas import IrisInput
from ml import predict_iris

app = FastAPI()

@app.post("/predict")
def predict(input_data: IrisInput):
    return predict_iris(input_data)
