<template>
    <div class="container" >
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
        </div>
        <div class="main_box">
          <p class="movie_title">[ 예고편 ] {{ movieStore.movieDetail.title }}</p>
          <div style="display:grid; grid-template-columns: 1fr 1fr;">
              <div>
                <iframe :src="movieStore.movieDetail.vods" style=" border-radius: 5px; border: hidden; margin-bottom: 30px ;" width="900px" height="600px" ></iframe>
              </div>
              <div class="content_style">
              <div style="display: grid; grid-template-columns: 5fr 1fr;">
                <div>
                  <p class="content_text">개봉일 &nbsp; {{ movieStore.movieDetail.repRlsDate }}</p>
                  <p class="content_text">줄거리</p>
                </div>

                <!-- 좋아요 버튼 여기있음 -->
                <div style="width: 100px; text-align: center; z-index: 99; margin-left: auto; margin-bottom: 30px; display: flex; align-items: end;">
                  <div v-if="!is_liked" @click="likeEvent" style="cursor: pointer;">
                    <img src="@/assets/icon/heart.png" alt=""   style="height: 50px;">
                    <p style="color: white; font-size: 20px; font-weight: bold; margin: 0px;">찜</p>
                  </div>
                  <div v-if="is_liked" @click="likeEvent" style="cursor: pointer;">
                    <img src="@/assets/icon/full_heart.png" alt=""   style="height: 50px;">
                    <p style="color: white; font-size: 20px; font-weight: bold; margin: 0px;">찜 취소</p>
                  </div>
                  <!-- <button ><h2>{{ likes_count }}</h2> <h1> {{ is_liked }} </h1></button> -->
                  <!-- ---------------------------- -->
                </div>
              </div>

                <p class="content_text">{{ movieStore.movieDetail.plots }}</p>
                <p class="content_text"> 
                  <template v-for="genre in movieStore.movieDetail.genre">
                    <span  v-if="genre !== 'no'"
                    class="genre_style animate__animated" :class="item_animate" style="position: relative; z-index: 100;"
                        @mouseenter="mouse1"
                        @mouseleave="mouse2"
                        @click="goGenreDetail(genre)"
                        >
                      #{{ genre }}&nbsp;
                    </span>
                  </template>
                </p>
              <img class="img_style" :src="movieStore.movieDetail.posters" alt="">
            </div>
          </div>
        </div>
          <div style="padding-left: 45px; padding-bottom: 10px;">
          <div style="padding-top: 0px;">
            <p class="comment_count">댓글 수 : {{ commentList.length }}</p>
            <div v-for="cmt in commentList">
              <span class="comment_text" >
                <a class="comment_user" href="#">{{ cmt.user }}</a> &nbsp;  {{ cmt.content }} 
                <!-- <p>{{ cmt.id }} </p> -->
                &nbsp;<img src="@/assets/icon/delete_btn.png"  @click="deleteEvent(cmt.id)" alt="" style="height: 11px; opacity: 70%;">
              </span>
                <hr style="border: 1px solid gray; width: 97%; opacity: 30%; margin-left: 0px;">
            </div>
          </div>
          <div style="margin-bottom: 20px;">
            <form @submit.prevent="create">
              <input class="comment_input" type="text" v-model="content">
              <input class="comment_btn" style="cursor: pointer;" type="submit" value="댓글 입력">
            </form>
          </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useMovieStore } from '@/stores/movies'
import { useRoute, useRouter } from 'vue-router'

const userStore = useCounterStore()
const route = useRoute()
const movieStore = useMovieStore()

//----------------------------
const dataAll = ref({})
const commentList = ref([])
const content = ref('')
//----------------------------


const item_animate = ref([])
const mouse1 = function(event){
    event.currentTarget.classList.add('animate__headShake')
}
const mouse2 = function(event){
    event.currentTarget.classList.remove('animate__headShake')
}

const router = useRouter()
const goGenreDetail = function(genre){  
  movieStore.movieDetail = genre
  router.push({name:"category", params:{moviename:genre}})
}

onMounted(() =>{
    /* 댓글창 구현 */
    axios({
    method: 'GET',
    url: `${userStore.API_URL}/api/v1/movies/${movieStore.movieDetail.id}/`
  })
    .then((res) => {
      dataAll.value = res.data
      commentList.value = dataAll.value.comment_set
      console.log(dataAll)
    })
    .catch((error) => {
      console.log(error)
    })
        
})

const create = function () {
  axios({
    method: 'POST',
    url: `${userStore.API_URL}/api/v1/movies/comment/${movieStore.movieDetail.id}/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization : `Token ${userStore.token}`
    }
  })
    .then((res) => {
      console.log(res)
      axios({
      method: 'GET',
      url: `${userStore.API_URL}/api/v1/movies/${movieStore.movieDetail.id}/`
      })
      .then((res) => {
        dataAll.value = res.data
        commentList.value = dataAll.value.comment_set
  
        
      })
      .then((res) => {
        content.value = ''
        console.log(content)
      })
      .catch((error) => {
      console.log(error)
      })
    })
    .catch((error) => {
      console.log(error)
    })

  
} 

watch(commentList, (newValue, oldValue) => {console.log(dataAll.value.comment_set) 
  console.log(oldValue.length)})



const deleteEvent = function (comment_pk) {
  axios({
    method: "DELETE",
    url: `${userStore.API_URL}/api/v1/movies/comment/delete/${comment_pk}/`,
    headers: {
      Authorization : `Token ${userStore.token}`
    }
  })
  .then((res) => {
    axios({
      method: 'GET',
      url: `${userStore.API_URL}/api/v1/movies/${movieStore.movieDetail.id}/`
      })
      .then((res) => {
        dataAll.value = res.data
        commentList.value = dataAll.value.comment_set
    
      })
      .catch((error) => {
      console.log(error)
      })
    })
    
  .catch((error) => {
    console.log(error)
  })

  .catch((error) => console.log(error))

}


// 좋아요 코드
//-----------------------------

const is_liked = ref(false)
const likes_count = ref(0)
const likeEvent = function () {
  axios({
    method: 'POST',
    url: `${userStore.API_URL}/api/v1/movies/like/${movieStore.movieDetail.id}/`,
    headers: {
      Authorization : `Token ${userStore.token}`
    }
  })
    .then((res) => {
      is_liked.value = res.data.is_liked
      likes_count.value = res.data.likes_count
      console.log(is_liked.value)
      console.log(likes_count.value)
      })
    .catch((error) => console.log(error))
}
</script>

<style scoped>
.container {
  background-color: #141517;
}

.main_box {
  border-top: 1px solid white;
  border-bottom: 1px solid white;
  margin: 20px 50px 0px 50px;
  padding: 20px 20px 0px 20px;

}
.movie_title {
  font-size: 40px;
  font-weight: bold;
  color: #FFC300;
  margin-bottom: 50px;
  margin-left: 0px;
  padding-left: 20px;
}

.content_style {
  padding-left: 30px;
  padding-right: 30px;
}

.content_text {
  color: white;
  font-size: 20px;
  line-height: 1.8;
}

.img_style {
  position: absolute;
  z-index: 50;
  width: 800px;
  max-height: 100%;
  margin-left: 70px;
  filter: blur(3px);
  opacity: 20%;
  right: 80px;
  top:0px;

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
  z-index: 99;
}

.teaser {
  font-size: 25px;
  color: white;
  align-items: center;
  text-align: center;
  border: hidden;
  border-radius: 5px;
  padding: 10px;
  margin: 10px;
}

/*---------------------- 댓글 창 ---------------------- */
.comment_input {
  width: 89%;
  height: 35px;
  margin: 10px 10px 10px 0px;
  border-radius: 5px;
  font-size: 15px;
}

.comment_btn {
  background-color: #B60030;
  color: white;
  font-size: 15px;
  border-radius: 5px;
  width: 100px;
  height: 35px;
  margin: 5px;
  border: hidden;
  /* box-shadow: 1px 1px 1px gray; */
}
.comment_text {
  color: lightslategrey;
}
.comment_count {
  margin-top: 30px;
  color: white;
  font-weight: bold;
  font-size: 20px;
}
.comment_user {
  color: white;
  text-decoration: none;
  /* font-weight: bold; */
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
</style>