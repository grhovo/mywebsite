from django.db import models

# Create your models here.
class Videos(models.Model):
    video_name = models.CharField( "Video Name" , max_length = 200)
    video_description = models.TextField( 'Video description' )
    video_path = models.CharField( "Video Link" , max_length = 200)
