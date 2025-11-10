# Media Authenticity Recognition System

A Django-based web application that uses CNN to detect fake/deepfake images.

## Features

- User authentication (signup, login, logout)
- Image upload and preprocessing
- CNN-based fake image detection
- Prediction history tracking
- Training statistics visualization
- Admin panel for monitoring

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Database Setup
- Install MySQL and create database `media_auth_db`
- Update database credentials in `media_auth/settings.py`

### 3. Django Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Dataset Preparation
- Download Kaggle Deepfake Image Detection dataset
- Organize in this structure:
```
dataset/
  train/
    real/
    fake/
  validation/
    real/
    fake/
```

### 5. Train Model
```bash
python train_model.py
```

### 6. Run Server
```bash
python manage.py runserver
```

## Usage

1. Register/Login to the system
2. Upload an image (JPG/PNG)
3. View prediction result with confidence score
4. Check prediction history
5. View training statistics

## Model Architecture

- CNN with 3 Conv2D layers
- MaxPooling and Dropout for regularization
- Binary classification (Real/Fake)
- Input size: 128x128x3
- Data augmentation for training

## API Endpoints

- `/` - Home page
- `/signup/` - User registration
- `/auth/login/` - User login
- `/upload/` - Image upload and prediction
- `/history/` - Prediction history
- `/stats/` - Training statistics
- `/admin/` - Admin panel

## Technologies Used

- Django 4.2.7
- TensorFlow 2.13.0
- OpenCV 4.8.1
- Bootstrap 5
- MySQL
- Matplotlib for visualization