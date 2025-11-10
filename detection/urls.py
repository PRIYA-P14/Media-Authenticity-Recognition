from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload_image, name='upload'),
    path('history/', views.history, name='history'),
    path('stats/', views.training_stats, name='training_stats'),
    path('logout/', views.logout_view, name='logout'),
]