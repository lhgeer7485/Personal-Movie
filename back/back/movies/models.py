from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.TextField(primary_key=True)

class Actor(models.Model):
    name = models.TextField(primary_key=True)

class Nation(models.Model):
    name = models.TextField(primary_key=True)

class Director(models.Model):
    name = models.TextField(primary_key=True)

class Type(models.Model):
    name = models.TextField(primary_key=True)

class Movie(models.Model):
    title = models.TextField()
    company = models.TextField()
    prodYear = models.TextField()
    plots = models.TextField()
    runtime = models.TextField()
    rating = models.TextField()
    repRlsDate = models.TextField()
    posters = models.TextField()
    stlls = models.TextField()
    vods = models.TextField()

    type = models.ManyToManyField(Type, related_name='type_movies')
    actors = models.ManyToManyField(Actor, related_name='actor_movies')
    genre = models.ManyToManyField(Genre, related_name='genre_movies')
    nation = models.ManyToManyField(Nation, related_name='nation_movies')
    directors = models.ManyToManyField(Director, related_name='director_movies')

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Upcomming(models.Model):
    title = models.TextField()
    plots = models.TextField()
    posters = models.TextField()
    vods = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='genre_upcomming')
    repRlsDate = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)