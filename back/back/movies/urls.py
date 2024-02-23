from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    # 영화 전체 리스트를 가져오기
    path('', views.movie_list, name='movie_list'),

    # 영화 디테일 정보를 가져오기
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),



    # 장르 리스트를 가져오기
    path('genre/', views.genre_list, name='genre_list'),

    # 해당 장르 영화 전체 가져오기 
    path('genre/<str:genre>/', views.genre_get, name='genre_get'),    




    # 메인페이지의 박스오피스 정보를 10개까지 가져오기
    path('boxOffice/', views.boxOffice, name='boxOffice'),

    # 메인페이지의 한국 영화 리스트 10개 가져오기
    path('main/korea/', views.main_korea, name='main_korea'),

    # 메인페이지의 해외 영화 리스트 10개 가져오기
    path('main/foreign/', views.main_foreign, name='main_foreign'),

    # 메인페이지의 애니메이션 리스트 10개 가져오기
    path('main/animation/', views.main_animation, name='main_animation'),

    # 메인페이지의 개봉예정 리스트 10개 가져오기
    path('main/upcomming/', views.main_upcomming, name='main_upcomming'),



    # 한국영화 카테고리 영화 전체를 가져오기
    path('category/kr/', views.koreaMovie, name='koreaMovie'),

    # 일본영화 카테고리 영화 전체를 가져오기
    path('category/jp/', views.japanMovie, name='japanMovie'),

    # 중국영화 카테고리 영화 전체를 가져오기
    path('category/cn/', views.chinaMovie, name='chinaMovie'),

    # 해외영화 카테고리 영화 전체를 가져오기
    path('category/fg/', views.foreignMovie, name='foreignMovie'),

    # 애니메이션 카테고리 영화 전체를 가져오기
    path('category/ani/', views.animationMovie, name='animationMovie'),

    # 다큐멘터리 카테고리 영화 전체를 가져오기
    path('category/doc/', views.documentaryMovie, name='documentaryMovie'),
        
    # (실황)공연물 카테고리 영화 전체를 가져오기
    path('category/live/', views.liveMovie, name='liveMovie'),

    # 극영화 카테고리 영화 전체를 가져오기
    path('category/nomal/', views.nomalMovie, name='nomalMovie'),

    # 영화의 포스터를 배열로 가져오기
    path('<int:movie_pk>/movie_poster/', views.movie_poster, name='movie_poster'),

    # 한 영화의 이미지와 스틸컷을 각각 전부 배열로 가져오기
    path('<int:movie_pk>/image/', views.movie_detail_image, name='movie_detail_image'),

    # 박스오피스의 영화 포스터를 각자 하나씩만 가져오기
    path('boxOffice_poster/', views.boxOffice_poster, name='boxOffice_poster'),


    # 검색기능 (영화) 
    path('searchMovie/<str:word>/', views.search_movie, name='search_movie'),

    # 댓글 관련
    path('comment/<int:movie_pk>/', views.comment_create, name='comment_create'),

    # 댓글 삭제
    path('comment/delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),

    # 영화 좋아요
    path('like/<int:movie_pk>/', views.like, name='like'),

    # 댓글순 추천 알고리즘
    path('algo/comment/', views.algo_comment, name='algo_comment'),

    # 좋아요순 추천 알고리즘
    path('algo/like/', views.algo_like, name='algo_like'),

    # 추천알고리즘
    path('recommend/', views.recommend, name='recommend'),

    # 월드컵
    path('worldcup/', views.worldcup, name='worldcup'),

    # 월드컵 결과
    path('worldcup/<int:movie_pk>/genre/', views.worldcup_genre, name='worldcup_genre'),
    path('worldcup/<int:movie_pk>/director/', views.worldcup_director, name='worldcup_director'),
    path('worldcup/<int:movie_pk>/actor/', views.worldcup_actor, name='worldcup_actor'),

    ]
