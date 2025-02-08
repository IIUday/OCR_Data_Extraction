import re

def parse_text(text):
    data = {
        "patient_name": re.search(r"Patient Name : ([\w\s]+)", text).group(1).strip() if re.search(r"Patient Name : ([\w\s]+)", text) else None,
        "dob": re.search(r"DOB : ([\d/]+)", text).group(1).strip() if re.search(r"DOB : ([\d/]+)", text) else None,
        "injection": "Yes" if "INJECTION : YES" in text else "No",
        "exercise_therapy": "Yes" if "Exercise Therapy : YES" in text else "No",
        "difficulty_ratings": {
            "bending": int(re.search(r"Bending or Stooping: (\d)", text).group(1)) if re.search(r"Bending or Stooping: (\d)", text) else None,
            "putting_on_shoes": int(re.search(r"Putting on shoes: (\d)", text).group(1)) if re.search(r"Putting on shoes: (\d)", text) else None,
            "sleeping": int(re.search(r"Sleeping: (\d)", text).group(1)) if re.search(r"Sleeping: (\d)", text) else None
        },
        "pain_symptoms": {
            "pain": int(re.search(r"Pain: (\d+)", text).group(1)) if re.search(r"Pain: (\d+)", text) else None,
            "numbness": int(re.search(r"Numbness: (\d+)", text).group(1)) if re.search(r"Numbness: (\d+)", text) else None
        }
    }
    return data
