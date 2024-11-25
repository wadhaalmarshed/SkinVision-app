import streamlit as st
from PIL import Image

# Title of the app
st.title("Streamlit Image Display Example")

# Load an image (local file)
image_path = "https://ibb.co/jTCVKkB"
image = Image.open(image_path)

# Display the image in the app
st.image(image, caption="This is your image", use_column_width=True)
