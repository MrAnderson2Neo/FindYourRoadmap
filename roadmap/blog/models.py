from django.db import models
import datetime


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publishTime = models.DateField(default=datetime.time.today)
    textArea =
