from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    post_title      = models.CharField('Post Title',max_length=255)
    pub_date        = models.DateTimeField("Date Published: ")
    post_contents   = models.CharField('Post Contents',max_length=10000)
    post_likes      = models.IntegerField('Number of likes',default=0)
    
    def __str__(self):
        return self.post_title
    
class CommentOnPost(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.CharField('Name', max_length=50, default='Anonymous')
    comment_contents = models.TextField()
    pub_date        = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Comment Left by {self.name} on {self.post.post_title}'