from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .serializer import UserSerializer
from .forms import CostomUserCreationForm
from .models import User
from django.http import JsonResponse

# Create your views here.
@api_view(['POST'])
def signup(request):
    form = CostomUserCreationForm(request.data)
    if form.is_valid():
        form.save()
        return Response(status=201)
    else:
        return Response(form.errors)
    

# 마이페이지
@api_view(['GET'])
def info(request, user_pk):
    user = User.objects.get(pk=user_pk)

    movies = user.like_movies.all()

    like_movies = []
    
    for movie in movies:
        obj = {
            'title': movie.title,
            'id': movie.id,
            'poster': movie.posters.replace('[',"").replace(']',"").replace("'","").split(',')[0].replace('"',""),
        }
        like_movies.append(obj)

    context = {
        'user_name': user.username,
        'user_pk': user.id,
        'user_email': user.userid,
        'user_date_joined': str(user.date_joined)[:10],
        'user_age': str(user.age),
        'user_sex': user.sex,

        'like_movies': like_movies,
    }
    
    return JsonResponse(context, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def myinfo(request):
    user = request.user

    movies = user.like_movies.all()
    print(movies)
    print("dddd")
    like_movies = []
    
    for movie in movies:
        obj = {
            'title': movie.title,
            'id': movie.id,
            'poster': movie.posters.replace('[',"").replace(']',"").replace("'","").split(',')[0].replace('"',""),
        }
        like_movies.append(obj)

    context = {
        'user_name': user.username,
        'user_pk': user.id,
        'user_email': user.userid,
        'user_date_joined': str(user.date_joined)[:10],
        'user_age': str(user.age),
        'user_sex': user.sex,

        'like_movies': like_movies,
    }
    
    return JsonResponse(context, json_dumps_params={'ensure_ascii': False})