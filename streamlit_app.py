import streamlit as st

# Set up the page config (optional, but gives you control over the app's layout)
st.set_page_config(
    page_title="Your App Title",
    page_icon="your_logo.png",  # Set your logo for the page icon (favicon)
)

# Set the logo at the top
st.image("your_logo.png", width=150)  # Adjust the width of the logo as needed

# Inject custom CSS to change background color to beige
st.markdown("""
    <style>
        body {
            background-color: #f5f5dc;  # Beige color
        }
    </style>
""", unsafe_allow_html=True)

# Your app content goes here
st.title("Welcome to My Streamlit App")
st.write("This app has a beige background and a custom logo!")
