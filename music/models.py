from django.db import models    
from django.contrib.auth.models import Permission, User

class Album(models.Model):
    user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(upload_to='music/images')
    is_favorite = models.BooleanField(default=False)  
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album       = models.ForeignKey(Album, on_delete=models.CASCADE)
    audio_file  = models.FileField(upload_to='music/songs')
    song_title  = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title