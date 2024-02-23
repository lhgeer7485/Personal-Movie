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
    <!-- 상단 이동하기 버튼 -->
    <img src="@/assets/icon/pageup.png" class="btn_gotop" type="button" style="height: 50px; " @click="moveUp" alt="">
    
    
    <!-- 본문 -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; " >
      <div>
        <img src="@/assets/background7.jpg" alt=""  style="width: 90%; margin-left: 60px; margin-top: 40px; border-radius: 10px;">
      </div>
      <div>
        <span class="title animate__animated animate__fadeInRight" style="display: flex; align-items: start; width: 80%; margin-bottom: 50px; border-bottom: white 2px solid;">
          Category
          <img src="@/assets/icon/movie_icon5.png" alt="" style="height: 60px; display: flex; align-items: center; margin-left: 10px;">
        </span>
        <div class="content_style">

<!-- 
            <div class="animate__animated animate__fadeInRight time1">
              <span class="subtitle_text" style="display: flex; align-items: center; ">
                <img src="@/assets/icon/popcorn2.png" alt="" style="display: flex; align-self: start; height: 50px; margin-right: 15px;">
                오늘의 추천영화!</span>
            </div> -->
            <div class="animate__animated animate__fadeInRight time2">
              <span class="subtitle_text korean_font" style="display: flex; align-items: center; ">
                <img src="@/assets/icon/popcorn2.png" alt="" style="display: flex; align-self: start; height: 50px; margin-right: 15px;">
                장르별</span>
                <span  v-for="(genre, index) in movieGenre.list" :key="index">
                  <p class="genre_style animate__animated" :class="item_animate"
                  @mouseenter="mouse1"
                  @mouseleave="mouse2"
                  @click="goGenreDetail(genre)"
                  ># {{ genre }}</p>
                </span>
            </div>


            <div class="animate__animated animate__fadeInRight time3">
              <span class="subtitle_text korean_font" style="display: flex; align-items: center; ">
                <img src="@/assets/icon/popcorn2.png" alt="" style="display: flex; align-self: start; height: 50px; margin-right: 15px;">
                나라별</span>
                <span class="genre_style animate__animated"
                @mouseenter="mouse1"
                @mouseleave="mouse2"
                @click="goGenreKorea"
                ># 한국영화</span>
                <span class="genre_style animate__animated"
                @mouseenter="mouse1"
                @mouseleave="mouse2"
                @click="goGenreJapan"
                ># 일본영화</span>
                <span class="genre_style animate__animated"
                @mouseenter="mouse1"
                @mouseleave="mouse2"
                @click="goGenreChina"
                ># 중국영화</span>
                <span class="genre_style animate__animated"
                @mouseenter="mouse1"
                @mouseleave="mouse2"
                @click="goGenreForiegn"
                ># 서부영화</span>
            </div>


            <div class="animate__animated animate__fadeInRight time4">

              <span class="subtitle_text korean_font" style="display: flex; align-items: center; ">
                <img src="@/assets/icon/popcorn2.png" alt="" style="display: flex; align-self: start; height: 50px; margin-right: 15px;">
                분류</span>
                <span class="genre_style animate__animated"
                @mouseenter="mouse1"
                @mouseleave="mouse2"
                @click="goGenreNormal"
                ># 일반영화</span>
                <span class="genre_style animate__animated"
                @mouseenter="mouse1"
                  @mouseleave="mouse2"
                  @click="goGenreAnimation"
                  ># 애니메이션</span>
                  <span class="genre_style animate__animated"
                  @mouseenter="mouse1"
                  @mouseleave="mouse2"
                  @click="goGenreDocumentary"
                  ># 다큐멘터리</span>
                  <span class="genre_style animate__animated"
                  @mouseenter="mouse1"
                  @mouseleave="mouse2"
                  @click="goGenreLive"
                  ># 공연물</span>  
            </div>
        </div>
    </div>
  </div>
  
  
  
  
  
  
  
  
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { useMovieStore } from '@/stores/movies';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const movieGenre = ref([])


const userStore = useCounterStore()
const movieStore = useMovieStore()

const item_animate = ref([])
const mouse1 = function(event){
    event.currentTarget.classList.add('animate__headShake')
}
const mouse2 = function(event){
    event.currentTarget.classList.remove('animate__headShake')
}

onMounted(() =>{
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/genre/`
  })
  .then ((res) =>{
    movieGenre.value = res.data
  })  
  .catch((error) => {
    console.log(error)
  })
  // #한국영화 클릭시
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/category/kr/`
  })
  .then ((res) =>{
    movieStore.genreKorea.value = res.data
  })  
  .catch((error) => {
    console.log(error)
  })
  // #일본영화 클릭시
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/category/jp/`
  })
  .then ((res) =>{
    movieStore.genreJapan.value = res.data
  })  
  .catch((error) => {
    console.log(error)
  })
  // #중국영화 클릭시
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/category/cn/`
  })
  .then ((res) =>{
    movieStore.genreChina.value = res.data
  })  
  .catch((error) => {
    console.log(error)
  })
  // #서부영화 클릭시
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/category/fg/`
  })
  .then ((res) =>{
    movieStore.genreForiegn.value = res.data
  })  
  .catch((error) => {
    console.log(error)
  })

  // #일반영화 클릭시
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/category/nomal/`
  })
  .then ((res) =>{
    movieStore.genreNor.value = res.data
  })  
  .catch((error) => {
    console.log(error)
  })

  // #애니메이션 클릭시
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/category/ani/`
  })
  .then ((res) =>{
    movieStore.genreAni.value = res.data
  })  
  .catch((error) => {
    console.log(error)
  })

  // #다큐멘터리 클릭시
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/category/doc/`
  })
  .then ((res) =>{
    movieStore.genreDocu.value = res.data
  })  
  .catch((error) => {
    console.log(error)
  })

  // #공연물 클릭시
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/category/live/`
  })
  .then ((res) =>{
    movieStore.genreLive.value = res.data
  })  
  .catch((error) => {
    console.log(error)
  })

})

const router = useRouter()
const goGenreDetail = function(genre){  
  movieStore.movieDetail = genre
  router.push({name:"category", params:{moviename:genre}})
}

const goGenreKorea = function(){  
  router.push({name:"category_national", params:{idx:1}})
}

const goGenreJapan = function(){  
  router.push({name:"category_national",params:{idx:2}})
}

const goGenreChina = function(){  
  router.push({name:"category_national",params:{idx:3}})
}

const goGenreForiegn = function(){  
  router.push({name:"category_national",params:{idx:4}})
}

const goGenreNormal = function(){  
  router.push({name:"category_national",params:{idx:5}})
}

const goGenreAnimation = function(){  
  router.push({name:"category_national",params:{idx:6}})
}

const goGenreDocumentary = function(){  
  router.push({name:"category_national",params:{idx:7}})
}

const goGenreLive = function(){  
  router.push({name:"category_national",params:{idx:8}})
}

const moveUp = function(){
	window.scrollTo({left:0, top:100})
}

</script>

<style scoped>
.container {
  margin: 0px;
  width: 100%;
  min-height: 100vh;
  background-color: #141517;
  /* background-color: wheat; */

}
.title {
  color: white;
  padding: 20px;
  margin-top: 10px;
  margin-left: 10px;
  font-size: 45px;
  font-family: 'Russo One', sans-serif;
  text-shadow: gray 2px 2px;

}

.content_style {
  margin-left: 30px;
  width: 800px;
}
.subtitle_text {
  color: white;
  font-size: 25px;
  margin-top: 30px;
  margin-bottom: 10px;
}


.nav_font {
  font-family: 'Jost', sans-serif;
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
  font-size: 20px;
}

.time1 {
  animation-delay: 0.2s;
}

.time2 {
  animation-delay: 0.4s;
}

.time3 {
  animation-delay: 0.6s;
}

.time4 {
  animation-delay: 0.8s;
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

.korean_font {
  font-family: 'Black Han Sans', sans-serif;
}
</style>