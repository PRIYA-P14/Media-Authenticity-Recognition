from django.contrib import admin
from .models import ImagePrediction

@admin.register(ImagePrediction)
class ImagePredictionAdmin(admin.ModelAdmin):
    list_display = ['user', 'prediction', 'confidence', 'created_at']
    list_filter = ['prediction', 'created_at']
    search_fields = ['user__username']
    readonly_fields = ['created_at']