import requests
from django.conf import settings

ANT_MEDIA_BASE_URL = settings.ANT_MEDIA_SERVER_URL

# def create_live_stream(title):
#     url = f"{ANT_MEDIA_BASE_URL}/rest/v2/broadcasts/create"  # Ensure this uses http://
#     payload = {"name": title, "type": "liveStream"}
#     response = requests.post(url, json=payload, auth=("rayyan22207@gmail.com", "password"))  # Replace with your Ant Media credentials
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": response.content}
    
def create_live_stream(title):
    url = f"{ANT_MEDIA_BASE_URL}/rest/v2/broadcasts/create"
    payload = {"name": title, "type": "liveStream"}
    response = requests.post(url, json=payload, auth=("rayyan22207@gmail.com", "password"))  # Replace credentials
    
    if response.status_code == 200:
        return response.json()  # Ensure this returns a dictionary
    else:
        return {"error": response.content.decode('utf-8')}  # Decode error response



def get_stream_details(stream_id):
    url = f"{ANT_MEDIA_BASE_URL}/rest/v2/broadcasts/{stream_id}"
    response = requests.get(url, auth=("rayyan22207@gmail.com", "password"))
    return response.json()

def list_active_streams():
    url = f"{ANT_MEDIA_BASE_URL}/rest/v2/broadcasts/list"
    response = requests.get(url, auth=("rayyan22207@gmail.com", "password"))
    return response.json()
