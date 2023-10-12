from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    
class ImageBackground(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='background_images/')

class Video(models.Model):
    article = models.ForeignKey(Article, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')