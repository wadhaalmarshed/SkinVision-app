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
st.title("Streamlit App with Custom Background Color")
st.write("This app has a custom background color of #DAC2B1.")
