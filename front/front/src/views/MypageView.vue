<template>
  <div class="container">
    <div>
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
    <img src="@/assets/background9.jpg" alt="" class="back_img" style="width: 100%; opacity: 70%;">
    <div class="content_style">
      <div class="main_content">
        <h1 class="title">My Page</h1>
        <div style="display: grid; grid-template-columns: 3fr 1fr; padding: 50px;">
          <div>
            <p class="subtitle_text korean_font" style="display: flex; align-items: center;" >내가 찜한 영화
              <img src="@/assets/icon/like_list.png" alt="" style="height: 40px; margin-left: 10px;" class="animate__animated animate__infinite animate__heartBeat">
            </p>
            <template v-if="userStore.userInfo.value?.like_movies">
              <div v-for="(movie,index) in userStore.userInfo.value?.like_movies " style="display: inline-block; width: 240px; margin: 20px">
                <!-- {{ movie }} -->
                <div style="margin: 10px;" >
                  <!-- <p style="color: white; font-size: 15px;" >{{ movie.title }}</p> -->
                  <img :src=movie.poster alt="" class="poster_style animate__animated"  style="height: 200px; border-radius: 5px; cursor: pointer;"  :class="item_animate"
                  @mouseenter="mouse1"
                  @mouseleave="mouse2"
                  @click="goMovieDetail(movie.id)"
                  >
                </div>
              </div>
            </template>
          </div>
          
          <div class="user_info">
            <!-- <img v-if="userStore.userInfo.user_sex === '남성'" src="@/assets/user2.png" alt="" class="user_img"> -->
            <img  src="@/assets/user2.png" alt="" class="user_img">


            <div>
              <p class="user_text">User &nbsp;|  {{ userStore.userInfo.user_name }}</p>
              <p class="user_text">E-mail &nbsp;|  {{ userStore.userInfo.user_email }}</p>
              <p class="user_text">성별 &nbsp;|  {{ userStore.userInfo.user_sex }}</p>
              <p class="user_text">나이 &nbsp;|  {{ userStore.userInfo.user_age }}</p>
              <p class="user_text">가입날짜 &nbsp;|  {{ userStore.userInfo.user_date_joined }}</p>
            </div>
              

          </div>
        </div>

      </div>
    </div>
  </div>

</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { useMovieStore } from '@/stores/movies'
import axios from 'axios';
import { ref, onMounted } from 'vue'
import { useRoute,useRouter } from 'vue-router'


const userStore = useCounterStore()
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
  font-size: 45px;
  font-family: 'Russo One', sans-serif;
  border-bottom: white 3px solid;
  width: 94%;
  margin-left: 30px;
}

.content_style {
  position: absolute;
  margin: 50px;
  margin-left: 100px;
  margin-right: 100px;

  top: 100px;
}

.back_img {
  filter: blur(5px);
  margin-left: auto;
  margin-right: auto;
}

.main_content {
  background-color: rgba(0, 0, 0, 60%);
  width: 1700px;
  margin-top: 40px;
  border-radius: 20px;
}

.user_info {
  text-align: center;
  border: 1px solid white;
  border-radius: 20px;
  margin: 30px 0px 10px 30px;
  box-shadow: 5px 5px 5px black;
  background-color: rgba(200, 200, 200, 50%);
}

.user_text {
  color: white;
  font-size: 15px;
  text-shadow: 2px 2px 2px black;

}
.user_img {
  margin: 20px ;
  height: 300px;
}

.user_content {
  background-color: rgba(200, 200, 200, 95%);
  border-radius: 20px;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 30px;
  text-align: start;
  padding-left: 20px;

  
}

.subtitle_text {
  color: white;
  font-size: 30px;
  margin-top: 30px;
  margin-bottom: 10px;
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