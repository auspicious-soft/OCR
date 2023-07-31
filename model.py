import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Load the image and convert it to grayscale
img = cv2.imread('MicrosoftTeams-image (12).tiff')
# Perform OCR using pytesseract
text = pytesseract.image_to_string(img, lang="eng")
print(text)
