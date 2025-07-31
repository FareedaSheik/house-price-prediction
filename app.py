import streamlit as st
from predictor import predict_price

st.title("🏠 House Price Prediction App")

# Input fields
overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
gr_liv_area = st.number_input("Above ground living area (sq ft)", 500, 5000, 1500)
garage_cars = st.selectbox("Garage capacity (cars)", [0, 1, 2, 3])
total_bsmt_sf = st.number_input("Basement area (sq ft)", 0, 3000, 800)
full_bath = st.selectbox("Number of Full Bathrooms", [1, 2, 3])
year_built = st.slider("Year Built", 1900, 2023, 2000)

if st.button("Predict Price"):
    features = [overall_qual, gr_liv_area, garage_cars, total_bsmt_sf, full_bath, year_built]
    result = predict_price(features)
    st.success(f"Estimated House Price: ₹{result:,.2f}")
