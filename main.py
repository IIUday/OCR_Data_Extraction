import cv2
import pytesseract
from preprocess import preprocess_image
from parse_text import parse_text
from database import insert_data, create_tables, connect_db
import json
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def main(image_path):
    processed_image = preprocess_image(image_path)
    extracted_text = pytesseract.image_to_string(processed_image)
    print("Extracted Text:\n", extracted_text)
    parsed_data = parse_text(extracted_text)
    print("Parsed Data (JSON):\n", json.dumps(parsed_data, indent=4))
    engine, session = connect_db('postgresql://username:password@localhost/yourdatabase')
    create_tables(engine)
    insert_data(session, parsed_data)
    print("Data successfully inserted into the database.")

if __name__ == "__main__":
    image_path = "D:\\Assignments\\OCR_Assignment\\sample_data\\sample_form.jpg"
    main(image_path)
