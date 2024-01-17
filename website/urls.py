
from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from homepage.api import api 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("homepage.urls")),
    path("api/", api.urls),
  # Include the homepage app's API endpoints
]