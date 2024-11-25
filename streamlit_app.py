import streamlit as st

# Add title to the app
st.title("Welcome to My App")

# Display an image as soon as the app loads
image_url = "https://ibb.co/jTCVKkB"  # Replace with your image URL
st.image(image_url, caption="Your Image Caption", use_column_width=True)

# Additional app content here
st.write("This is the content that appears below the image.")
