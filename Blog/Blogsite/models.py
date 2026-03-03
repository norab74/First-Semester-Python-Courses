from django.db import models

# Create your models here.
class BlogPost(models.Model):
    '''
    Represents a blog post with an image and timestamps
    '''
    post_title = models.CharField(max_length=255)
    post_contents = models.TextField()
    post_image = models.ImageField(upload_to='postImages/')
    post_created_at = models.DateTimeField(auto_now_add=True)
    post_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''
        Returns a string representation of a post, its title
        '''
        return self.post_title

    def edit(self, post_title, post_contents, post_image)
        '''
        Passes args to self.%arg% to allow for the updating
        of posts and their contents, saves after executing
        '''
        self.post_title = post_title
        self.post_contents = post_contents
        self.post_image = post_image
        self.save()
    def shortened_post_contents(self):
        '''
        If a post is longer than 50 words, get the first 30
        and append an ellipsis.
        '''
        contents = self.post_contents.split()
        if len(contents) > 50:
            return ' '.join(contents[:30]) + '...'
        else:
            return self.description

