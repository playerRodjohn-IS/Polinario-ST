import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

# Add the page title
add_page_title()

# Show pages configuration
show_pages(
    [
        Page("home_app.py", "ITEQMT Machine Learning Application Portfolio", "👨‍💻"),
        Section("Main Page", "📢"),
        Page("pages/aboutme_app.py", "ABOUT ROD JOHN", "1️⃣", in_section=True),
        Page("pages/appdescription_app.py", "APP FEATURES DESCRIPTION", "2️⃣", in_section=True),
        Page("pages/mylearnings_app.py", "MY CLASS LEARNINGS", "3️⃣", in_section=True),

        Section("Sample Projects", "📂"),
        Page("pages/emotion_app.py", "SENTIMENT ANALYZER", "1️⃣", in_section=True),
        Page("pages/analyzer_app.py", "HOLIDAY'S CLASSIFICATION", "2️⃣", in_section=True),
        Page("pages/prediction_app.py", "LIFE EXPECTANCY PREDICTION", "3️⃣", in_section=True),

        Section("Project Source Code", "💻"),
        Page("pages/emotion_code.py", "Sentiment Analyzer CODE", "1️⃣", in_section=True),
        Page("pages/analyzer_code.py", "Holiday's Classification CODE", "2️⃣", in_section=True),
        Page("pages/prediction_code.py", "Life Expectancy CODE", "3️⃣", in_section=True),
    ]
)

# Hide specific pages if necessary
hide_pages(["Thank you"])

# Final requirements section
st.markdown("### FINAL REQUIREMENTS PRESENTED BY: ")
st.header("Polinario, Rod John of BSIS 3B")
st.image("./profile.JPG")

# Add a description under the image
st.markdown('''
This Streamlit app project is my final end-term project, featuring three main functionalities:

1. **Life Expectancy Prediction**: Predicts life expectancy based on inputs such as schooling, BMI, and alcohol consumption.
2. **Emotion Analyzer**: Analyzes emotions such as joy, sadness, and frustration based on input sentences.
3. **Image Classification for Holidays**: Classifies images into holiday categories like Christmas, Halloween, Lent season, New Year, and Valentine's Day.

Explore the app to see how machine learning models can provide insights and enhance user interaction.
''')

# Add a hyperlink (ensure correct formatting)
st.markdown('''
<a href="https://www.freeimages.com/photographer/thinkstock-83786" target="_blank">Thinkstock</a> on <a href="https://www.freeimages.com" target="_blank">Freeimages.com</a>
''', unsafe_allow_html=True)
