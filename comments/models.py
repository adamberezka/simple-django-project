from django.db import models
from news.models import News


class Comment(models.Model):
    author = models.CharField(max_length=200)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    create_time = models.DateTimeField('create time')
