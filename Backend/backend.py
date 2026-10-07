from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from pydantic import BaseModel ,Field 
from typing import Annotated ,Literal 
import pickle
import pandas as pd

app = FastAPI()
preprocessor = pickle.load(open("models/preprocessor.pkl", "rb"))
model = pickle.load(open("models/model.pkl", "rb"))


class House(BaseModel):
    City : Annotated[Literal["Hyderabad" , "Bangalore","Pune" ,"Mumbai"],Field(...,description="city of the user from Hyderabad Bangalore Pune  Mumbai")]
    Locality_Tier : Annotated[Literal["Mid", "Budget" ,"Premium"] ,Field(...,description="locality tier of the house ")]
    Furnishing : Annotated[Literal["Semi-Furnished" , "Unfurnished" ,"Fully-Furnished"],Field(...,description="furnishing status of the house")]
    BHK : Annotated[int , Field(...,gt = 0 , lt = 7, description="bhk of the house ")]
    Bathrooms : Annotated[int , Field(..., gt =0 ,description= "no of bathrooms in the house")]
    Super_Area_sqft: Annotated[float, Field(..., gt=0, description="super area of the house in square feet")]
    Carpet_Area_sqft: Annotated[float, Field(..., gt=0, description="carpet area of the house in square feet")]
    Total_Floors: Annotated[int, Field(..., gt=0, description="total number of floors in the building")]
    Floor_No: Annotated[int, Field(..., ge=0,  description="floor number of the house")]
    Property_Age_years: Annotated[int, Field(..., ge=0, description="age of the property in years")]
    Parking: Annotated[int, Field(..., ge=0, description="number of parking spaces")]
    Lift: Annotated[Literal[0,1], Field(..., description="lift availability :1 for yes, 0 for no")]
    Gated_Society: Annotated[Literal[0, 1], Field(..., description="gated society: 1 for yes, 0 for no")]
    Distance_to_Metro_km: Annotated[float, Field(..., ge=0, description="distance to metro in kilometers")]
    Distance_to_CityCenter_km: Annotated[float, Field(..., ge=0, description="distance to city center in kilometers")]
    Nearby_School_km: Annotated[float, Field(..., ge=0, description="distance to nearby school in kilometers")]
    Nearby_Hospital_km: Annotated[float, Field(..., ge=0, description="distance to nearby hospital in kilometers")]
    Crime_Rate_Index: Annotated[float, Field(..., ge=0, description="crime rate index of the locality")]


@app.post("/predict")
def Predict(input_data : House):
    input_data = input_data.model_dump()

    df = pd.DataFrame([input_data])
    trans_data = preprocessor.transform(df)
    predicted_value = model.predict(trans_data)[0]

    return JSONResponse(content={"predicted_price": predicted_value})

