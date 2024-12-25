from django.urls import path
from .views import start_stream, view_stream, list_streams

urlpatterns = [
    path('start_stream/', start_stream),
    path('view_stream/<stream_id>/', view_stream),
    path('list_streams/', list_streams),
]
