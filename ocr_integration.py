from PIL import Image
import pytesseract

# Tesseract executable path (adjust this path if Tesseract is installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Extracts text from the given image using Tesseract OCR.
    :param image_path: Path to the image file
    :return: Extracted text as a string
    """
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        return "Error: Image file not found."
    
    # Enhance the image for better OCR accuracy
    image = image.resize((image.width * 2, image.height * 2), Image.Resampling.LANCZOS)

    # Perform OCR using Tesseract
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text
