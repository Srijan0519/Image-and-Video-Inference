from flask import Flask, request, jsonify
import torch
import os
from model import load_model, infer_image
from utils import save_uploaded_file

app = Flask(__name__)

# Load YOLOv5 model
MODEL_PATH = "models/yolov5s.pt"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
model = load_model(MODEL_PATH, DEVICE)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to Object Detection API"})


@app.route("/predict/image", methods=["POST"])
def predict_image():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = save_uploaded_file(file)

    # Run inference
    result_img = infer_image(file_path, model)
    return jsonify({"message": "Prediction complete", "image_path": file_path})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
