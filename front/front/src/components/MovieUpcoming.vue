<template>
  <div>
    <p class="title title_font ">
      <img class="icon_style" src="@/assets/icon/movie_icon2.png" alt="">
      UpComing Movie</p>
      <div style=" padding: 10px 30px 30px 30px;">
      <Carousel style="margin:0px"  :autoplay="2000"  :itemsToShow="5" :wrapAround="true" :transition="500">
        <Slide v-for="(upMovie,index) in upcomingMovie" :key="index"  >
          <div class="carousel__item "> 
            <img class="poster_style animate__animated" :src=upMovie.posters alt="" :class="item_animate"
            @mouseenter="mouse1"
            @mouseleave="mouse2"
            @click="goUpcomingmovie(index, upcomingMovie[index])"> 
          </div> 
        </Slide>
        <Pagination/>
      </Carousel>
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

const store = useMovieStore()

const upcomingMovie = ref([])

onMounted(() =>{

  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/main/upcomming/`
  })
  .then((res) =>{
    // console.log(res)
    upcomingMovie.value = res.data
    // console.log(upcomingMovie)

  })
  .catch((err) =>{
    console.log(err)
  })
})

const router = useRouter()

const goUpcomingmovie = function(index, item){
  store.movieDetail = item
  store.idx = index
  router.push({name:"teaser", params:{id:index}})
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

.video_style {
  background-color: black;
  border-radius: 10px;
  width: 360px;
  height: 230px;
  margin: 10px;  
  box-shadow: 10px 10px 10px black;

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




</style>