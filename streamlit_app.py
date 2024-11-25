import streamlit as st

# Injecting custom CSS
st.markdown("""
    <style>
        /* Change background color to beige */
        body {
            background-color: #f5f5dc;
        }

        /* Change font color and size for the title */
        .streamlit-expanderHeader {
            font-size: 28px;
            color: #2a2a2a;
            font-family: 'Arial', sans-serif;
        }

        /* Add padding to all content in Streamlit */
        .block-container {
            padding: 20px;
        }

        /* Style the sidebar */
        .sidebar .sidebar-content {
            background-color: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

# Display some content
st.title("Streamlit App with Custom CSS")
st.write("This app uses custom CSS to modify the appearance.")
