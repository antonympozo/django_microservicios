from django.contrib import admin
from django.urls import path, include
from users.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', include('website.urls')),  # Añade esta línea
]