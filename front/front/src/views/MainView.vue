<template>
  <div class="container" style="background-color: #141517;">
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
    <div>
      <br>
      <div 
      @mousemove="onMousemove"
            :style="{ backgroundColor: `hsl(${x}, 60%, 40%)` }"
            class="movearea title_back">
        <h1 class="animate__animated animate__bounce">Hi</h1>
        <h1>
          What's Your <span style="color:black;"
          ><strong>Personal Movie?</strong></span>
          <span class="blinking-cursor"> |</span>
        </h1>
      </div>
      <br>
      <br>
    </div>
      <div>
        <MovieTodayBOX
        :movieList="movieList"
        />
      </div>
      <div>
        <MovieUpcoming/>
      </div>
      <div>

      </div>
      <div>
        <KoreaMovies/>
      </div>
      <div>
        <ForeignMovies/>
      </div>
      <div>
        <AnimationMovies/>
      </div>
      <!-- 상단 이동하기 버튼 -->
      <img src="@/assets/icon/pageup.png" class="btn_gotop" type="button" style="height: 50px;" @click="moveUp" alt="">
    </div>

  <RouterView/>
</template>

<script setup>
import axios from 'axios'
import { useMovieStore } from '@/stores/movies'
import { defineComponent, ref, onMounted } from "vue";
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router';

import MovieTodayBOX from '@/components/MovieTodayBOX.vue'
import MovieUpcoming from '@/components/MovieUpcoming.vue'
import KoreaMovies from '@/components/KoreaMovies.vue'
import ForeignMovies from '@/components/ForeignMovies.vue'
import AnimationMovies from '@/components/AnimationMovies.vue'

//--------------------------------------//
const screenAvailWidth = window.screen.availWidth;

// console.log(screenAvailWidth);

const userStore = useCounterStore()

//-----------------------------------------------//
const store = useMovieStore()
const movieList = ref([])

onMounted(() =>{
  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/`
  })
  .then ((res) =>{
    movieList.value = res.data
    // console.log(movieList)
  })
  .catch((err) =>{
    console.log(err)
  })
})
//----------------------------------------------//




const moveUp = function(){
	window.scrollTo({left:0, top:100})
}

const x = ref(0)

function onMousemove(e) {
  x.value = e.clientX
}

//검색바

const word = ref('')
const router = useRouter()

const searchMovie = function() {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/movies/searchMovie/${word.value}/`
  })
    .then((res) => {
      if (res.data.length > 0){
        // console.log(res.data[0].id)
        router.push({name:"national", params:{id:res.data[0].id}})
      }else{
        alert('검색 결과가 없습니다.')
      }
    })
  // router.push({name:"national", params:{id:index}})
}




</script>


<style>
h1 {
  padding-left: 30px;
  color: #FFF1DE;
  font-size: 4rem;
  font-weight: normal;
  margin: 0px;
  text-shadow: 3px 3px 3px #2c3e50; 
}

 /* Cursor blinking CSS Starts... */
.blinking-cursor {
  font-size: 4rem;
  color: #2c3e50;
  animation: 1s blink step-end infinite;
}
@keyframes blink {
  from,
  to {
    color: transparent;
  }
  50% {
    color: wheat;
  }
}

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

.title_back {
  background-color: #133129;
  padding-top: 20px;
  padding-bottom: 20px;
  width: 100%;
}

.movearea {
  transition: 0.3s background-color ease;
}


.title1 {
  color: antiquewhite;
  font-size: 45px;
}

.icon_boxoffice {
  height: 40px;
  padding-left: 30px;
}

.nav_box {
  padding: 20px ;
  display: flex;
  justify-content: space-between;
}

.nav_style1 {
  display: flex;
  text-align: start;
  gap: 20px;
}

.nav_style2 {
  display: flex;
  text-align: end;
  gap: 20px;
}

.nav_text {
  display: flex;
  color : wheat;
  font-size: 30px;
  text-decoration: none;
  align-items: center;
  cursor: pointer;
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

.koren_font {
  font-family: 'Black Han Sans', sans-serif;
  font-family: 'Comfortaa', sans-serif;
  font-family: 'Exo 2', sans-serif;
  font-family: 'Rubik Moonrocks', sans-serif;
  font-family: 'Russo One', sans-serif;
  font-family: 'Vina Sans', sans-serif;
}

/*--------------------------검색바----------------------- */
.search_style {
  display: flex;
  align-items: center;

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
}

.search_input {
  height: 33px; 
  width: 250px;
  border-radius: 10px 0px 0px 10px;
  border: hidden;
  margin-top: 5.9px;
  padding-left: 10px;  
  font-size: 20px;

}
</style>