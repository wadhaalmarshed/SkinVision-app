import streamlit as st

# Inject custom CSS to change background color
st.markdown("""
    <style>
        body {
            background-color: #DAC2B1;  /* Light beige color */
        }
    </style>
""", unsafe_allow_html=True)

# Add content to your app

image_url = "https://ibb.co/jTCVKkB"
st.image(image_url, caption="logo", width=300)
