<template>
  <div>
    <p class="title title_font korean_font">
      <img class="icon_style " src="@/assets/icon/movie_icon2.png" alt="">
      좋아요순 영화추천 </p>
      <p style="color: white;">
      </p>

      <div>
        <div style=" padding: 10px 30px 30px 30px;">
        <Carousel style="margin:0px"  :autoplay="2000"  :itemsToShow="5" :wrapAround="true" :transition="500">
          <Slide v-for="(rmv, index) in  recommendMovie.result" :key="index">
            <div class="carousel__item "> 
/              <p style="color: wheat;">
              </p>
              <img :src =rmv.poster alt="" class="poster_style animate__animated" :class="item_animate"
              @mouseenter="mouse1"
              @mouseleave="mouse2"
              @click="goMovieDetail(rmv.id, recommendMovie, newMovies[rmv.id])"
              >

            
          </div>
        </Slide>
        <Pagination/>
      </Carousel>
    </div>

  </div>
  </div>
</template>

<script setup>
import { Carousel, Pagination, Slide } from "vue3-carousel";
import { ref, onMounted, computed } from 'vue'
import "vue3-carousel/dist/carousel.css";
import axios from 'axios'
import { useMovieStore } from '@/stores/movies'
import { routerKey, useRouter } from "vue-router";
import { useCounterStore } from '@/stores/counter'
const movieStore = useMovieStore()
const userStore = useCounterStore()

const recommendMovie = ref([])
const newMovies = ref([])

onMounted(() =>{
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
  axios({
    method:'get',
    url: `${movieStore.API_URL}/api/v1/movies/algo/like/`,
    headers :{
          Authorization : `Token ${userStore.token}`
  }})
  .then((res) =>{
    // console.log(res)
    recommendMovie.value = res.data
    console.log(recommendMovie)
    console.log(recommendMovie.value.result)

    // let arr = []
    // let temp = ''
    // for(let i = 0; i<recommendMovie.value.length; i++){
    //   temp = recommendMovie.value[i].posters.split("'")[1]
    //   arr.push(temp)
    // }
    // newMovies.value = arr
    // console.log(newMovies.value)
  })
  .catch((err) =>{
    console.log(err)
  })
})
const router = useRouter()
const goMovieDetail = function(index, item, poster){
  movieStore.movieDetail = item
  movieStore.PosterDetail  = poster
  movieStore.idx = index
  router.push({name:"national", params:{id:index}})
}

// 포스터 애니메이션 //
const item_animate = ref([])
const mouse1 = function(event){
    event.currentTarget.classList.add('animate__pulse')
}
const mouse2 = function(event){
    event.currentTarget.classList.remove('animate__pulse')
}
// -----------------------------------------------------------------//

</script>

<style scoped>
.title {
  color: antiquewhite;
  margin-top: 20px;
  font-size: 50px;
  text-shadow: 5px 5px 5px black; 
}

.title_font {
  /* font-family: 'Comfortaa', sans-serif; */
  font-family: 'Russo One', sans-serif;
  /* font-family: 'Vina Sans', sans-serif; */
}

.icon_style {
  height: 40px;
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
.korean_font {
  font-family: 'Black Han Sans', sans-serif;
  /* font-family: 'Comfortaa', sans-serif; */
  /* font-family: 'Exo 2', sans-serif; */
  /* font-family: 'Rubik Moonrocks', sans-serif; */
  /* font-family: 'Russo One', sans-serif; */
  /* font-family: 'Vina Sans', sans-serif; */
}
</style>