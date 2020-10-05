from djongo import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField()

    def __str__(self):
        return self.text

class Like(models.Model):
    user_email = models.EmailField(blank=True)


class Posts(models.Model):
    author = models.EmailField()
    author_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = RichTextUploadingField(blank=True,null=True)
    created_on = models.DateTimeField()
    comments_count = models.IntegerField(blank=True)
    comments = models.ArrayModelField(
        model_container = Comment,
    )
    likes_count = models.IntegerField(blank=True)
    likes = models.ArrayModelField(
        model_container = Like,
    )

    def __str__(self):
        return self.title

