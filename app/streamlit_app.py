import streamlit as st
import joblib
import pandas as pd
import glob
import pydeck as pdk

st.title("🚕 NYC Taxi Demand Predictor")
st.subheader("🗺️ Taxi Demand Heatmap")

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

# Load map data
import glob
files = glob.glob("data/map_data/*.csv")
map_df = pd.concat([pd.read_csv(f) for f in files])

# Rename columns for pydeck
map_df = map_df.rename(columns={
    "pickup_latitude": "lat",
    "pickup_longitude": "lon"
})

# Drop missing values
map_df = map_df.dropna()

# Create heatmap layer
layer = pdk.Layer(
    "HeatmapLayer",
    data=map_df,
    get_position='[lon, lat]',
    radiusPixels=50,
)

view_state = pdk.ViewState(
    latitude=40.7128,
    longitude=-74.0060,
    zoom=10,
)

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
))
