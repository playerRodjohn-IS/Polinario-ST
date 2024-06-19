import os
import streamlit as st
import pickle
from sklearn.ensemble import RandomForestRegressor

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the pickle file
pkl_file_path = os.path.join(script_dir, 'life_expectancy_model.pkl')

# Load the model from the pickle file
with open(pkl_file_path, 'rb') as f:
    loaded_model = pickle.load(f)

# Function to predict life expectancy
def predict_life_expectancy(BMI, GDP_per_capita, Alcohol_consumption):
    return loaded_model.predict([[BMI, GDP_per_capita, Alcohol_consumption]])[0]

# Streamlit app
st.title('Life Expectancy Prediction App')

# Input fields
BMI = st.number_input('Enter BMI:', min_value=0.0, value=100.0)
GDP_per_capita = st.number_input('Enter GDP per Capita:', min_value=0, value=100000)
Alcohol_consumption = st.number_input('Enter Alcohol Consumption:', min_value=0.0, value=20.0)

# Predict button
if st.button('Predict Life Expectancy'):
    result = predict_life_expectancy(BMI, GDP_per_capita, Alcohol_consumption)
    st.write(f'Predicted Life Expectancy: {result:.2f} years')
