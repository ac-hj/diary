from django.db import models
from django.contrib.auth.models import User

# Creating Diary DB
class Diary(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    # this links the diary model to the user model
    # so when you delete users, you need to delete 
    # that user's diary entries first
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
