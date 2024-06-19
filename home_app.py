import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [
        Page("home_app.py", "ITEQMT Machine Learning Application Portfolio", "👨‍💻"),
        Section("Main Page", "📢"),
        Page("pages/aboutme_app.py", "ABOUT ME", "1️⃣", in_section=True),
        Page("pages/appdescription_app.py", "Streamlit Features Description", "2️⃣", in_section=True),
        Page("pages/mylearnings_app.py", "🧠 What I Have Learned", "3️⃣", in_section=True),

        Section("Sample Projects", "📂"),
        Page("pages/emotion_app.py", "📝Basic Sentiment Analyzer", "1️⃣", in_section=True),
        Page("pages/analyzer_app.py", "Dog Breeds Classification", "2️⃣", in_section=True),
        Page("pages/prediction_app.py", "📊 Prediction", "3️⃣", in_section=True),

        Section("Project Source Code", "💻"),
        Page("pages/emotion_code.py", "Sentiment Analyzer SRC", "1️⃣", in_section=True),
        Page("pages/analyzer_code.py", "Image Classification SRC", "2️⃣", in_section=True),
        Page("pages/prediction_code.py", "Prediction SRC", "3️⃣", in_section=True),
    ]
)
hide_pages(["Thank you"])

st.markdown("### FINAL REQUIREMENTS PRESENTED BY: ")
st.header("Polinario, Rod John of BSIS 3B")
st.image("./profile.JPG")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)

st.info("For more info. Contact:", unsafe_allow_html=True)
with st.expander("See Contacts"):
  st.markdown("""
  * [Polinario, Rod John T.](/https://www.facebook.com/polinario.rodjohn.3?mibextid=JRoKGi) on Fb
  * [@withplayy](https://www.instagram.com/polinario.rodjohn?igsh=MXdnaGY0Z2hzNzJqag==) on IG
  """, unsafe_allow_html=True)

st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("History, Purpose and, Usage"""):
    st.markdown("""
    
    
    #

        History of Machine Learning
        
Machine learning has a rich history spanning several decades. 
It began in the 1940s-1950s with the foundation of AI and the introduction of neural networks by Frank Rosenblatt. 
The 1950s-1960s saw symbolic AI using explicit rules and logic, with early programs like the Logic Theorist. 
From the 1960s-1980s, machine learning algorithms emerged, including the nearest neighbor algorithm and the backpropagation algorithm for neural networks.
Despite an "AI Winter" in the 1970s-1980s, foundational work continued. The 1990s brought a resurgence with statistical methods like SVMs and ensemble methods.
The 2000s-2010s marked the deep learning revolution with CNNs and RNNs, significantly advancing image and sequence data processing. By the 2010s, machine learning became crucial in various fields, aided by frameworks like TensorFlow and PyTorch. 
Key figures include Geoffrey Hinton, Yann LeCun, and Yoshua Bengio, pioneers in deep learning. Today, machine learning continues to evolve rapidly, driving innovation across numerous applications
.
               
        Purpose of Machine Learning
                 
The purpose of machine learning is to enable computers to learn from data and make decisions or predictions without being explicitly programmed. 
It aims to create systems that can automatically improve their performance over time through experience. 
Machine learning is used to recognize patterns, classify information, and make forecasts based on data. It helps in automating tasks, enhancing efficiency, and providing insights in various fields such as healthcare, finance, marketing, and technology. 
By leveraging algorithms and statistical models, machine learning enables the development of intelligent applications that can adapt and respond to new data, ultimately driving innovation and solving complex problems
.
                
        Usage of Machine Learning
Machine learning is used across various industries and applications, including:

* Healthcare: Machine learning is used to analyze medical data for diagnosing diseases, predicting patient outcomes, and personalizing treatment plans.
* Entertainment: It powers recommendation systems for streaming services, helping to suggest movies, shows, and music tailored to individual preferences.
* Transportation: Machine learning enhances autonomous driving technologies, optimizing routes, and improving safety through predictive maintenance and traffic management.
* Retail: Machine learning helps in demand forecasting, personalized marketing, and inventory management, enhancing customer experience and sales.
* Manufacturing: It enables predictive maintenance, quality control, and supply chain optimization, improving efficiency and reducing downtime.
* Business: It is used for financial analysis, fraud detection, and customer relationship management, driving better decision-making and operational efficiency.
    #""", unsafe_allow_html=True)

st.title('Introduction to the Streamlit Application Project')

st.markdown("""


##### 👨‍🔧 More Content

Welcome to our Streamlit Application Project, a comprehensive initiative designed to harness the power of machine learning through an 
            intuitive and interactive web interface. This project aims to showcase the versatility and practicality of machine learning 
            models in real-world applications, specifically focusing on three key areas: sentiment analysis, image classification, and predictive analytics.
### 🔎 Overview""", unsafe_allow_html=True)


st.image("./profile.JPG")


st.markdown("""
Machine learning is a branch of artificial intelligence (AI) that focuses on developing algorithms and statistical models that enable computers 
            to perform tasks without explicit instructions. Instead, these systems learn from data, identifying patterns and making decisions with 
            minimal human intervention. The core idea is to allow the machine to improve its performance over time as it is exposed to more data.
Quantitative methods refer to a set of techniques used in research and analysis that rely on quantifiable data, numerical values, and statistical 
            methods to investigate phenomena, test hypotheses, and draw conclusions. These methods are particularly useful in fields such as social sciences, 
            economics, psychology, and natural sciences, where researchers seek to measure and analyze observable and measurable variables. 
                       
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 