import os
import re
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Get API key from environment and configure Google Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Initialize the Google Translator and Tesseract
translator = Translator()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path based on your installation

# Function to clean up extracted text
def clean_extracted_text(text):
    # Remove unwanted characters and excess whitespace
    cleaned_text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with a single space
    cleaned_text = cleaned_text.strip()  # Remove leading and trailing whitespace
    return cleaned_text

# Function to handle image upload and text extraction using Tesseract OCR
def extract_text_from_image(uploaded_file):
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image.", use_column_width=True)
        
        # Extract text using Tesseract with improved configuration
        extracted_text = pytesseract.image_to_string(img, config='--psm 6')  # Adjust config for better accuracy
        return clean_extracted_text(extracted_text)
    else:
        raise FileNotFoundError("No file uploaded")

# Function to translate extracted text to the target language
def translate_text(extracted_text, target_language='en'):
    if extracted_text:
        translated = translator.translate(extracted_text, dest=target_language)
        return translated.text
    return ""

# Function to identify target language from user input (limited to specified languages)
def identify_target_language(prompt):
    languages = {
        "english": "en",
        "french": "fr",
        "japanese": "ja",
        "marathi": "mr",
        "tamil": "ta",
        "hindi": "hi"
    }
    
    # Check for any language mentioned in the prompt
    for language in languages.keys():
        if re.search(r'\b' + re.escape(language) + r'\b', prompt, re.IGNORECASE):
            return languages[language]
    
    return 'en'  # Default to English if no language is specified

# Function to load Gemini 1.5 flash model and get response (image + text)
def get_gemini_response(input_text, image_data):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Generating response based on the input prompt (task and language are specified in the input)
    response = model.generate_content([input_text, image_data])
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Multi-Language Invoice Extractor")

st.header("MULTI-LANGUAGE INVOICE EXTRACTOR")

# Input for the user's prompt, including language specification
input_text = st.text_input("Enter your prompt (Specify task and language if needed): ", key="input")  
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Submit button to trigger processing
submit = st.button("RESPOND TO THE PROMPT")

# Handling the response when the button is clicked
if submit:
    if uploaded_file:
        try:
            # Step 1: Extract text from the uploaded image using Tesseract OCR
            extracted_text = extract_text_from_image(uploaded_file)
            st.subheader("Extracted Text:")
            st.write(extracted_text)

            # Step 2: Identify the target language from the user input
            target_language = identify_target_language(input_text)
            
            # Step 3: Translate the extracted text
            translated_text = translate_text(extracted_text, target_language)
            st.subheader(f"Translated Text ({target_language}):")
            st.write(translated_text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload an image.")
