from django.urls import path
from streams.views import create_stream, list_streams

urlpatterns = [
    path('create_stream/', create_stream),
    path('list_streams/', list_streams),
]
