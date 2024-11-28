import os
from flask import Flask, request, render_template, jsonify
from ocr_integration import extract_text_from_image  # Import OCR function here
from grading_rubrics import grade_submission

app = Flask(__name__)

# Example rubric
rubric = [
    {"question": "Define Python.", "ideal_answer": "Python is a high-level programming language."},
    {"question": "Explain semantic similarity.", "ideal_answer": "Semantic similarity measures the closeness in meaning between two texts."}
]

UPLOAD_FOLDER = "./uploads"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    # Ensure the upload folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    image = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    # Extract text using OCR
    extracted_text = extract_text_from_image(image_path)

    # Grade the extracted text
    results = grade_submission(extracted_text, rubric)

    return render_template('results.html', results=results, extracted_text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True)
