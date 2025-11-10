from django.test import TestCase
from django.contrib.auth.models import User
from .models import ImagePrediction

class ImagePredictionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_image_prediction_creation(self):
        prediction = ImagePrediction.objects.create(
            user=self.user,
            prediction='Real',
            confidence=85.5
        )
        self.assertEqual(prediction.user, self.user)
        self.assertEqual(prediction.prediction, 'Real')
        self.assertEqual(prediction.confidence, 85.5)