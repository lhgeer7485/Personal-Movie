<template>
  <div>
    <p class="title title_font">
      <img class="icon_style" src="@/assets/icon/movie_icon2.png" alt="">
      Foreign Movie</p>
      <p style="color: white;">
      </p>

      <div>
        <div style=" padding: 10px 30px 30px 30px;">
        <Carousel style="margin:0px"  :autoplay="2000"  :itemsToShow="5" :wrapAround="true" :transition="500">
          <Slide v-for="(fmv, index) in  foreignMovie" :key="index">
            <div class="carousel__item "> 
              <p style="color: wheat;">
              </p>
              <img :src =newMovies[index] alt="" class="poster_style animate__animated" :class="item_animate"
              @mouseenter="mouse1"
              @mouseleave="mouse2"
              @click="goForeignmovie(fmv.id, foreignMovie, newMovies[fmv.id])"
              :foreignMovie="foreignMovie"
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
import { ref, onMounted, computed } from 'vue'
import { Carousel, Pagination, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import axios from 'axios'
import { useMovieStore } from '@/stores/movies'
import { routerKey, useRouter } from "vue-router";
const store = useMovieStore()

const foreignMovie = ref([])
const newMovies = ref([])
onMounted(() =>{
  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/main/foreign/`
  })
  .then((res) =>{
    // console.log(res)
    foreignMovie.value = res.data
    // console.log(foreignMovie)
    let arr = []
    let temp = ''
    for(let i = 0; i<foreignMovie.value.length; i++){
      temp = foreignMovie.value[i].posters.split("'")[1]
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

const goForeignmovie = function(index, item, poster){
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