## Personal Movie - 영화 추천 웹 서비스

## 1. 팀원 및 업무 분담
> ![image.png](./image.png)
> - Back-end와 Front-end를 업무 분담하여 프로젝트에 참여하였습니다.  
  


## 2. 서비스 구현
> ![image-1.png](./image-1.png)

> - 처음 입장 화면  




> ![image-2.png](./image-2.png)

> - 회원가입 페이지
> - 처음 입장 시 회원가입 필요
> - 아이디, 이메일, 비밀번호, 나이, 성별을 입력
> - 회원가입 시 자동 로그인  




> ![image-3.png](./image-3.png)

> - 로그인 페이지  




> ![image-4.png](./image-4.png)

> - 메인 페이지
> - 케러셀을 이용하여 자동으로 포스터가 움직이게 만들었습니다.
> - 모든 포스터 클릭 시 영화 상세정보 화면으로 이동합니다.
> - Today BoxOffice : 그날의 영화관 박스오피스 TOP 10을 보여준다.
> - UpComing Movie : 개봉 예정 영화 10개의 목록을 보여준다.
> - Korea Movie : 한국 영화 10개의 목록을 보여준다.
> - Foregin Movie : 해외 영화 10개의 목록을 보여준다.
> - Animation Movie : 애니메이션 영화 10개의 목록을 보여준다.  




> ![image-5.png](./image-5.png)

> - 마이 페이지
> - 유저의 기본 정보와 찜한 영화의 목록을 보여준다.  




> ![image-6.png](./image-6.png)

> - 검색창
> - 검색어 입력 시, 일치하는 영화의 상세정보 화면으로 이동한다.
> - 일치하는 정보가 없는 경우, 알림창을 보여준다.  




> ![image-7.png](./image-7.png)
> ![image-8.png](./image-8.png)

> - 영화 상세정보 페이지
> - [예고편 보러가기] 클릭 시, 영화의 티져 영상을 모달을 통해 보여준다.
> - 찜 버튼 클릭 시, 좋아요가 적용된다.
> - #태그 클릭 시, 해당 태그의 전체 영화 목록 페이지로 이동한다.
> - 댓글 적성 및 삭제 가능  




> ![image-9.png](./image-9.png)
> ![image-21.png](./image-21.png)

> - Category 페이지
> - 장르 / 나라 / 분류별 태그가 표시된다.
> - 각 태그 클릭 시, 해당 태그의 전체 영화 목록 페이지로 이동한다.  




> ![image-11.png](./image-11.png)

> - Recommended 페이지
> - 오늘의 추천영화(추천 알고리즘) : 사용자와 같은 연령대 및 성별의 다른 사용자들이 찜한 영화의 목록을 좋아요순으로 각각 정렬하여 서로 중복되는 영화를 우선적으로 추천한다.
> - 좋아요순 영화 추천 : 좋아요가 가장 많은 영화를 우선적으로 추천
> - 댓글순 영화 추천 : 댓글이 가장 많은 영화를 우선적으로 추천  




> ![image-12.png](./image-12.png)

> - Cinema 페이지
> - 키워드 입력시, 주변 영화관을 지도로 보여준다.  




> ![image-13.png](./image-13.png)
> ![image-15.png](./image-15.png)
> ![image-18.png](./image-18.png)

> - MyWorldcup 페이지
> - 영화 이상형 월드컵 구현
> - 우승 영화와 관련된 장르, 감독, 배우가 출연한 영화들을 추천해준다.  
  
  

## 3. 데이터 베이스 모델링 (ERD)
> ![image-19.png](./image-19.png)
  
  ## 4. URL 명세서

  > ![image-20.png](./image-20.png)

## 5. Vue 구성
    
      
## 6. 영화 추천 알고리즘

    ```
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
    ```

      
        
>- 기본적인 데이터들은 api요청을 통해 json 파일을 만든 다음 DB에 저장을 한다.
>- 각 연령대별 좋아요순으로 정렬한 리스트를 만들고
>- 각 성별 좋아요순으로 정렬한 리스트를 만든다.
>- 2개의 리스트에서 사용자의 연령대와 성별에 맞는 영화를 골라서
>- 해당 연령대와 성별의 좋아요 top 30중에서 중복되는것을 최우선 순위로 추천하고
>- 나머지 영화는 연령대와 성별 각각의 top 10에서 가져와 최대 10개 영화를 추천하는 리스트를 완성한다.
>- 그래도 10개 미만이거나 좋아요가 없다면 기본적으로는 랜덤으로 영화를 추가한다.
>- 최종 리스트를 serializer를 통해 Response한다.


## 7. 느낀점 / 후기

>- 이해건 : 처음으로 백앤드와 프론트앤드를 완벽하게 나누어서 작업을 한 프로젝트였습니다. 저는 백앤드 작업을 맡았고, 덕분에 백앤드에 관한 이해도가 많이 높아졌습니다. 처음에 제대로된 DB모델 설계 없이 구현부터 시작을 했다가 프로젝트를 진행하면서 DB모델을 계속 수정하는 일이 발생해서 여러 시행착오를 겪었습니다. 다음 프로젝트에서 백앤드를 다시 맡게 된다면 시작이 느리더라도 설계부터 정확하게 해서 체계적으로 진행하고 싶습니다.

>- 현지혜 : 관통프로젝트를 수행하면서 조금씩 영화 정보 사이트를 구현해본것이 많이 도움이 되었습니다. 구현하고 싶은 기능이 많았으나, 시간과 데이터 부족으로 생각보다 진행속도가 더뎌서 힘들었습니다. 다음부터는 모델구성 및 웹사이트 이미지 구성부터 체계적으로 구상 후 모델과 데이터를 구성, 이후 css작업 및 UI/UX 작업을 하면 더 좋을 것 같습니다. 또한 여러 이벤트 핸들러들을 더 집어넣어 유저들의 접근을 용이하게 하는 사이트를 제작해보고 싶습니다.


