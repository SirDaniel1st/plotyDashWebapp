from django.db import models

# Create your models here.
from django.db import models

class Song(models.Model):
    danceablity=models.FloatField()
    energy=models.FloatField()
    key=models.FloatField()
    loudness=models.FloatField()
    valence=models.FloatField()
    speechiness=models.FloatField()
    acounticness=models.FloatField()
    instrumentalness=models.FloatField()
    liveness=models.FloatField()
    tempo=models.FloatField()
    duration_ms=models.FloatField()
    time_signature=models.FloatField()

    def DataRetrun(self):
        return self.danceablity , self.energy,self.key,self.loudness,self.valence,self.speechiness,self.acounticness,self.instrumentalness,self.liveness,self.tempo,self.duration_ms,self.time_signature
