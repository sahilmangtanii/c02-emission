import streamlit as st
import pandas as pd
import joblib

# Load full pipeline (with preprocessing + model)
model = joblib.load('final_pipeline.pkl')

st.title("🚗 EmissionSense: CO₂ Emission Predictor")

# Input fields matching the original X columns
make = st.selectbox("Make", ["Toyota", "Honda", "Ford", "BMW"])  # Add all or most common
model_name = st.text_input("Model")
vehicle_class = st.selectbox("Vehicle Class", ["SUV", "Sedan", "Compact", "Pickup"])
engine_size = st.slider("Engine Size (L)", 1.0, 8.0, 2.0)
cylinders = st.slider("Cylinders", 2, 16, 4)
transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Hybrid", "Electric"])
fc_city = st.slider("Fuel Consumption City (L/100 km)", 1.0, 30.0, 10.0)
fc_hwy = st.slider("Fuel Consumption Hwy (L/100 km)", 1.0, 25.0, 7.0)
fc_comb = st.slider("Fuel Consumption Comb (L/100 km)", 1.0, 25.0, 8.0)
fc_mpg = st.slider("Fuel Consumption Comb (mpg)", 5, 100, 30)

# Prediction
if st.button("Predict CO₂ Emissions"):
    input_df = pd.DataFrame([{
        "Make": make,
        "Model": model_name,
        "Vehicle Class": vehicle_class,
        "Engine Size(L)": engine_size,
        "Cylinders": cylinders,
        "Transmission": transmission,
        "Fuel Type": fuel_type,
        "Fuel Consumption City (L/100 km)": fc_city,
        "Fuel Consumption Hwy (L/100 km)": fc_hwy,
        "Fuel Consumption Comb (L/100 km)": fc_comb,
        "Fuel Consumption Comb (mpg)": fc_mpg
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated CO₂ Emission: {prediction:.2f} g/km")