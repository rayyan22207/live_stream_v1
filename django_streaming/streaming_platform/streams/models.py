from django.db import models

class Stream(models.Model):
    title = models.CharField(max_length=255)
    stream_key = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
