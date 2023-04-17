from django.db import models
from imagekit.processors import Thumbnail, ResizeToFill, SmartResize
from imagekit.models import ProcessedImageField, ImageSpecField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    thumbnail_img = ProcessedImageField(
        blank = True,
        upload_to = 'thumbnail/',
        processors=[Thumbnail(1500, 1000)],  # 200x300파일로 줄이기
        format='JPEG',
        options={'quality': 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)