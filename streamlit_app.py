import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("models/model.pkl")  # change path if needed

st.title("🧠 MedScan Classifier")

st.write("Enter scan data as numbers separated by commas (e.g., `5.2, 3.1, 1.4, 0.2`)")

input_str = st.text_input("Enter input features:")

if st.button("Predict"):
    try:
        features = np.array([float(x) for x in input_str.split(",")]).reshape(1, -1)
        prediction = model.predict(features)
        st.success(f"✅ Prediction: {prediction[0]}")
    except Exception as e:
        st.error("❌ Error: Invalid input. Please enter valid numbers separated by commas.")
