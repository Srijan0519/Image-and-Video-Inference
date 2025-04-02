# Image-and-Video-Inference
An app for image and video inferencing using YOLO

# Object Recognition Dashboard

This is a Streamlit-based Object Recognition Dashboard that uses the YOLOv5s model for detecting objects in images and videos uploaded by users.

## Running the App

Run the Streamlit application:
```sh
streamlit run main_app.py
```

## Usage
1. Upload an image (`.png`, `.jpeg`, `.jpg`) or a video (`.mp4`, `.mpv`, `.avi`).
2. Adjust the confidence slider to set the detection threshold.
3. View the processed image/video with detected objects.

## Output
![image](https://github.com/Srijan0519/Image-and-Video-Inference/blob/main/output/Screenshot%202025-04-02%20153237.jpg)

## Dependencies
- Python 3.7+
- Streamlit
- OpenCV
- PIL (Pillow)
- Torch
- Ultralytics YOLOv5

## Future Modifications
- Containerisation and orchestration of the app
- Deployment on on a web-based interface


