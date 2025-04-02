import streamlit as st
import torch
import cv2
import time
import os
from PIL import Image

st.set_page_config(layout="wide")

# Default model path
MODEL_PATH = 'models/yolov5s.pt'
CONFIDENCE_THRESHOLD = 0.25

def image_input():
    img_bytes = st.sidebar.file_uploader("Upload an image", type=['png', 'jpeg', 'jpg'])
    if img_bytes:
        img_file = "data/uploaded_data/upload." + img_bytes.name.split('.')[-1]
        Image.open(img_bytes).save(img_file)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(img_file, caption="Uploaded Image")
        with col2:
            img = infer_image(img_file)
            st.image(img, caption="Model Prediction")

def video_input():
    vid_bytes = st.sidebar.file_uploader("Upload a video", type=['mp4', 'mpv', 'avi'])
    if vid_bytes:
        vid_file = "data/uploaded_data/upload." + vid_bytes.name.split('.')[-1]
        with open(vid_file, 'wb') as out:
            out.write(vid_bytes.read())
        
        cap = cv2.VideoCapture(vid_file)
        fps = 0
        st1, st2, st3 = st.columns(3)
        with st1:
            st.markdown("## Height")
        with st2:
            st.markdown("## Width")
        with st3:
            st.markdown("## FPS")

        st.markdown("---")
        output = st.empty()
        prev_time = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                st.write("Can't read frame, stream ended? Exiting ....")
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output_img = infer_image(frame)
            output.image(output_img)
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if prev_time else 0
            prev_time = curr_time

        cap.release()

def infer_image(img):
    model.conf = CONFIDENCE_THRESHOLD
    result = model(img)
    result.render()
    return Image.fromarray(result.ims[0])

@st.cache_resource
def load_model(path):
    try:
        model_ = torch.hub.load('ultralytics/yolov5', 'custom', path=path, force_reload=True)
        model_.to('cuda' if torch.cuda.is_available() else 'cpu')
        st.success("Model loaded successfully.")
        return model_
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def main():
    global model
    
    st.title("Object Recognition Dashboard")
    st.sidebar.title("Settings")
    
    model = load_model(MODEL_PATH)
    confidence = st.sidebar.slider('Confidence', min_value=0.1, max_value=1.0, value=CONFIDENCE_THRESHOLD)
    
    input_option = st.sidebar.radio("Select input type:", ['image', 'video'])
    
    if input_option == 'image':
        image_input()
    else:
        video_input()

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass


