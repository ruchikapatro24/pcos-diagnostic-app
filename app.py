
import streamlit as st
import numpy as np
import joblib


model = joblib.load('pcos_model.pkl')

st.title("PCOS Diagnostic Tool 💡")
st.markdown("Enter the patient details to check the likelihood of PCOS.")

# Input fields
r_follicles = st.number_input("Follicle No. (Right Ovary)", min_value=0, max_value=50, value=10)
l_follicles = st.number_input("Follicle No. (Left Ovary)", min_value=0, max_value=50, value=10)

skin_darkening = st.radio("Skin Darkening?", ["No", "Yes"])
hair_growth = st.radio("Hair Growth?", ["No", "Yes"])
weight_gain = st.radio("Weight Gain?", ["No", "Yes"])

bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)

# Convert categorical inputs
skin_darkening_bin = 1 if skin_darkening == "Yes" else 0
hair_growth_bin = 1 if hair_growth == "Yes" else 0
weight_gain_bin = 1 if weight_gain == "Yes" else 0

# Predict button
if st.button("Predict PCOS"):
    input_data = np.array([[r_follicles, l_follicles, skin_darkening_bin, hair_growth_bin, weight_gain_bin, bmi]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of PCOS Detected")
    else:
        st.success("✅ Low Risk of PCOS Detected")
