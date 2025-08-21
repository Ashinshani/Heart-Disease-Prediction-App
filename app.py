import streamlit as st
import pickle
import numpy as np  # Added missing import
from PIL import Image # Added missing import

# Load the model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

# UI (app)
st.title("Heart Disease Prediction App🩺")
st.image("heart.png", width=700)
st.markdown("Enter your symptoms to predict heart disease...🫀") 

# Input fields for user symptoms
col1, col2 = st.columns(2)
with col1:
   age = st.number_input("Enter Age", 20, 100, 52)
   sex = st.selectbox("Sex", [0, 1])  # 0 - female, 1 - male 
   cp = st.selectbox("Chest Pain Type (1-4)", [1, 2, 3, 4])  # 1- typical angina, 2 - atypical angina, 3 - non-anginal pain, 4 - asymptomatic
   trestbds = st.number_input("Resting Blood Pressure (mm Hg)", 90, 200, 130)
   chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 700, 200)
   fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])  # 0 - false, 1 - true

with col2:
   restecg = st.selectbox("Resting Electrocardiographic Results (0-2)", [0, 1, 2])  # 0 - normal, 1 - ST-T wave abnormality, 2 - left ventricular hypertrophy
   thalach = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)
   exang = st.selectbox("Exercise Induced Angina", [0, 1])  # 0 - no, 1 - yes
   oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", 0.0, 6.0, 1.0)
   slope = st.selectbox("Slope of the Peak Exercise ST Segment (0-2)", [0, 1, 2])  # 0 - upsloping, 1 - flat, 2 - downsloping
   major_vessels = st.number_input("Number of Major Vessels Colored by Fluoroscopy (0-3)", 0, 3, 0)
   thal = st.selectbox("Thalassemia ", [3, 6, 7])  # 3 - normal, 6 - fixed defect, 7 - reversible defect  

# Button to make prediction - FIXED: moved all prediction logic inside the if block
if st.button("Predict"):
    # Create input_data inside the button click block
    input_data = np.array([[age, sex, cp, trestbds, chol, fbs, restecg, thalach, exang, oldpeak, slope, major_vessels, thal]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display result
    if prediction[0] == 2:
        st.error("⚠️ You have a high risk of heart disease. Please consult a doctor.")      
    else:
        st.success("✅ You have a low risk of heart disease. Keep up the good health! 😊")