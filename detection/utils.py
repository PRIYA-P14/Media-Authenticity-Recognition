import numpy as np
from PIL import Image
try:
    import cv2
    import tensorflow as tf
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

def preprocess_image(image_path):
    """Preprocess image for model prediction"""
    if not CV2_AVAILABLE:
        raise ImportError("OpenCV is not installed. Please install it with: pip install opencv-python")
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def preprocess_uploaded_image(uploaded_file):
    """Preprocess uploaded Django file for prediction"""
    img = Image.open(uploaded_file)
    img = img.convert('RGB')
    img = img.resize((128, 128))
    img_array = np.array(img)
    img_array = img_array.astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array