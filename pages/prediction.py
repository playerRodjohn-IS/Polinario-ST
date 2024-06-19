import os
import pandas as pd
import ydata_profiling as p_prof  # Updated import
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pickle

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define file paths
csv_file_path = os.path.join(script_dir, 'Life Expectancy Data.csv')
pkl_file_path = os.path.join(script_dir, 'life_expectancy_model.pkl')

# Print current working directory and files in the script directory
print("Current Working Directory:", os.getcwd())
print("Files in the script directory:", os.listdir(script_dir))

# Check if the CSV file exists
if not os.path.exists(csv_file_path):
    raise FileNotFoundError(f"The file {csv_file_path} does not exist.")

# Load the dataset
datasetCSV = pd.read_csv(csv_file_path)

# Display the head of the dataset
print(datasetCSV.head())

# Preprocess the data
# Selecting relevant columns and dropping rows with missing values
datasetCSV = datasetCSV[['BMI', 'GDP_per_capita', 'Alcohol_consumption', 'Life_expectancy']]
datasetCSV = datasetCSV.dropna()

# Define the features (X) and the target (y)
X = datasetCSV[['BMI', 'GDP_per_capita', 'Alcohol_consumption']]
y = datasetCSV['Life_expectancy']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}')

# Save the model to a pickle file
with open(pkl_file_path, 'wb') as f:
    pickle.dump(model, f)

# Load the model from the pickle file
with open(pkl_file_path, 'rb') as f:
    loaded_model = pickle.load(f)

# Function to predict life expectancy
def predict_life_expectancy(BMI, GDP_per_capita, Alcohol_consumption):
    return loaded_model.predict([[BMI, GDP_per_capita, Alcohol_consumption]])[0]

# Example prediction
example_BMI = 25
example_GDP_per_capita = 10000
example_Alcohol_consumption = 10
predicted_life_expectancy = predict_life_expectancy(example_BMI, example_GDP_per_capita, example_Alcohol_consumption)
print(f'Predicted Life Expectancy: {predicted_life_expectancy}')
