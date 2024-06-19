import streamlit as st
from PIL import Image
import os

# Page title
st.set_page_config(layout="wide", page_title="Streamlit App Features Description")

# Define the path to the images folder (adjust if needed)
images_folder = "."

# Feature 1: Life Expectancy Prediction
st.header('Feature 1: Life Expectancy Prediction')
st.write('''
This feature predicts life expectancy based on inputs such as schooling, BMI, and alcohol consumption. The prediction model utilizes data from the Kaggle Life Expectancy dataset, which includes various demographic and health-related factors. Users can input their own values and obtain an estimate of life expectancy, providing insights into how lifestyle choices can impact longevity.
''')
# Display image for Life Expectancy Prediction feature
life_expectancy_image_path = os.path.join(images_folder, "predictpic.png")
if os.path.exists(life_expectancy_image_path):
    life_expectancy_image = Image.open(life_expectancy_image_path)
    st.image(life_expectancy_image, caption='Life Expectancy Prediction', use_column_width=True)
else:
    st.error(f"File not found: {life_expectancy_image_path}")

# Feature 2: Emotion Analyzer
st.header('Feature 2: Emotion Analyzer')
st.write('''
The Emotion Analyzer feature analyzes emotions such as joy, sadness, and frustration based on input sentences. Originally designed for analyzing comments from movie or TV series reviews, users can input text to determine the underlying emotional tone. This tool is useful for gauging audience sentiment and understanding emotional responses to media content.
''')
# Display image for Emotion Analyzer feature
emotion_analyzer_image_path = os.path.join(images_folder, "sentimentpic.png")
if os.path.exists(emotion_analyzer_image_path):
    emotion_analyzer_image = Image.open(emotion_analyzer_image_path)
    st.image(emotion_analyzer_image, caption='Emotion Analyzer', use_column_width=True)
else:
    st.error(f"File not found: {emotion_analyzer_image_path}")

# Feature 3: Image Classifications for Holidays
st.header('Feature 3: Image Classifications for Holidays')
st.write('''
This feature provides image classification for five different holidays: Christmas, Halloween, Lent season, New Year, and Valentine's Day. Users can upload images or use predefined examples to classify them into the respective holiday categories. The classification model is trained on a dataset containing holiday-themed images to accurately identify holiday-specific attributes.
''')
# Display image for Image Classifications for Holidays feature
holiday_classification_image_path = os.path.join(images_folder, "imageClasspic.png")
if os.path.exists(holiday_classification_image_path):
    holiday_classification_image = Image.open(holiday_classification_image_path)
    st.image(holiday_classification_image, caption='Holiday Image Classifications', use_column_width=True)
else:
    st.error(f"File not found: {holiday_classification_image_path}")

# Footer
st.write("Explore these features to gain insights and enjoy interactive experiences with the Streamlit app!")
