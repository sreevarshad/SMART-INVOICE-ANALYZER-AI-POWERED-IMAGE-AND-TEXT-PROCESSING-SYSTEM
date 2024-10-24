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
