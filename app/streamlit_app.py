import streamlit as st
import joblib
import pandas as pd
import glob

st.title("🚕 NYC Taxi Demand Predictor")

model = joblib.load("ml/model.pkl")

hour = st.slider("Hour", 0, 23)
day = st.slider("Day (0=Mon, 6=Sun)", 0, 6)

prediction = model.predict([[hour, day]])

st.metric("Predicted Demand", int(prediction[0]))

# Load data for visualization
files = glob.glob("data/processed/*.csv")
df = pd.concat([pd.read_csv(f) for f in files])

st.subheader("Trips by Hour")
st.line_chart(df.groupby('hour')['count'].sum())
