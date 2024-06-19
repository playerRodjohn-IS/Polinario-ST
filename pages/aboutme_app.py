import streamlit as st
from PIL import Image
import os

# Profile Page
st.set_page_config(layout="wide", page_title="About Me")

# Add a header with your full name
st.title('Rod John Tones Polinario')

# Display your picture
profile_image_path = 'profile.JPG'  # Ensure this path is correct
if os.path.exists(profile_image_path):
    profile_image = Image.open(profile_image_path)
    st.image(profile_image, width=600)
else:
    st.error(f"File not found: {profile_image_path}")

# Add your personal information
st.subheader('Personal Information')
info_columns = st.columns([1, 3])
with info_columns[0]:
    st.write("**Address:** Sitio Balogo Barangay Concepcion Talisay City Negros Occidental")
    st.write("**Birthdate:** May 29, 2003")
    st.write("**Age:** 21 Years Old")
with info_columns[1]:
    st.write("**Gender:** Male")
    st.write("**Religion:** Catholic")
    st.write("**Occupation:** IS Student")

# Contact Information
st.subheader('Contact Information')
st.write("**Email:** rjtpolinario.chmsu@gmail.com")
st.write("**Phone:** 09770817226")
st.write("**Facebook:** [Rod John Polinario](https://www.facebook.com/johndoe)")
st.write("**Instagram:** [@withplayy](https://www.instagram.com/johndoe)")

# Background (Left-aligned)
st.subheader('Background')
st.markdown('''
Hello! My name is Rod John Polinario, and I'm currently pursuing a degree in information systems with a keen ambition to become a proficient programmer while exploring the world through travel. Technology has always fascinated me, and I find great satisfaction in crafting code that enhances efficiency and usability in software systems. Whether it's debugging intricate algorithms or designing intuitive user interfaces, I thrive on the challenges and creativity that programming entails.

As an introvert, I relish my quiet moments, often spent watching movies that transport me to different narratives and inspire new perspectives. This downtime not only rejuvenates me but also fuels my imagination, providing a refreshing break from the intricacies of coding and problem-solving.

Looking ahead, I envision myself not just as a skilled coder but also as a capable leader. I aspire to motivate and mentor a team of professionals, guiding them to collaborate effectively and innovate in software development. My communication skills, honed through coursework and personal development, enable me to articulate complex ideas clearly and inspire others toward a shared vision of success.
''')

# Image Slider horizontally
st.subheader('Gallery')
st.write("Here are some pictures of myself:")

# Function to load images for the slider
def load_image(file_path):
    if os.path.exists(file_path):
        return Image.open(file_path)
    else:
        st.error(f"File not found: {file_path}")
        return None

# Image paths - replace these with the paths to your images
image_files = ['image1.jpeg', 'image2.jpg', 'image3.jpeg', 'image4.jpg', 'image5.jpg']

# Display images in a horizontal slider with reduced size and spacing
image_columns = st.columns(len(image_files))
for col, image_file in zip(image_columns, image_files):
    personal_image = load_image(image_file)
    if personal_image:
        col.image(personal_image, width=200, caption=image_file, use_column_width=False)

# Footer
st.write("by koalatech...")
