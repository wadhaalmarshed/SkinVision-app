import streamlit as st
from PIL import Image
import time

# Function to simulate the model processing (e.g., image transformation)
def reprocess_image(image, progress):
    # Simulate some image processing, e.g., applying filters or resizing
    time.sleep(0.5)  # Simulate a short delay to show progress bar working
    processed_image = image.convert("L")  # Convert the image to grayscale as an example

    # Simulating progress for the image processing
    for i in range(100):
        time.sleep(0.05)  # Simulating time taken for each step
        progress.progress(i + 1)  # Update progress bar

    return processed_image

# Function to display a styled markdown header
def header(title, subtitle):
    st.markdown(f"<h1 style='color: #F27C6A; text-align: center;'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color: #5C5C5C; text-align: center;'>{subtitle}</h4>", unsafe_allow_html=True)

# Streamlit App with a polished UI
def main():
    # Set page config with custom title, icon, and wide layout
    st.set_page_config(page_title="SkinVision: Image Upload & Reprocessing", page_icon=":camera:", layout="wide")
    
    # Custom CSS styling to enhance the UI
    st.markdown("""
        <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #F5F5DC; /* Beige background */
            color: #333;
        }
        .stButton button {
            background-color: #F27C6A;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #F27C6A;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }
        .stProgress>div {
            background-color: #F27C6A;
        }
        .stAlert {
            background-color: #F27C6A;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: #777;
        }
        .footer a {
            color: #F27C6A;
            text-decoration: none;
        }
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 200px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Logo upload (Centered)
    logo_file = st.file_uploader("Upload Logo", type=["jpg", "png", "jpeg"], help="Upload a logo to display at the top of the page.")
    if logo_file is not None:
        logo = Image.open(logo_file)
        st.image(logo, caption="Logo", use_column_width=False, width=200)

    # Header with the app name
    header("SkinVision: Image Upload & Reprocessing", "Upload skin images for analysis and reprocessing.")

    # Create columns for image upload and processing dashboard
    col1, col2 = st.columns([2, 1])

    # Section 1: Image Upload in the first column
    with col1:
        st.subheader("1. Upload Your Skin Image")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], help="Upload a skin-related image (e.g., mole, lesion).")

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.success("Image uploaded successfully!")

            # Show reprocess button only after image upload
            if st.button("Reprocess Image :twisted_rightwards_arrows:", key="reprocess"):
                with st.spinner("Processing..."):
                    # Create the progress bar
                    progress = st.progress(0)
                    # Reprocess the image and simulate the progress
                    processed_image = reprocess_image(image, progress)
                    st.image(processed_image, caption="Processed Image", use_column_width=True)

                    # Show model dashboard after reprocessing (under the processed image)
                    st.subheader("2. Model Processing Dashboard")
                    st.write("Model: Grayscale Conversion (Example)")
                    st.write("Processing Time: ~2 seconds")
                    st.write("This simple model converts the uploaded image to grayscale.")
                    st.write("More sophisticated models could be used here, such as lesion detection or skin cancer classification.")

                    # Optional: Download button for processed image
                    st.download_button("Download Processed Image", processed_image, file_name="processed_image.jpg", mime="image/jpeg")

    # Adding a footer with some branding and links
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
        <div class="footer">
            <p>Powered by <a href="https://www.streamlit.io/" target="_blank">Streamlit</a> | Created for SkinVision</p>
            <p>Find out more about skin health and AI-based analysis on our <a href="https://www.skinvision.com" target="_blank">official website</a>.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
