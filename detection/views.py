from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from .forms import ImageUploadForm, CustomUserCreationForm
from .models import ImagePrediction
from .ml_model import DeepfakeDetector
from .utils import preprocess_uploaded_image
import os

def home(request):
    return render(request, 'detection/home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Preprocess image
                image_file = request.FILES['image']
                processed_image = preprocess_uploaded_image(image_file)
                
                # Make prediction
                detector = DeepfakeDetector()
                prediction, confidence = detector.predict(processed_image)
                
                # Save to database
                image_pred = ImagePrediction.objects.create(
                    user=request.user,
                    image=image_file,
                    prediction=prediction,
                    confidence=confidence
                )
                
                return render(request, 'detection/result.html', {
                    'prediction': prediction,
                    'confidence': round(confidence, 2),
                    'image_url': image_pred.image.url
                })
                
            except Exception as e:
                messages.error(request, f'Error processing image: {str(e)}')
    else:
        form = ImageUploadForm()
    
    return render(request, 'detection/upload.html', {'form': form})

@login_required
def history(request):
    predictions = ImagePrediction.objects.filter(user=request.user)
    return render(request, 'detection/history.html', {'predictions': predictions})

def training_stats(request):
    stats_image = os.path.join('static', 'training_history.png')
    context = {
        'stats_available': os.path.exists(stats_image)
    }
    return render(request, 'detection/training_stats.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')