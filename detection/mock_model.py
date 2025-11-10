import random
import numpy as np

class MockDeepfakeDetector:
    def __init__(self):
        self.model = "mock_model"
        
    def predict(self, image_array):
        # Mock prediction - randomly classify as Real or Fake
        confidence = random.uniform(0.6, 0.95)
        result = random.choice(["Real", "Fake"])
        confidence_percent = confidence * 100
        return result, confidence_percent