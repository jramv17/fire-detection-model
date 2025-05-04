# app.py
from flask import Flask, request, jsonify, send_file
import os
from fire_model import detect_fire
from PIL import Image
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("static/results", exist_ok=True)

@app.route("/api/detect-fire", methods=["POST"])
def detect_fire_api():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files['image']
    filename = f"{uuid.uuid4().hex}.jpg"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    image_file.save(file_path)

    result = detect_fire(file_path)

    return jsonify({
        "fire_detected": result["fire_detected"],
        "fire_percentage": result["fire_percentage"],
        "image_result_url": request.host_url + result["image_path"]
    })

if __name__ == "__main__":
    app.run(debug=True)
