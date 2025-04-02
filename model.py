import torch
from PIL import Image


def load_model(path, device):
    """Load the YOLOv5 model"""
    try:
        model = torch.hub.load("ultralytics/yolov5", "custom", path=path, force_reload=True)
        model.to(device)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def infer_image(image_path, model):
    """Perform inference on an image"""
    model.conf = 0.45  # Confidence threshold
    result = model(image_path)
    result.render()
    img = Image.fromarray(result.ims[0])
    img.save("static/output.jpg")  # Save output
    return "static/output.jpg"
