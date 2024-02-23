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
    </div>

    <div class="main_box ">
      <div >
        <div class="content_style">
          <div>
            <h1 class="movie_title">{{ movieStore.movieDetail.id }}위. {{ movieStore.movieDetail.title  }}</h1>
            <div style="display: flex;">
              <div class="btn_style">{{ movieStore.movieDetail.runtime }}분</div>
              <div class="btn_style">{{ movieStore.movieDetail.prodYear }}</div>
              <div v-if="movieStore.movieDetail.nation.length > 0" class="btn_style">{{ movieStore.movieDetail.nation[0] }}</div>

              <div v-if="movieStore.movieDetail.rating ==='전체관람가'" class="all_age_type">{{ movieStore.movieDetail.rating }}</div>
              <div v-if="movieStore.movieDetail.rating ==='18세관람가(청소년관람불가)'" class="eightteen_age_type">{{ movieStore.movieDetail.rating }}</div>
              <div v-if="movieStore.movieDetail.rating ==='15세관람가'" class="fifteen_age_type">{{ movieStore.movieDetail.rating }}</div>
              <div v-if="movieStore.movieDetail.rating ==='12세관람가'" class="twelve_age_type">{{ movieStore.movieDetail.rating }}</div>

              <a class="teaser" style=" cursor: pointer;" id="open-calc-modal" @click="isTeaserViewed=true">예고편 보러가기
              <img src="@/assets/icon/video4.png" alt="" style="height: 20px;  cursor: pointer;"></a>
              <div id="calc-modal">
                <div class="calc-modal-content">
                  <div style="display: flex; justify-content:space-between;" > 
                    <span style="margin:0px; margin-bottom: 10px; color:white; font-size: 30px;">[ 예고편 ] {{ movieStore.movieDetail.title  }}</span>
                    <span id="close-calc-modal" style="font-size: 30px; color:white; cursor: pointer; ">x</span>
                  </div>
                      <div style="text-align: center; ">
                              <iframe :src="`${movieStore.movieDetail.vods}`" style="border-radius: 5px; border: hidden;" width="900px" height="600px"></iframe>
                    </div>
                </div>
              </div>
            </div>
            <p class="content_text">크리에이터  &nbsp; {{ movieStore.movieDetail.directors[0] }}</p>
            <p class="content_text">개봉일  &nbsp; {{ movieStore.movieDetail.repRlsDate }}</p>
            <p class="content_text">{{ movieStore.movieDetail.plots }}</p>
            <div style="display: grid; grid-template-columns: 5fr 1fr;">
              <div style="width: 800px;">
                <p class="content_text">출연  &nbsp;  
                  <span v-for="actor in movieStore.movieDetail.actors">
                    {{ actor }}, 
                  </span></p>
                <p class="content_text"> 
                  <template v-for="genre in movieStore.movieDetail.genre">
                    <span v-if="genre !== 'no'"
                      class="genre_style animate__animated" :class="item_animate"
                        @mouseenter="mouse1"
                        @mouseleave="mouse2"
                        @click="goGenreDetail(genre)"
                        >
                        # {{ genre }}&nbsp;
                    </span>
                  </template>
                </p>
                </div>

              <!-- 좋아요 버튼 여기있음 -->
              <div style="width: 100px; text-align: center; margin-left: auto; margin-bottom: 30px; display: flex; align-items: end;">
                <div v-if="!is_liked">
                  <img src="@/assets/icon/heart.png" alt="" @click="likeEvent"  style="height: 50px; cursor: pointer;">
                  <p style="color: white; font-size: 20px; font-weight: bold; margin: 0px;">찜</p>
                </div>
                <div v-if="is_liked">
                  <img src="@/assets/icon/full_heart.png" alt="" @click="likeEvent"  style="height: 50px; cursor: pointer;">
                  <p style="color: white; font-size: 20px; font-weight: bold; margin: 0px;">찜 취소</p>
                </div>
                <!-- <button ><h2>{{ likes_count }}</h2> <h1> {{ is_liked }} </h1></button> -->
                <!-- ---------------------------- -->
              </div>

              </div>

          </div>
          <div>
            <img class="img_style" :src="movieStore.PosterDetail" alt="" >
          </div>
        </div>
      </div>
    </div>
    <div style="border-bottom: white 1px solid ; padding-left: 30px; padding-right: 30px;">
      <div style=" padding: 10px 30px 10px 30px;">
      <Carousel style="margin:0px" :autoplay="2000" :itemsToShow="5" :wrapAround="true" :transition="500">
          <Slide v-for="still in movieStill.stlls " :key="still">
            <div class="carousel__item img_size "> 
              <img :src="still" alt="" style="height: 150px;">
            </div>
          </Slide>
        <Pagination/>
      </Carousel>
    </div> 

    <div style="padding-left: 45px;">
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
          <input class="comment_btn" style=" cursor: pointer;" type="submit" value="댓글 입력">
        </form>
      </div>
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
import { Carousel, Pagination, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import MovieTeaserView from '@/views/MovieTeaserView.vue'

const userStore = useCounterStore()
const route = useRoute()
const movieStore = useMovieStore()
let movieStill = ref([])


const dataAll = ref({})
const commentList = ref([])
const content = ref('')

const item_animate = ref([])
const mouse1 = function(event){
    event.currentTarget.classList.add('animate__headShake')
}
const mouse2 = function(event){
    event.currentTarget.classList.remove('animate__headShake')
}


onMounted(() =>{
  const movieIndex = movieStore.movieIndex
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/${movieIndex+1}/image/`
  })
  .then ((res) =>{
    movieStill.value=res.data
    // console.log(movieStill)
  })  
  /* 모달창 */
  const calcModal = document.getElementById("calc-modal");
        const openCalcModalBtn = document.getElementById("open-calc-modal");
        const closeCalcModalBtn = document.getElementById("close-calc-modal");
        // 모달창 열기
        console.log(openCalcModalBtn)
        console.log(closeCalcModalBtn)

        openCalcModalBtn.addEventListener("click", () => {
        calcModal.style.display = "block";
        document.body.style.overflow = "hidden"; // 스크롤바 제거
        });
        // 모달창 닫기
        closeCalcModalBtn.addEventListener("click", () => {
        calcModal.style.display = "none";
        document.body.style.overflow = "auto"; // 스크롤바 보이기
        });


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


// 장르 태그 이동
const router = useRouter()
const goGenreDetail = function(genre){  
  movieStore.movieDetail = genre
  router.push({name:"category", params:{moviename:genre}})
}


</script>

<style scoped>
.container {
  background-color: #141517;
}

.main_box {
  border-top: 1px solid white;
  border-bottom: 1px solid white;
  margin: 50px 50px 10px 50px;
  padding: 30px;
}
.movie_title {
  font-size: 40px;
  color: #FFC300;
  margin-bottom: 20px;
  margin-left: 0px;
  padding-left: 5px;
}

.content_style {
  display: grid;
  grid-template-columns: 2fr 1fr; 
  padding-left: 50px;
}

.content_text {
  color: white;
  font-size: 20px;
  line-height: 1.7;

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


.img_style {
  min-height: 550px;
  margin-left: 70px;
}

.btn_style {
  border: 2px solid white;
  font-size: 25px;
  color: white;
  border-radius: 5px;
  padding: 10px ;
  margin: 10px 15px 10px 0px;

}

.all_age_type {
  border: 2px solid #FFC300;
  background-color: #FFC300;
  font-size: 25px;
  font-weight: bold;
  border-radius: 5px;
  color: black;
  padding: 10px;
  margin: 10px 10px 10px 0px;

}

.eightteen_age_type {
  border: 2px solid red;
  background-color: red;
  font-size: 25px;
  font-weight: bold;
  border-radius: 5px;
  color: white;
  padding: 10px;
  margin: 10px 10px 10px 0px;

}

.fifteen_age_type {
  border: 2px solid blue;
  background-color: blue;
  font-size: 25px;
  font-weight: bold;
  border-radius: 5px;
  color: white;
  padding: 10px;
  margin: 10px 10px 10px 0px;

}

.twelve_age_type {
  border: 2px solid green;
  background-color: green;
  font-size: 25px;
  font-weight: bold;
  border-radius: 5px;
  color: white;
  padding: 10px;
  margin: 10px 10px 10px 0px;

}

.teaser {
  font-size: 25px;
  font-weight: bold;
  color: black;
  background-color: white;
  align-items: center;
  text-align: center;
  border: hidden;
  border-radius: 5px;
  padding: 10px;
  margin: 10px;
}
/*--------------------모달----------------------- */
#calc-modal {
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
  display: none;
  }
.calc-modal-content {
  display: grid;
  align-items: center;
  background-color: #161414;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 1000px;
  height: 700px;
  border-radius: 15px;
  }
.close-calc-modal {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
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
  margin-top: 0px;
  color: white;
  font-weight: bold;
  font-size: 20px;
}
.comment_user {
  color: white;
  text-decoration: none;
  /* font-weight: bold; */
}


/*----------------------네비게이션 바---------------------- */
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
  color : wheat;
  font-size: 30px;
  text-decoration: none;
  align-items: center;
}

.nav_font {
  font-family: 'Jost', sans-serif;
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
