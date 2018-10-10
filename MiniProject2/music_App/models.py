from django.db import models


class SubmissionModel(models.Model):
    songName = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    duration = models.CharField(default=0, max_length=5)
    rating = models.IntegerField(default=0)


def __str__(self):
    return self.songName
