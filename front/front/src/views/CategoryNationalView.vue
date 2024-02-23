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
    <h1 class="title">{{ nation }}</h1>
    <div style="margin: 50px;">
        <VueFlexWaterfall
          align-content="center"
          col="6"
          col-spacing="16"
          :break-at="{ 900: 3, 600: 2, 300: 1 }"
        >
        <template v-for="(mv,index) in nationalMovieList"  >
          <img class="poster_style animate__animated" v-if="newMovies[index]" :src=newMovies[index] alt=""  :class="item_animate"
          @mouseenter="mouse1"
          @mouseleave="mouse2"
          @click="gomovieDetail(mv.id, nationalMovieList, newMovies[mv.id])"
          >
          <!-- <p>{{ genreDetail }}gomovieDetail</p> -->
        </template>
      <!-- items -->
    </VueFlexWaterfall>
        <!-- {{ genreDetail }} -->
      <br>
      <br>
      </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { useMovieStore } from '@/stores/movies';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { routeLocationKey, useRouter, useRoute } from 'vue-router';
import {VueFlexWaterfall} from 'vue-flex-waterfall';


const userStore = useCounterStore()
const movieStore = useMovieStore()
const nationalMovieList = ref({})
const nation = ref('')
const route = useRoute()
const newMovies = ref([])

onMounted(()=>{
  if (route.params.idx == 1){
    nationalMovieList.value = movieStore.genreKorea.value
    nation.value = '한국영화'
    let arr = []
    let temp = ''
    for(let i = 0; i<nationalMovieList.value.length; i++){
      temp = nationalMovieList.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr
  }
  if (route.params.idx == 2){
    nationalMovieList.value = movieStore.genreJapan.value
    nation.value = '일본영화'
    let arr = []
    let temp = ''
    for(let i = 0; i<nationalMovieList.value.length; i++){
      temp = nationalMovieList.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr

  }
  if (route.params.idx == 3){
    nationalMovieList.value = movieStore.genreChina.value
    nation.value = '중국영화'
    let arr = []
    let temp = ''
    for(let i = 0; i<nationalMovieList.value.length; i++){
      temp = nationalMovieList.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr

  }
  if (route.params.idx == 4){
    nationalMovieList.value = movieStore.genreForiegn.value
    nation.value = '서부영화'
    let arr = []
    let temp = ''
    for(let i = 0; i<nationalMovieList.value.length; i++){
      temp = nationalMovieList.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr

  }
  if (route.params.idx == 5){
    nationalMovieList.value = movieStore.genreNor.value
    nation.value = '일반영화'
    console.log(nationalMovieList.value)
    let arr = []
    let temp = ''
    for(let i = 0; i<nationalMovieList.value.length; i++){
      temp = nationalMovieList.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr

  }
  if (route.params.idx == 6){
    nationalMovieList.value = movieStore.genreAni.value
    nation.value = '애니메이션'
    let arr = []
    let temp = ''
    for(let i = 0; i<nationalMovieList.value.length; i++){
      temp = nationalMovieList.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr

  }
  if (route.params.idx == 7){
    nationalMovieList.value = movieStore.genreDocu.value
    nation.value = '다큐멘터리'
    let arr = []
    let temp = ''
    for(let i = 0; i<nationalMovieList.value.length; i++){
      temp = nationalMovieList.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr

  }
  if (route.params.idx == 8){
    nationalMovieList.value = movieStore.genreLive.value
    nation.value = '공연물'
    let arr = []
    let temp = ''
    for(let i = 0; i<nationalMovieList.value.length; i++){
      temp = nationalMovieList.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr

  }
})


const router = useRouter()

const gomovieDetail = function(index, item, poster){
  movieStore.movieDetail = item
  movieStore.PosterDetail  = poster
  movieStore.idx = index
  router.push({name:"national", params:{id:index}})
}




// 포스터 애니메이션 //
const item_animate = ref([])
const mouse1 = function(event){
    event.currentTarget.classList.add('animate__jello')
}
const mouse2 = function(event){
    event.currentTarget.classList.remove('animate__jello')
}
// -----------------------------------------------------------------//


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
  color: #CC8B65;
  padding: 30px;
  margin: 0px;
}

.poster_style {
  min-height: 300px;
  margin: 30px;
  cursor: pointer;
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
</style>