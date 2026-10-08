from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from schema.input import House
from models.predict_logic import predict


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the House Price Prediction API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def Predict(input_data : House):
    input_data = input_data.model_dump()

    predicted_value = predict(input_data)
    return JSONResponse(content={"predicted_price": predicted_value})

