import streamlit as st
import pickle
import nltk
from nltk.classify import NaiveBayesClassifier
import os

# Download NLTK data
nltk.download('punkt')

# Function to extract features (words) from text
def word_features(words):
    return dict([(word, True) for word in words])

# Define emotional words and their corresponding categories
happy_words = [
    'happy', 'delighted', 'ecstatic', 'cheerful', 'elated', 'jubilant',
    'exuberant', 'thrilled', 'gleeful', 'radiant', 'blissful', 'overjoyed',
    'euphoric', 'excited', 'grateful', 'satisfied', 'lighthearted', 'merry',
    'enjoyable', 'uplifting', 'delightful', 'fun', 'heartwarming',
    'captivating', 'joyous', 'charming', 'entertaining',
    'positive', 'exhilarating', 'thrilling', 'satisfying',
    'lovable', 'beautiful', 'adorable', 'fantastic', 'brilliant',
    'amazing', 'awesome', 'wonderful', 'fantastic', 'superb'
]

frustrated_words = [
    'frustrated', 'annoyed', 'irritated', 'aggravated',
    'exasperated', 'disgruntled', 'angry', 'mad', 'furious',
    'livid', 'infuriated', 'resentful', 'incensed', 'enraged',
    'bitter', 'hostile', 'fuming', 'riled up', 'wrathful',
    'disgusted', 'distressed', 'discontented', 'vexed',
    'displeased', 'perturbed', 'bothered', 'pissed off',
    'offended', 'irked', 'fed up', 'exasperated', 'outraged',
    'seething', 'peeved', 'agitated', 'tense', 'storming out',
    'upset', 'cross', 'angered', 'infuriated', 'fuming'
]

sad_words = [
    'sad', 'unhappy', 'gloomy', 'miserable', 'depressed',
    'heartbroken', 'tearful', 'sorrowful', 'despondent',
    'despairing', 'melancholy', 'grief-stricken', 'wistful',
    'desolate', 'disconsolate', 'forlorn', 'downcast', 'blue',
    'dejected', 'bereft', 'morose', 'somber', 'downhearted',
    'heavy-hearted', 'woeful', 'wretched', 'broken-hearted',
    'crestfallen', 'sullen', 'weepy', 'lugubrious', 'weepy',
    'glum', 'plaintive', 'pensive', 'melancholic', 'sombre',
    'dispirited', 'heartrending', 'sorrowing'
]

# Combine features for training
emotions = {
    'happy': happy_words,
    'frustrated': frustrated_words,
    'sad': sad_words
}

train_set = [(word_features(word.split()), emotion) for emotion, words in emotions.items() for word in words]

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Save the trained classifier as a pickle file
current_dir = os.path.dirname(os.path.abspath(__file__))
model_filename = os.path.join(current_dir, 'sentiment_model.sav')
with open(model_filename, 'wb') as model_file:
    pickle.dump(classifier, model_file)

# Function to classify emotion based on user input
def classify_emotion(input_text):
    # Load the trained classifier
    with open(model_filename, 'rb') as model_file:
        loaded_model = pickle.load(model_file)

    # Tokenize input text into words
    words = nltk.word_tokenize(input_text.lower())

    # Extract features from input words
    features = word_features(words)

    # Classify emotion
    emotion = loaded_model.classify(features)
    return emotion

# Streamlit app starts here
st.title("Emotion Analyzer :speech_balloon:")
message = st.text_area("Enter a sentence to analyze its emotion:")

# Function to classify sentiment and display result
def analyze_emotion():
    if message.strip():
        emotion = classify_emotion(message)
        st.write(f"Input: {message}")
        st.write(f"Predicted Emotion: {emotion}")
    else:
        st.write("Please enter a sentence to analyze.")

# Button to trigger emotion analysis
if st.button("Analyze Emotion"):
    analyze_emotion()
