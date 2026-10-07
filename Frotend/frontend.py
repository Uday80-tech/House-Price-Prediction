import streamlit as st
import pandas as pd
import requests

url ="http://127.0.0.1:8000/predict"

st.title("House Price Prediction")

st.write("this is a simple linear regression model project with fastapi integration ")

c1 , c2 ,c3 = st.columns(3)

City = c1.selectbox("Select City", ["Hyderabad", "Bangalore", "Pune", "Mumbai"])
Locality_Tier = c2.selectbox("Select Locality Tier", ["Mid", "Budget", "Premium"])
Furnishing = c3.selectbox("Select Furnishing", ["Semi-Furnished", "Unfurnished", "Fully-Furnished"])
BHK = c1.number_input("Enter BHK", min_value=1, max_value=6, step=1)
Bathrooms = c2.number_input("Enter Number of Bathrooms", min_value=1 , max_value= 6 , step=1)
Super_Area_sqft = c3.number_input("Enter Super Area in sqft", min_value=100.0, max_value=10000.0, step=10.0)
Carpet_Area_sqft = c1.number_input("Enter Carpet Area in sqft", min_value=100.0, max_value=10000.0, step=10.0)
Total_Floors = c2.number_input("Enter Total Floors", min_value=1, max_value=100, step=1)
Floor_No = c3.number_input("Enter Floor Number", min_value=0, max_value=100, step=1)
Property_Age_years = c1.number_input("Enter Property Age in years", min_value=0, max_value=100, step=1)
Parking = c2.number_input("Enter Number of Parking Spaces", min_value=0, max_value=10, step=1)
Lift = 1 if c3.selectbox("Is there a Lift?", ["Yes", "No"]) == "Yes" else 0
Gated_Society = 1 if c1.selectbox("Is it a Gated Society?", ["Yes", "No"]) == "Yes" else 0
Distance_to_Metro_km = c2.number_input("Enter Distance to Metro in km", min_value=0.0, max_value=100.0, step=0.1)
Distance_to_CityCenter_km = c3.number_input("Enter Distance to City Center in km", min_value=0.0, max_value=100.0, step=0.1)
Nearby_School_km = c1.number_input("Enter Distance to Nearby School in km", min_value=0.0, max_value=100.0, step=0.1)
Nearby_Hospital_km = c2.number_input("Enter Distance to Nearby Hospital in km", min_value=0.0, max_value=100.0, step=0.1)
Crime_Rate_Index = c3.number_input("Enter Crime Rate Index", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Predict Price"):
    input_data = {
        "City": City,
        "Locality_Tier": Locality_Tier,
        "Furnishing": Furnishing,
        "BHK": BHK,
        "Bathrooms": Bathrooms,
        "Super_Area_sqft": Super_Area_sqft,
        "Carpet_Area_sqft": Carpet_Area_sqft,
        "Total_Floors": Total_Floors,
        "Floor_No": Floor_No,
        "Property_Age_years": Property_Age_years,
        "Parking": Parking,
        "Lift": Lift,
        "Gated_Society": Gated_Society,
        "Distance_to_Metro_km": Distance_to_Metro_km,
        "Distance_to_CityCenter_km": Distance_to_CityCenter_km,
        "Nearby_School_km": Nearby_School_km,
        "Nearby_Hospital_km": Nearby_Hospital_km,
        "Crime_Rate_Index": Crime_Rate_Index
    }

    response = requests.post(url, json=input_data)
    if response.status_code == 200:
        predicted_price = response.json()["predicted_price"]
        st.success(f"The predicted price of the house is: {predicted_price}")
    else:
        st.error("Error in prediction. Please try again.")