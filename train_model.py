#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'media_auth.settings')
django.setup()

from detection.ml_model import DeepfakeDetector

def main():
    print("Starting model training...")
    
    # Initialize detector
    detector = DeepfakeDetector()
    detector.build_model()
    
    # Print model summary
    detector.model.summary()
    
    # Note: You need to download and organize the Kaggle dataset
    # Dataset structure should be:
    # dataset/
    #   train/
    #     real/
    #     fake/
    #   validation/
    #     real/
    #     fake/
    
    train_dir = 'dataset/train'
    val_dir = 'dataset/validation'
    
    if not os.path.exists(train_dir) or not os.path.exists(val_dir):
        print("Dataset not found!")
        print("Please download the Kaggle Deepfake Image Detection dataset")
        print("and organize it in the following structure:")
        print("dataset/")
        print("  train/")
        print("    real/")
        print("    fake/")
        print("  validation/")
        print("    real/")
        print("    fake/")
        return
    
    # Train the model
    history = detector.train_model(train_dir, val_dir, epochs=20)
    print("Training completed!")
    print("Model saved as models/deepfake_model.h5")

if __name__ == '__main__':
    main()