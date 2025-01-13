from django.db import models

# Create your models here.

class Post (models.Model):

    Title = models.CharField (max_length=40)
    Bio = models.TextField ()
    Image = models.ImageField (upload_to='Post_Picture')

    def __str__(self):
        return self.Title