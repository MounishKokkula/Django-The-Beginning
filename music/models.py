from django.db import models

# Create your models here.
# creates a primary key by default for each table
# when you declare a foreign key it is associated with the primary key
class Album(models.Model):
    artist = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 100)
    album_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.album_title + self.album_logo

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
