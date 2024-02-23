<template>
  <div>
    <p class="title title_font">
      <img class="icon_style" src="@/assets/icon/movie_icon2.png" alt="">
      Animation Movie</p>
      <p style="color: white;">
      </p>

      <div>
        <div style=" padding: 10px 30px 30px 30px;">
        <Carousel style="margin:0px"  :autoplay="2000"  :itemsToShow="5" :wrapAround="true" :transition="500">
          <Slide v-for="(amv, index) in  aniMovie" :key="index">
            <div class="carousel__item "> 
              <p style="color: wheat;">
              </p>
              <img :src =newMovies[index] alt="" class="poster_style animate__animated" :class="item_animate"
              @mouseenter="mouse1"
              @mouseleave="mouse2"
              @click="goAnimovie(amv.id, aniMovie, newMovies[amv.id])"
              :aniMovie="aniMovie"
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
const store = useMovieStore()

const aniMovie = ref([])
const newMovies = ref([])
onMounted(() =>{
  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/main/animation/`
  })
  .then((res) =>{
    // console.log(res)
    aniMovie.value = res.data
    // console.log(aniMovie)
    let arr = []
    let temp = ''
    for(let i = 0; i<aniMovie.value.length; i++){
      temp = aniMovie.value[i].posters.split("'")[1]
      arr.push(temp)
    }
    newMovies.value = arr
    // console.log(newMovies.value)
  })
  .catch((err) =>{
    console.log(err)
  })
})

const router = useRouter()

const goAnimovie = function(index, item, poster){
  store.movieDetail = item
  store.PosterDetail  = poster
  store.idx = index
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
  font-size: 50px;
  margin-top: 20px;
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

</style>