import streamlit as st
import pandas as pd
import joblib

model = joblib.load('C:/Users/karan/OneDrive/Desktop/Model_HTML_CSS/Credit_Card_raud_Detection/fraud_detection_model.pkl')

st.title("Credit Card Fraud Detection")
uploaded_file = st.file_uploader("Upload transaction data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    prediction = model.predict(df)
    df['anomaly'] = prediction
    st.write(df)
    st.success("Prediction complete. -1 indicates Fraud.")
