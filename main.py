import os
from google.colab import files
from functions.extract_text import extract_text_from_pdf, extract_text_from_docx, extract_text_from_image
from functions.parse_resume import parse_resume_gemini
from functions.format_resume import format_resume_pandas
from functions.convert_to_pdf import convert_df_to_pdf

# Upload Resume File
uploaded = files.upload()
filename = list(uploaded.keys())[0]

# Extract Text Based on File Type
if filename.endswith(".pdf"):
    extracted_text = extract_text_from_pdf(filename)
elif filename.endswith(".docx"):
    extracted_text = extract_text_from_docx(filename)
elif filename.endswith((".png", ".jpg", ".jpeg")):
    extracted_text = extract_text_from_image(filename)
else:
    print("Unsupported file format")
    extracted_text = ""

# Parse Resume Using Google Gemini API
parsed_resume = parse_resume_gemini(extracted_text)

# Format Resume as Pandas DataFrame
df_resume = format_resume_pandas(parsed_resume)

# Save to PDF
convert_df_to_pdf(df_resume, "formatted_resume.pdf")

# Show DataFrame (optional)
import ace_tools as tools
tools.display_dataframe_to_user(name="Formatted Resume", dataframe=df_resume)

# Download Formatted Resume
files.download("formatted_resume.pdf")
