<template>
  <div class="container">
    <nav class="nav_box">
      <div class="nav_style1" style="display: grid; grid-template-columns: 1fr 5fr;">
        <div class="nav_style2">
          <RouterLink class="nav_text nav_font" :to="{name:'main'}">
            <img src="@/assets/icon/title_icon2.png" alt="" style="height: 70px;">
            <img src="@/assets/icon/color_icon5.gif" alt="" 
            style="position: absolute; height: 46px; top: 38px; left: 90px;"
            >
          </RouterLink>
          <RouterLink class="nav_text nav_font" :to="{name:'movies'}">Category</RouterLink>
          <RouterLink class="nav_text nav_font" :to="{name:'recommend'}">Recommend</RouterLink>
          <RouterLink class="nav_text nav_font" :to="{name:'cinema'}">Cinema</RouterLink>
          <RouterLink class="nav_text nav_font" :to="{name:'worldcup'}">MyWorldcup</RouterLink>
        </div>
        <div class="nav_style2" style="margin-left: auto;">
          <!-- 검색바 -->
        <span style="display: flex; margin-top: 15px;">
          <input class="search_input" type="text" v-model="word">
          <img class="search_btn" type="button" src="@/assets/icon/search.png" alt="" 
                @mousemove="onMousemove"
                @click="searchMovie()"
            :style="{ backgroundColor: `hsl(${x}, 60%, 40%)` }"
          >
        </span>
          <RouterLink v-if="!userStore.token"  class="nav_text nav_font" :to="{name:'SignUpView'}">SignUp</RouterLink>
          <RouterLink v-if="!userStore.token" class="nav_text nav_font" :to="{name:'LogInView'}">Login</RouterLink>
          <RouterLink v-if="userStore.token" class="nav_text nav_font" :to="{name:'mypage'}">Mypage</RouterLink>
          <RouterLink v-if="userStore.token"  class="nav_text nav_font" :to="{name:'LogOutView'}">Logout</RouterLink>
        </div>
      </div>
    </nav>

    <div style="display: grid; grid-template-columns: 1fr 2fr;">
          <!-- 왼쪽: 우승 영화 -->
          <div class="win_movie_style">
            <div>

              <img class="win_poster" :src="winPoster" alt="" style="height: 500px;"
              :class="item_animate"
              @mouseenter="mouse1"
              @mouseleave="mouse2"
              >
              <p style="color: antiquewhite; text-shadow: 1px 1px gray;font-size: 30px; display: flex; align-items: center; justify-content: center;" >
            <img src="@/assets/icon/medal.png" alt="" style="height: 40px;">
            {{ winMovie.title }}</p>
            <div style="text-align: start; padding: 30px;">
              <div style="display: flex;">
                <p class="btn_style">{{ winMovie.prodYear }}년</p>
                <p class="btn_style">{{ winMovie.runtime }}분</p>
                <div v-if="winMovie.rating ==='전체관람가'" class="all_age_type">{{ winMovie.rating }}</div>
                <div v-if="winMovie.rating ==='18세관람가(청소년관람불가)'" class="eightteen_age_type">{{ winMovie.rating }}</div>
                <div v-if="winMovie.rating ==='15세관람가'" class="fifteen_age_type">{{ winMovie.rating }}</div>
                <div v-if="winMovie.rating ==='12세관람가'" class="twelve_age_type">{{ winMovie.rating }}</div>
              </div>
              <p class="content_text">크리에이터  &nbsp; {{ moviedirector }}</p>
              <p class="content_text">개봉일  &nbsp; {{ winMovie.repRlsDate }}</p>
              <p class="content_text">배급사 &nbsp; {{ winMovie.company }}</p>
              <p class="content_text">출연  &nbsp;  
                  <span v-for="actor in winMovie.actors">
                    {{ actor }}, 
                  </span></p> 
              <p class="content_text">{{ winMovie.plots }}</p>
                <p class="content_text"> 
                  <template v-for="genre in winMovie.genre">
                    <span v-if="genre !== 'no'"
                      class="genre_style animate__animated" :class="item_animate"
                        @mouseenter="mouse1"
                        @mouseleave="mouse2"
                        @click="goGenreDetail(genre)"
                        >
                      #{{ genre }}&nbsp;
                    </span>
                  </template>
                </p>  
                




            </div>
          </div>
          </div>
          <div>
                <!-- 장르별 추천 -->
                <div style=" padding: 10px 30px 30px 30px;">
                    <p class="sub_title" style="display: flex; align-items: center;">
                      <img src="@/assets/icon/recommend2.png" style="height: 40px;" alt="">
                      &nbsp;해당 장르별 추천</p>
                  <Carousel style="margin:0px"  :autoplay="2000"  :itemsToShow="3" :wrapAround="true" :transition="500">
                    <Slide v-for="(movie, index) in  movieList_genre" :key="index">
                      <div class="carousel__item "> 
                        <p style="color: wheat;">
                        </p>
                        <img :src =newMovies_genre[index] alt="" class="poster_style animate__animated" :class="item_animate"
                        @mouseenter="mouse1"
                        @mouseleave="mouse2"
                        @click="goMovieDetail(movie.id)"
                        >
                      </div>
                    </Slide>
                  <Pagination/>
                  </Carousel>
                </div>

                <!-- 배우별 추천 -->
                <div style=" padding: 10px 30px 30px 30px;">
                  <p class="sub_title" style="display: flex; align-items: center;">
                      <img src="@/assets/icon/recommend2.png" style="height: 40px;" alt="">
                      &nbsp;해당 배우별 추천</p>
                  <Carousel style="margin:0px"  :autoplay="2000"  :itemsToShow="3" :wrapAround="true" :transition="500">
                    <Slide v-for="(movie, index) in  movieList_actor" :key="index">
                      <div class="carousel__item "> 
                        <p style="color: wheat;">
                        </p>
                        <img :src =newMovies_actor[index] alt="" class="poster_style animate__animated" :class="item_animate"
                        @mouseenter="mouse1"
                        @mouseleave="mouse2"
                        @click="goMovieDetail(movie.id)"
                        >
                      </div>
                    </Slide>
                  <Pagination/>
                  </Carousel>
                </div>
                <!-- 감독별 추천 -->
                <div style=" padding: 10px 30px 30px 30px;">
                  <p class="sub_title" style="display: flex; align-items: center;">
                      <img src="@/assets/icon/recommend2.png" style="height: 40px;" alt="">
                      &nbsp;해당 감독별 추천</p>
                <Carousel style="margin:0px"  :autoplay="2000"  :itemsToShow="3" :wrapAround="true" :transition="500">
                  <Slide v-for="(movie, index) in  movieList_director" :key="index">
                    <div class="carousel__item "> 
                      <p style="color: wheat;">
                      </p>
                      <img :src =newMovies_director[index] alt="" class="poster_style animate__animated" :class="item_animate"
                      @mouseenter="mouse1"
                      @mouseleave="mouse2"
                      @click="goMovieDetail(movie.id)"
                      >
                    </div>
                  </Slide>
                  <Pagination/>
                </Carousel>
              </div>
          </div>
    </div>
    <!-- 상단 이동하기 버튼 -->
    <img src="@/assets/icon/pageup.png" class="btn_gotop" type="button" style="height: 50px; " @click="moveUp" alt="">
    

  </div>
</template>

<script setup>
import axios, { Axios } from 'axios'
import { ref, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { useMovieStore } from '@/stores/movies'
import { Carousel, Pagination, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";


const userStore = useCounterStore()
const route = useRoute()
const movieStore = useMovieStore()

const winMovie = ref({})
const winPoster = ref('')
const moviedirector = ref('')

const movieList_director = ref({})
const movieList_actor = ref({})
const movieList_genre = ref({})

const newMovies = ref([])

const newMovies_director = ref([])
const newMovies_actor = ref([])
const newMovies_genre = ref([])

// 장르 태그 이동
const router = useRouter()
const goGenreDetail = function(genre){  
  movieStore.movieDetail = genre
  router.push({name:"category", params:{moviename:genre}})
}

onMounted(()=>{
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/${route.params.idx}/`
  })
  .then((res)=>{
    winMovie.value = res.data
    console.log(winMovie)
    let arr = []
    let temp = ''
    temp = winMovie.value.posters.split("'")[1]
    arr.push(temp)

    newMovies.value = arr
    console.log(newMovies.value)
    winPoster.value = newMovies.value[0]
    moviedirector.value = winMovie.value.directors[0]
  })
  .catch((err)=>{
    console.log(err)
  })
  // 장르별 영화 추천 받아오기
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/worldcup/${route.params.idx}/genre/`
  })
  .then((res)=>{
    movieList_genre.value = res.data
    let arr1 = []
    let temp1 = ''
    for(let i = 0; i<movieList_genre.value.length; i++){
      temp1 = movieList_genre.value[i].posters.split("'")[1]
      arr1.push(temp1)
    }
    newMovies_genre.value = arr1

  })
  .catch((err)=>{
    console.log(err)
  })
  // 감독별 영화 추천 받아오기
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/worldcup/${route.params.idx}/director/`
  })
  .then((res)=>{
    movieList_director.value = res.data
    let arr2 = []
    let temp2 = ''
    for(let i = 0; i<movieList_director.value.length; i++){
      temp2 = movieList_director.value[i].posters.split("'")[1]
      arr2.push(temp2)
    }
    newMovies_director.value = arr2
  })
  .catch((err)=>{
    console.log(err)
  })
  // 배우별 영화 추천 받아오기
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/worldcup/${route.params.idx}/actor/`
  })
  .then((res)=>{
    movieList_actor.value = res.data
    let arr3 = []
    let temp3 = ''
    for(let i = 0; i<movieList_actor.value.length; i++){
      temp3 = movieList_actor.value[i].posters.split("'")[1]
      arr3.push(temp3)
    }
    newMovies_actor.value = arr3
  })
  .catch((err)=>{
    console.log(err)
  })
})

// 포스터 애니메이션 //
const item_animate = ref([])
const mouse1 = function(event){
    event.currentTarget.classList.add('animate__pulse')
}
const mouse2 = function(event){
    event.currentTarget.classList.remove('animate__pulse')
}
// -----------------------------------------------------------------//

const goMovieDetail = function(index){

  router.push({name:"national", params:{id:index}})
}

const moveUp = function(){
	window.scrollTo({left:0, top:100})
}

</script>

<style scoped>
.container {
  margin: 0px;
  min-height: 100vh;
  background-color: #141517;
}

.title {
  color: white;
  padding: 50px;
  margin: 0px;
}

.sub_title {
  color: white;
  padding: 20px;
  margin: 0px;
  margin-left: 40px;
  font-size: 30px;
  font-family: 'Russo One', sans-serif;
}



.text_style {
  color: white;
  text-align: start;
  font-size: 25px;
  font-family: 'Russo One', sans-serif;
  text-shadow: 3px 3px 2px #0B220E;


}

.form_style {
  border: solid 1px wheat;
  border-radius: 5px;
  border: hidden;
  width: 90%;
  height: 300px;
  padding: 50px;
  margin-left: auto;
  margin-right: auto;
}

.form_title {
  color: antiquewhite;
  font-size: 80px;
  font-weight: bold;
  text-shadow: 3px 3px 2px #0B220E;
  font-family: 'Jost', sans-serif;
}

.nav_font {
  font-family: 'Jost', sans-serif;
}

.poster_style {
  background-color: black;
  border-radius: 10px;
  width: 250px;
  height: 360px;
  margin: 10px;
  box-shadow: 10px 10px 10px black;
  cursor: pointer;

}

.win_poster {
  box-shadow: 5px 5px #A52020;
  border-radius: 5px;
  
}
.win_movie_style {
  border: hidden;
  border-radius: 20px;
  background-color: black;
  margin-top: 100px;
  margin-bottom: 50px;
  margin-left: 50px;
  text-align: center;
  padding-top: 30px;
}

.content_text {
  color: white;
  font-size: 20px;
  line-height: 1.7;

}
.btn_style {
  border: 2px solid white;
  font-size: 15px;
  color: white;
  border-radius: 5px;
  padding: 7px;
  margin: 5px;

}
.genre_style {
  display: inline-block;
  color: white;
  border: #888 3px solid;
  background-color: rgba(97, 97, 97, 0.4);
  border-radius: 20px;
  padding: 5px;
  padding-left: 12px;
  padding-right: 12px;
  margin: 10px;
  width: auto;
  text-decoration: none;
  cursor: pointer;
}

.all_age_type {
  border: 2px solid #FFC300;
  background-color: #FFC300;
  font-size: 15px;
  font-weight: bold;
  border-radius: 5px;
  color: black;
  padding: 7px;
  margin: 5px;

}

.eightteen_age_type {
  border: 2px solid red;
  background-color: red;
  font-size: 15px;
  font-weight: bold;
  border-radius: 5px;
  color: white;
  padding: 7px;
  margin: 5px;

}

.fifteen_age_type {
  border: 2px solid blue;
  background-color: blue;
  font-size: 15px;
  font-weight: bold;
  border-radius: 5px;
  color: white;
  padding: 7px;
  margin: 5px;

}

.twelve_age_type {
  border: 2px solid green;
  background-color: green;
  font-size: 15px;
  font-weight: bold;
  border-radius: 5px;
  color: white;
  padding: 7px;
  margin: 5px;

}
/*--------------------------검색바----------------------- */
.search_style {
  border: 1px solid white;
  border-radius: 10px;
  height: 30px;
}

.search_btn {
  height: 25px; 
  width: 25px;
  font-weight: bold;
  color: white;
  border-radius: 0px 10px 10px 0px;
  cursor: pointer;
  padding: 5px 15px 6px 15px;
  margin-top: 5px;
  background-color: #A52020;  
}

.search_input {
  height: 33px; 
  width: 250px;
  border-radius: 10px 0px 0px 10px;
  border: hidden;
  margin-top: 5.8px;
  padding-left: 10px;  
  font-size: 20px;

}
.btn_gotop { 
display: block; 
position: fixed; 
bottom: 35px; /* 탑버튼을 화면의 가장 아래에서 몇 픽셀 떨어뜨릴 것인지 정하세요*/ 
right: 30px; /* 탑버튼을 화면의 가장 오른쪽에서 몇 픽셀 떨어뜨릴 것인지 정하세요*/ 
z-index: 999; 
outline: none; 
color: rgba(0,0,0,0.7); 
cursor: pointer; 
padding: 15px 20px; 
} 
</style>