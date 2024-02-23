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
    <p class="title korean_font" style="display: flex; align-items: start;">{{ movieGenre }}
    <img src="@/assets/icon/popcorn.png" alt="" style="height: 65px; margin-left: 20px;">
    </p>
    <div style="margin: 50px;">
      <VueFlexWaterfall
        align-content="center"
        col="6"
        col-spacing="16"
        :break-at="{ 900: 3, 600: 2, 300: 1 }"
      >
      <template v-for="(gmv,index) in genreDetail"  >
        <img class="poster_style animate__animated" v-if="newMovies[index]" :src=newMovies[index] alt=""  :class="item_animate"
        @mouseenter="mouse1"
        @mouseleave="mouse2"
        @click="gomovieDetail(gmv.id, genreDetail, newMovies[gmv.id])"
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
import { useRouter } from 'vue-router';
import {VueFlexWaterfall} from 'vue-flex-waterfall';


const userStore = useCounterStore()
const movieStore = useMovieStore()
const genreDetail = ref([])
const newMovies = ref([])
const movieGenre = movieStore.movieDetail

onMounted(() =>{
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/genre/${movieGenre}`
  })
  .then ((res) =>{
    genreDetail.value = res.data
    let arr = []
    let temp = ''
    for(let i = 0; i<genreDetail.value.length; i++){
      temp = genreDetail.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr
    console.log(newMovies.value)
  })  
  .catch((error) => {
    console.log(error)
  })
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
  background-color: #141517;
  /* background-color: wheat; */

}
.title {
  color: white;
  padding: 30px;
  margin: 0px;
  font-size: 60px;
  text-shadow: 3px 3px #F44343;
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

.korean_font {
  font-family: 'Black Han Sans', sans-serif;
  /* font-family: 'Comfortaa', sans-serif; */
  /* font-family: 'Exo 2', sans-serif; */
  /* font-family: 'Rubik Moonrocks', sans-serif; */
  /* font-family: 'Russo One', sans-serif; */
  /* font-family: 'Vina Sans', sans-serif; */
}
</style>