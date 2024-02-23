from rest_framework import serializers
from .models import Movie, Genre, Actor, Nation, Director, Type, Upcomming, Comment

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    user= serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('movie','user')

class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = "__all__"

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class NationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        fields = "__all__"

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"

class TypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"

class UpcommingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upcomming
        fields = "__all__"