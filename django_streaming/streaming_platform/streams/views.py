from django.http import JsonResponse
from .services import create_live_stream, get_stream_details, list_active_streams

def start_stream(request):
    title = request.GET.get("title", "Untitled Stream")
    stream_data = create_live_stream(title)

    # Log the stream_data type and content for debugging
    print(f"Stream Data Type: {type(stream_data)}, Content: {stream_data}")

    if isinstance(stream_data, bytes):
        stream_data = stream_data.decode('utf-8')

    return JsonResponse(stream_data, safe=False)

def view_stream(request, stream_id):
    stream_data = get_stream_details(stream_id)
    return JsonResponse(stream_data)  # Returns details like status, viewer count

def list_streams(request):
    streams = list_active_streams()
    return JsonResponse({"streams": streams})
