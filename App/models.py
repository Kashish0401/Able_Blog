from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class PostModel(models.Model):
  title =  models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
  date_created = models.DateTimeField(auto_now_add=True)
  content = models.TextField()
  

  class Meta:
    ordering = ['date_created']

  def __str__(self):
    return self.title
