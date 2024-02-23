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
    <!-- 본문 -->
    <div>
      <div>
        <RecommendRank/>
      </div>
      <div>
        <LikedRank/>
      </div>
      <div>
        <CommentRank/>
      </div>


  <!-- 상단 이동하기 버튼 -->
  <img src="@/assets/icon/pageup.png" class="btn_gotop" type="button" style="height: 50px;" @click="moveUp" alt="">

    </div>



    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import RecommendRank from '@/components/RecommendRank.vue';
import LikedRank from '@/components/LikedRank.vue';
import CommentRank from '@/components/CommentRank.vue';
import { useMovieStore } from '@/stores/movies'
import axios from 'axios';
import { ref, onMounted } from 'vue'
import { useRoute,useRouter } from 'vue-router'


const userStore = useCounterStore()


const moveUp = function(){
	window.scrollTo({left:0, top:100})
}

const movieStore = useMovieStore()
const poster = ref([])
const router = useRouter()

onMounted(() => {
  axios({
        method:'get',
        url: `${movieStore.API_URL}/accounts/info/`,
        headers :{
          Authorization : `Token ${userStore.token}`
        }
      })
      .then((res)=>{
        console.log(userStore.userInfo.value.like_movies)
        userStore.userInfo.value = res.data
      })
      .catch((err)=>{
        console.log(err)


      })

})





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