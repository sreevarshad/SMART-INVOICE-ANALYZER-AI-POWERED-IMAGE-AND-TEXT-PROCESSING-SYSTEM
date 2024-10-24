# SMART INVOICE ANALYZER: AI-POWERED IMAGE AND TEXT PROCESSING SYSTEM

## Introduction:
The Smart Invoice Analyzer is an advanced AI-driven solution designed to automate the extraction and interpretation of data from invoice images. The system uses Optical Character Recognition (OCR) with Tesseract to process invoices and leverages Google Generative AI (gemini-1.5-flash) for multilingual support, allowing users to handle invoices in various languages. This project is developed using Python and Streamlit to provide an intuitive web-based interface, ensuring easy uploading of invoice images and quick, accurate text extraction and translation.

---

## Requirements:

### Software Specification:
- **Programming Language:** Python
- **Libraries:** Streamlit, Tesseract-OCR, GoogleTrans, google-generativeai, PIL (Python Imaging Library)
- **Operating System:** Windows 10/11 (32 and 64 bit)

### Hardware Specification:
- **RAM:** Minimum 4GB
- **OS:** Windows 7, 8, or 10 (32 or 64-bit)

### Environment Setup:
- **Tesseract Installation:** Download and install Tesseract-OCR and update the path in the script accordingly.
- **Python Libraries:** Install the following libraries:
  
  ```bash
  pip install streamlit pytesseract googletrans==4.0.0-rc1 google-generativeai Pillow python-dotenv

## Existing System:
Traditional invoice processing is manual and time-consuming. Existing solutions often use Optical Character Recognition (OCR) but are limited to single-language support. Handling multilingual invoices can be particularly challenging in international businesses, requiring users to switch between different systems.

## Proposed System:
The Smart Invoice Analyzer introduces a unified platform for multi-language invoice processing. It automates text extraction and translation, eliminating the manual effort involved in handling invoices in different languages. By leveraging the Gemini 1.5 flash model and Tesseract OCR, the system can quickly extract relevant text from images, clean it, and translate it into the desired language specified by the user. This enhances productivity and minimizes errors caused by manual data entry.

## Proposed Methodology:
Data Collection: Invoice images are uploaded by the user.
Text Extraction: Tesseract OCR extracts text from the uploaded invoice image.
Text Cleaning: The extracted text is cleaned to remove unwanted characters and excess whitespace.
Language Identification: The system identifies the target language for translation based on the user’s input.
Translation: The extracted text is translated into the specified language using Google Translate.
Response Generation: The system provides the user with both the extracted and translated text.

## System Architecture:
![Invoice Example](https://github.com/sreevarshad/SMART-INVOICE-ANALYZER-AI-POWERED-IMAGE-AND-TEXT-PROCESSING-SYSTEM/blob/main/images/Screenshot%202024-10-13%20125903.png)



## Result & Implications:
Accurate Invoice Processing: The system automates invoice text extraction, reducing manual errors.
Multi-language Support: Supports translation of invoices in multiple languages including English, French, Japanese, Marathi, Tamil, and Hindi.
Faster Decision-Making: Speeds up invoice processing, improving decision-making for businesses.
Improved Productivity: Reduces the time spent on manual data entry and translation.

## Conclusion:
The Smart Invoice Analyzer enhances efficiency in handling multi-language invoices by automating the extraction and translation processes using advanced OCR and AI techniques. By simplifying the extraction of data from images and supporting multiple languages, the system contributes to more streamlined invoice management, especially for international businesses.

## References:
Smith, R., 2021. "A Survey of Optical Character Recognition Systems". Journal of Image and Vision Computing, 45(3), pp.25-39.
Lee, C., 2020. "Multilingual Invoice Processing Using OCR and Machine Translation". International Journal of Applied AI Research, 14(4), pp.67-80.


