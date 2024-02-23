from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, ActorListSerializer, DirectorListSerializer, GenreListSerializer, TypeListSerializer, NationListSerializer, MovieSerializer, UpcommingListSerializer, CommentSerializer
from .models import Movie, Actor, Director, Genre, Nation, Type, Upcomming, Comment
from rest_framework import filters
import urllib
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import JsonResponse
from accounts.models import User
import random
# Create your views here.

# 영화 전체 리스트를 가져오기
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serilaizer = MovieListSerializer(movies, many = True)
        return Response(serilaizer.data)
    

# 영화 디테일 정보를 가져오기
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    if request.method == 'GET':
        serilaizer = MovieSerializer(movie)
        return Response(serilaizer.data)
    
    


# 메인페이지의 박스오피스 정보를 10개까지 가져오기
@api_view(['GET'])
def boxOffice(request):
    boxOfficeList = []
    if request.method == 'GET':
        for idx in range(1,11):
            movie = Movie.objects.get(pk=idx)
            boxOfficeList.append(movie)
        serilaizer = MovieListSerializer(boxOfficeList, many = True)
        return Response(serilaizer.data)
    

# 영화의 포스터를 배열로 가져오기
@api_view(['GET'])
def movie_poster(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie = movie.posters.replace('[',"").replace(']',"").replace("'","")
    movie = movie.split(',')

    if request.method == 'GET':
        serilaizer = MovieSerializer(movie)
        return Response(movie)


# 박스오피스의 영화 포스터를 각자 하나씩만 가져오기
@api_view(['GET'])
def boxOffice_poster(request):
    list = []

    if request.method == 'GET':
        for idx in range(1, 11):
            movie = Movie.objects.get(pk=idx)
            movie = movie.posters.replace('[',"").replace(']',"").replace("'","")
            movie = movie.split(',')
            list.append(movie[0])
        serilaizer = MovieSerializer(list)
        
        return Response(list)

# 한 영화의 이미지와 스틸컷을 각각 전부 배열로 가져오기

@api_view(['GET'])
def movie_detail_image(request, movie_pk):
    
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        poster = movie.posters.replace('[',"").replace(']',"").replace("'","")
        poster = poster.split(',')

        stlls = movie.stlls.replace('[',"").replace(']',"").replace("'","")
        stlls = stlls.split(',')

        detail_data = {
            'poster': poster,
            'stlls': stlls,
        }

        serilaizer = MovieSerializer(detail_data)
        
        return Response(detail_data)


# 메인페이지의 한국 영화 리스트 10개 가져오기
@api_view(['GET'])
def main_korea(request):
    if request.method == 'GET':
        nations = Nation.objects.get(pk="대한민국")
        movies = nations.nation_movies.all()
        
        list = []
        cnt = 0
        for movie in movies:
            if cnt > 9:
                break
            list.append(movie)
            cnt +=1

        serilaizer = MovieListSerializer(list, many = True)
        return Response(serilaizer.data)


# 메인페이지의 해외 영화 리스트 10개 가져오기
@api_view(['GET'])
def main_foreign(request):
    if request.method == 'GET':
        nations = Nation.objects.get(pk="해외영화")
        movies = nations.nation_movies.all()
        
        list = []
        cnt = 0
        for movie in movies:
            if cnt > 9:
                break
            list.append(movie)
            cnt +=1

        serilaizer = MovieListSerializer(list, many = True)
        return Response(serilaizer.data)


# 메인페이지의 애니메이션 리스트 10개 가져오기
@api_view(['GET'])
def main_animation(request):
    if request.method == 'GET':
        types = Type.objects.get(pk="애니메이션")
        movies = types.type_movies.all()
        
        list = []
        cnt = 0
        for movie in movies:
            if cnt > 9:
                break
            list.append(movie)
            cnt +=1

        serilaizer = MovieListSerializer(list, many = True)
        return Response(serilaizer.data)
    

# 메인페이지의 개봉예정 리스트 10개 가져오기
@api_view(['GET'])
def main_upcomming(request):
    if request.method == 'GET':
        upcomming = Upcomming.objects.all()
        
        serilaizer = UpcommingListSerializer(upcomming, many = True)
        return Response(serilaizer.data)
    

# 영화검색
@api_view(['GET'])
def search_movie(request, word):
    w = urllib.parse.unquote(word)
    w = ' ' + w

    movie = Movie.objects.filter(title=w)

    if request.method == 'GET':
        serilaizer = MovieListSerializer(movie, many = True)
        return Response(serilaizer.data)
    
# 댓글 추가
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
        if request.method == 'POST':
            serializer = CommentSerializer(data = request.data)
            mv = Movie.objects.get(pk=movie_pk)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user,movie=mv)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            

# 댓글 삭제
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
    if request.method == 'DELETE':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if not movie.like_users.filter(pk=request.user.pk):
        movie.like_users.add(request.user)
        is_liked = True
    else:
        movie.like_users.remove(request.user)
        is_liked = False

    movie.save()

    context = {
        'is_liked': is_liked,
        'likes_count': movie.like_users.count()
    }

    return JsonResponse(context)


# 카테고리 탭 부분에 사용되는 것들
# -----------------------------------------------------------------------------


# 한국영화 전체
@api_view(['GET'])
def koreaMovie(request):
    if request.method == 'GET':
        nations = Nation.objects.get(pk="대한민국")
        movies = nations.nation_movies.all()

        serilaizer = MovieListSerializer(movies, many = True)
        return Response(serilaizer.data)
    

# 일본영화 전체
@api_view(['GET'])
def japanMovie(request):
    if request.method == 'GET':
        nations = Nation.objects.get(pk="일본")
        movies = nations.nation_movies.all()

        serilaizer = MovieListSerializer(movies, many = True)
        return Response(serilaizer.data)
    

# 중국영화 전체
@api_view(['GET'])
def chinaMovie(request):
    if request.method == 'GET':
        nations = Nation.objects.get(pk="중국")
        movies = nations.nation_movies.all()

        serilaizer = MovieListSerializer(movies, many = True)
        return Response(serilaizer.data)


# 해외영화 전체
@api_view(['GET'])
def foreignMovie(request):
    if request.method == 'GET':
        nations = Nation.objects.get(pk="해외영화")
        movies = nations.nation_movies.all()

        serilaizer = MovieListSerializer(movies, many = True)
        return Response(serilaizer.data)
    


# 장르 전체 리스트를 가져오기
@api_view(['GET'])
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        
        list = []
        for gen in genres:

            list.append(gen.name)
        print(list)
        context = { 
            'list': list[:-2],
        }

        return JsonResponse(context, json_dumps_params={'ensure_ascii': False})


# 해당 장르 영화 가져오기
@api_view(['GET'])
def genre_get(request, genre):
    w = urllib.parse.unquote(genre)

    gen = Genre.objects.filter(name=w)
    print(gen[0])
    g = gen[0].genre_movies.all()

    if request.method == 'GET':
        serilaizer = MovieListSerializer(g, many = True)
        return Response(serilaizer.data)
    

# 애니메이션 전체
@api_view(['GET'])
def animationMovie(request):
    if request.method == 'GET':
        typs = Type.objects.get(pk="애니메이션")
        movies = typs.type_movies.all()

        serilaizer = MovieListSerializer(movies, many = True)
        return Response(serilaizer.data)

# 다큐멘터리 전체
@api_view(['GET'])
def documentaryMovie(request):
    if request.method == 'GET':
        typs = Type.objects.get(pk="다큐멘터리")
        movies = typs.type_movies.all()

        serilaizer = MovieListSerializer(movies, many = True)
        return Response(serilaizer.data)
    

# (실황)공연물 전체
@api_view(['GET'])
def liveMovie(request):
    if request.method == 'GET':
        typs = Type.objects.get(pk="(실황)공연물")
        movies = typs.type_movies.all()

        serilaizer = MovieListSerializer(movies, many = True)
        return Response(serilaizer.data)
    
# 극영화 전체
@api_view(['GET'])
def nomalMovie(request):
    if request.method == 'GET':
        typs = Type.objects.get(pk="극영화")
        movies = typs.type_movies.all()

        serilaizer = MovieListSerializer(movies, many = True)
        return Response(serilaizer.data)
    

# 댓글 순 추천
@api_view(['GET'])
def algo_comment(request):
    comment = Comment.objects.all()

    dic = {}

    result = []
    
    for com in comment:
        mv = com.movie
        cnt = mv.comment_set.all().count()
        
        if mv.id in dic:
            dic[mv.id] += 1
        else:
            dic[mv.id] = 1
    
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for data in dic:
        movie_id = data[0]
        movie = Movie.objects.get(pk=movie_id)

        poster = movie.posters.replace('[',"").replace(']',"").replace("'","")
        poster = poster.split(',')

        obj = {
            'id': movie.id,
            'title': movie.title,
            'poster': poster[0]
        }

        result.append(obj)

    while(len(result)<=10):
        idx = random.randrange(0, 181)
        
        movie = Movie.objects.get(pk=idx)
        poster = movie.posters.replace('[',"").replace(']',"").replace("'","")
        poster = poster.split(',')

        if not movie in result:
            obj = {
                'id': movie.id,
                'title': movie.title,
                'poster': poster[0]
            }
            result.append(obj)

    context = {
        'result': result,
    }

    return JsonResponse(context, json_dumps_params={'ensure_ascii': False})


# 좋아요 순 추천
@api_view(['GET'])
def algo_like(request):
    users = User.objects.all()

    dic = {}

    result = []
    
    for user in users:
        mvs = user.like_movies.all()

        for mv in mvs:
        
        
            if mv.id in dic:
                dic[mv.id] += 1
            else:
                dic[mv.id] = 1
        
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        for data in dic:
            movie_id = data[0]
            movie = Movie.objects.get(pk=movie_id)

            poster = movie.posters.replace('[',"").replace(']',"").replace("'","")
            poster = poster.split(',')

            obj = {
                'id': movie.id,
                'title': movie.title,
                'poster': poster[0]
            }

            result.append(obj)

    while(len(result)<=10):
        idx = random.randrange(0, 181)
        
        movie = Movie.objects.get(pk=idx)
        poster = movie.posters.replace('[',"").replace(']',"").replace("'","")
        poster = poster.split(',')

        if not movie in result:
            obj = {
                'id': movie.id,
                'title': movie.title,
                'poster': poster[0]
            }
            result.append(obj)

    context = {
        'result': result,
    }

    return JsonResponse(context, json_dumps_params={'ensure_ascii': False})


# 각 연령대별 좋아요순으로 정렬한 리스트
# 각 성별 좋아요순으로 정렬한 리스트
# 2개의 리스트에서 사용자의 연령대와 성별에 맞는 영화를 골라서
# 해당 연령대와 성별의 좋아요 top 30중에서 중복되는것을 최우선 순위로 추천하고
# 나머지 영화는 연령대와 성별 각각의 top 10에서 가져와 최대 10개 영화를 추천하는 리스트를 완성한다.
# 그래도 10개 미만이거나 좋아요가 없다면 기본적으로는 랜덤으로 영화를 추가한다.
@api_view(['GET'])
def recommend(request):
    # users = User.objects.all()

    age_list = ['10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대', '90대']
    # 해당 연령대가 좋아하는 영화 리스트
    age_movies = [0] * 9

    for idx in range(len(age_list)):
        # 연령대의 유저를 모두 구하고
        age_dic = {}
        age_users = User.objects.filter(age=age_list[idx])
        for age_user in age_users:
            # 각 연령대의 유저들이 좋아하는 영화 전체를 리스트에 저장
            # age_movies[idx] = age_user.like_movies.all()
            for a in age_user.like_movies.all():
                if a.id in age_dic:
                    age_dic[a.id] += 1
                else:
                    age_dic[a.id] = 1

        # 좋아요순으로 정렬
        age_dic = sorted(age_dic.items(), key=lambda x: x[1], reverse=True)          
        age_movies[idx] = age_dic


    gender_list = ['남성', '여성']
    # 해당 성별이 좋아하는 영화 리스트
    gender_movies = [0] * 2
    
    for idx in range(len(gender_list)):
        # 각 성별의 유저를 모두 구하고
        gender_dic = {}
        gender_users = User.objects.filter(sex=gender_list[idx])
        for gender_user in gender_users:
            # 각 성별의 유저들이 좋아하는 영화 전체를 리스트에 저장
            # gender_movies[idx] = gender_user.like_movies.all()
            for a in gender_user.like_movies.all():
                if a.id in gender_dic:
                    gender_dic[a.id] += 1
                else:
                    gender_dic[a.id] = 1
        # 좋아요순으로 정렬                    
        gender_dic = sorted(gender_dic.items(), key=lambda x: x[1], reverse=True)
        gender_movies[idx] = gender_dic


    me = request.user

    print(me)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    age_idx = int(me.age[:1])-1
    # try: age_idx = int(me.age[:1])-1
    # except: AttributeError
        

    if me.sex == '남성':
        gender_idx = 0
    else:
        gender_idx = 1
    
    result = []

    list = []

    if len(age_movies[age_idx]) > 30:
        age_movies[age_idx] = age_movies[age_idx][:30]

    for k, v in age_movies[age_idx]:
        movie = Movie.objects.get(pk=k)
        result.append(movie)

    if len(gender_movies[gender_idx]) > 30:
        gender_movies[gender_idx] = gender_movies[gender_idx][:30]

    for k, v in gender_movies[gender_idx]:
        movie = Movie.objects.get(pk=k)
        # 중복을 최우선으로
        if movie in result:
            list.append(movie)          
            continue
        result.append(movie)

    a = len(age_movies[age_idx])
    b = len(gender_movies[gender_idx])

    if a > b:
        c = b
        rest = age_movies[age_idx]
    else:
        c = a
        rest = gender_movies[gender_idx]

    for idx in range(0, c):
        if len(list) > 10:
            break

        k, v = age_movies[age_idx][idx]
        movie = Movie.objects.get(pk=k)
        if not movie in list:
            list.append(movie)

        k, v = gender_movies[gender_idx][idx]
        movie = Movie.objects.get(pk=k)
        if not movie in list:
            list.append(movie)

    if len(list) <= 10:
        for idx in range(c, len(rest)):
            if len(list) > 10:
                break
            k, v = rest[idx]
            movie = Movie.objects.get(pk=k)
            list.append(movie)


    while(len(list)<=10):
        idx = random.randrange(0, 181)

        movie = Movie.objects.get(pk=idx)
        if not movie in list:
            list.append(movie)

    serilaizer = MovieListSerializer(list, many = True)
    return Response(serilaizer.data)


@api_view(['GET'])
def worldcup(request):
    list = []
    check = set()

    while(len(list) < 16):
        idx = random.randrange(1, 198)
        movie = Movie.objects.get(pk=idx)

        if not movie in check:
            check.add(movie)
        else:
            continue
        
        poster = movie.posters.replace('[',"").replace(']',"").replace("'","")
        poster = poster.split(',')
        print(poster[0])
        if len(poster[0]) < 4:
            continue
        list.append(movie)

    serilaizer = MovieListSerializer(list, many = True)
    return Response(serilaizer.data)



@api_view(['GET'])
def worldcup_genre(request, movie_pk):
    list = []
    movie = Movie.objects.get(pk=movie_pk)
    genres = movie.genre.all()

    for gen in genres:
        if gen.name == 'no':
            continue
        genre = Genre.objects.get(pk=gen.name)
        idx = 1
        for g in genre.genre_movies.all():
            if idx > 10:
                break
            if g in list:
                continue
            if g == movie:
                continue            
            list.append(g)
            idx += 1
 
    serilaizer = MovieListSerializer(list, many = True)
    return Response(serilaizer.data)


@api_view(['GET'])
def worldcup_director(request, movie_pk):
    list = []
    movie = Movie.objects.get(pk=movie_pk)
    directors = movie.directors.all()

    for di in directors:
        director = Director.objects.get(pk=di.name)
        idx = 1
        for d in director.director_movies.all():
            if idx > 3:
                break
            if d in list:
                continue
            # if d == movie:
            #     continue            
            list.append(d)
            idx += 1
 
    serilaizer = MovieListSerializer(list, many = True)
    return Response(serilaizer.data)


@api_view(['GET'])
def worldcup_actor(request, movie_pk):
    list = []
    movie = Movie.objects.get(pk=movie_pk)
    actors = movie.actors.all()
    i = 0
    for ac in actors:
        if i > 10:
            break
        actor = Actor.objects.get(pk=ac.name)
        idx = 1
        for a in actor.actor_movies.all():
            if idx > 3:
                break
            if a in list:
                continue
            if a == movie:
                continue

            list.append(a)
            idx += 1
        i += 1

    serilaizer = MovieListSerializer(list, many = True)
    return Response(serilaizer.data)
