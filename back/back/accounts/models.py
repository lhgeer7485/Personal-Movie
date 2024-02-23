from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
SEX_CHOICES = {
        ('남성','남성'),
        ('여성','여성'),
    }
# Create your models here.
class User(AbstractUser):
    
    userid = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=False, default="남성")

    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    # likes = models.ManyToManyField(Movie, symmetrical=False, related_name='like_movies')

