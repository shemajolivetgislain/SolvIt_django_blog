from django.db import models
from firstblog.models import Blog
from django.contrib.auth import get_user_model
User=get_user_model()
import uuid
# Create your models here.
class Comment(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    comment_by=models.ForeignKey(User,related_name="user_comment",on_delete=models.CASCADE)
    comment_content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)