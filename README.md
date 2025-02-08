# OCR Data Extraction and Storage

## Project Overview
This project extracts data from patient assessment forms using Optical Character Recognition (OCR) and stores the extracted data in a SQL database in JSON format.

## Project Structure
```
OCR_Assignment/
├── main.py                 # Main entry point for running the full process
├── preprocess.py           # Image preprocessing functions
├── parse_text.py           # Text parsing functions using regex
├── database.py             # Database schema and insert functions
├── requirements.txt        # Dependencies for the project
└── README.md               # Documentation
```

## Setup Instructions
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Update the database connection URL in `database.py`.
4. Run the `main.py` script:
   ```bash
   python main.py
   ```

## Sample JSON Output
```json
{
  "patient_name": "John Doe",
  "dob": "01/05/1988",
  "injection": "Yes",
  "exercise_therapy": "No",
  "difficulty_ratings": {
    "bending": 3,
    "putting_on_shoes": 1,
    "sleeping": 2
  },
  "pain_symptoms": {
    "pain": 2,
    "numbness": 5
  }
}
```

## Notes
- Ensure Tesseract OCR is installed and added to your system path.
- Test the script with various sample images for best results.
- Handle exceptions and edge cases in `parse_text.py` to improve reliability.
- Change the username and password as for your database in main.py
