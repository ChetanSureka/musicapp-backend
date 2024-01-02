from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('watch/<str:videoId>/<str:title>/', Video),
    path('search/', home)
]
