from django.forms import ModelForm
from .models import Song

class SongFrom(ModelForm):
    class Meta:
        model= Song
        fields= [
            'danceablity',
            'energy',
            'key',
            'loudness',
            'valence',
            'speechiness',
            'acounticness',
            'instrumentalness',
            'liveness',
            'tempo',
            'duration_ms',
            'time_signature'
        ]