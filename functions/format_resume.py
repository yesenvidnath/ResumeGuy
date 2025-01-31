import pandas as pd

def format_resume_pandas(parsed_data):
    """ Converts parsed resume into an ATS-friendly Pandas DataFrame """
    resume_data = {
        "Section": ["Name", "Contact", "Skills", "Experience", "Education", "Certifications"],
        "Details": [
            parsed_data.get("name", ""),
            parsed_data.get("contact_info", ""),
            ", ".join(parsed_data.get("skills", [])),
            "\n".join(parsed_data.get("experience", [])),
            "\n".join(parsed_data.get("education", [])),
            "\n".join(parsed_data.get("certifications", []))
        ]
    }
    
    df = pd.DataFrame(resume_data)
    return df
