from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class News(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def has_comments(self):
         return self.comment_set.exists() 
    
class Comment(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

