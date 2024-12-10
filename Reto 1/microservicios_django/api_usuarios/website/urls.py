from django.urls import path
from . import views

urlpatterns = [
    path('csv/upload/', views.upload_csv, name='upload_csv'),
]