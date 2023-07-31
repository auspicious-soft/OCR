import re
import cv2
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def pan():
    print("======================== Pan Card Data ========================")
    # Load the image and convert it to grayscale
    img = cv2.imread('data/input/img/4.jpeg')
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Threshold the grayscale image
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Set text regions to white
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[thresh == 0] = 255

    # Invert the mask
    inv_mask = cv2.bitwise_not(mask)

    # Apply median blur to non-text regions
    blurred = cv2.medianBlur(img, 25)

    # Copy the original text regions to the blurred image
    blurred[mask == 0] = img[mask == 0]
    img = blurred

    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(img, lang="eng")
    # Define regular expressions for extracting fields
    name_regex = r"Name\n(.*?)\n"
    father_name_regex = r"Father's Name\n(.*?)\n"
    dob_regex = r"[0-9]{2}/[0-9]{2}/[0-9]{4}"
    pan_regex = r"([A-Z]{5}[0-9]{4}[A-Z]{1})"

    # Extract fields using regular expressions
    name_match = re.search(name_regex, text, flags=re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else ""
    father_name_match = re.search(father_name_regex, text, flags=re.IGNORECASE)
    father_name = father_name_match.group(1).strip() if father_name_match else ""
    dob_match = re.search(dob_regex, text, flags=re.IGNORECASE)
    dob = dob_match.group(0).strip() if dob_match else ""

    pan_match = re.search(pan_regex, text)
    pan = pan_match.group(1).strip() if pan_match else ""

    # Print extracted fields
    print("Name:", name)
    print("Father's Name:", father_name)
    print("Date of Birth:", dob)
    print("PAN Number:", pan)

def container():
    print("======================== Container Data ========================")
    # Load image
    img = Image.open(r"C:\Users\ACER\Downloads\cve test.jpg")

    # Convert image to grayscale
    img = img.convert('L')

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(img, lang="eng")

    # Print the recognized text
    print("text: ", text)

# Function calls
pan()
container()