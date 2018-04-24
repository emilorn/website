from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=120)
    albumTitle= models.CharField(max_length=120)
    genre = models.CharField(max_length=50)
    albumLogo=models.CharField(max_length=1000)

    def __str__(self):
        return self.albumTitle + ' - ' + self.artist

class Song(models.Model):
    album =  models.ForeignKey(Album,on_delete=models.CASCADE)
    fileType = models.CharField(max_length=10)
    songTitle = models.CharField(max_length=250)

    def __str__(self):
        return self.songTitle