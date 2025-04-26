import streamlit as st
import pandas as pd
import pickle

# Load the trained model
@st.cache_resource
def load_model():
    with open('rainfall_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

st.title("🌧️ Rainfall Prediction App")
st.write("Predict if it will rain tomorrow based on today's weather conditions.")

st.sidebar.header("Input Features")

def user_input_features():
    min_temp = st.sidebar.slider('Min Temperature (°C)', 0.0, 40.0, 15.0)
    max_temp = st.sidebar.slider('Max Temperature (°C)', 10.0, 50.0, 25.0)
    humidity_9am = st.sidebar.slider('Humidity at 9AM (%)', 0, 100, 50)
    humidity_3pm = st.sidebar.slider('Humidity at 3PM (%)', 0, 100, 50)
    pressure_9am = st.sidebar.slider('Pressure at 9AM (hPa)', 980, 1050, 1010)
    pressure_3pm = st.sidebar.slider('Pressure at 3PM (hPa)', 980, 1050, 1010)
    cloud_9am = st.sidebar.slider('Cloud Cover at 9AM (%)', 0, 8, 4)
    cloud_3pm = st.sidebar.slider('Cloud Cover at 3PM (%)', 0, 8, 4)

    data = {
        'MinTemp': min_temp,
        'MaxTemp': max_temp,
        'Humidity9am': humidity_9am,
        'Humidity3pm': humidity_3pm,
        'Pressure9am': pressure_9am,
        'Pressure3pm': pressure_3pm,
        'Cloud9am': cloud_9am,
        'Cloud3pm': cloud_3pm
    }
    return pd.DataFrame([data])

input_df = user_input_features()

st.subheader('Input Weather Data')
st.write(input_df)

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.subheader("Prediction:")
    st.success("🌧️ It will rain tomorrow." if prediction == 1 else "☀️ It will not rain tomorrow.")
