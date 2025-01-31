import pytesseract
import fitz  # PyMuPDF
import pdf2image
import pdfminer.high_level
import cv2
import numpy as np
from PIL import Image
from docx import Document

def extract_text_from_pdf(pdf_path):
    """ Extract text from PDF using pdfminer and pdf2image for better OCR. """
    try:
        # Try extracting directly from PDF (works best for digital PDFs)
        text = pdfminer.high_level.extract_text(pdf_path)
        if text.strip():
            return text

        # If no text, convert PDF to images and use OCR
        images = pdf2image.convert_from_path(pdf_path)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        return text

    except Exception as e:
        return f"Error extracting text: {str(e)}"

def extract_text_from_docx(docx_path):
    """ Extract text from Word documents """
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_image(img_path):
    """ Extract text from an image using OpenCV preprocessing and Tesseract OCR """
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(binary)
    return text
