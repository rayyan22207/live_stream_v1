from django.http import JsonResponse
from .models import Stream
import uuid

def create_stream(request):
    title = request.GET.get("title", "Untitled Stream")
    stream_key = str(uuid.uuid4())
    stream = Stream.objects.create(title=title, stream_key=stream_key)
    return JsonResponse({"id": stream.id, "title": stream.title, "stream_key": stream.stream_key})

def list_streams(request):
    streams = list(Stream.objects.values("id", "title", "stream_key"))
    return JsonResponse({"streams": streams})
