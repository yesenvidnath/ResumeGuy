import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def parse_resume_gemini(text):
    """ Extracts structured resume data using Google Gemini API """
    prompt = f"""
    Extract and structure this resume text into JSON format with the following keys:
    - name
    - contact_info
    - skills (as a list)
    - experience (as a list of job titles and companies)
    - education (as a list of degrees and institutions)
    - certifications (if available)
    
    Text: {text}
    """

    response = genai.generate_text(prompt)
    
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        print("Error parsing JSON response.")
        return {}
