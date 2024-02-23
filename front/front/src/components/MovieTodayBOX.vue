<template>
  <div>
    <p class="title title_font ">
    <img class="icon_style " src="@/assets/icon/movie_icon2.png" alt="">
    Today BoxOffice</p>
    <div style=" padding: 10px 30px 30px 30px;">
      <Carousel style="margin:0px" :autoplay="2000" :itemsToShow="5" :wrapAround="true" :transition="500">
        <!-- <Slide v-for="slide in slides" :key="slide"> -->
          <Slide v-for="(topMovie,index) in movieBox " :key="index">
            <span 
            style="color:white; 
            font-size: 130px; 
            font-weight: bold; 
            text-shadow: 3px 3px 3px black; 
            position: absolute; 
            z-index: 10; 
            left:-10px; 
            top:-20px; 
            display: flex; 
            align-items: start;
            color:#E7E1DB;
            
            " >
              {{ index+1 }}
            </span>

          <div class="carousel__item img_size "> 
              <img :src="movieBoxPoster[index]" class="animate__animated" style=" height: 420px; cursor: pointer; border-radius: 10px;" alt="" :class="item_animate"
              @mouseenter="mouse1"
              @mouseleave="mouse2"
              @click="goBoxOffice(index, topMovie, movieBoxPoster[index])"
              :topMovie="topMovie"
              >
            </div>
          </Slide>
        <Pagination/>
      </Carousel>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Carousel, Pagination, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import axios from 'axios'
import { useMovieStore } from '@/stores/movies'
import { useRouter } from "vue-router";



const store = useMovieStore()

const props = defineProps({
  movieList:Object
})

const movieBox = ref([])
let movieBoxPoster = ref([])
let movieIndex =ref(0)

const router = useRouter()
const goBoxOffice = function(index, item, poster){
  store.movieDetail = item
  store.PosterDetail  = poster
  store.movieIndex = index
  // console.log(poster)
  router.push({name:'DetailView', params:{ id: index }})
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



onMounted(() =>{
  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/boxOffice/`
  })
  .then ((res) =>{
    movieBox.value = res.data
    // console.log(movieBox)
  })
  .catch((err) =>{
    console.log(err)
  })
    axios({
    method:'get',
    url: `${store.API_URL}/api/v1/movies/boxOffice_poster/`
  })
  .then ((res) =>{
    movieBoxPoster.value=res.data
    // console.log(movieBoxPoster)
  })


  
})









</script>

<style scoped>
.title {
  color: antiquewhite;
  font-size: 50px;
  text-shadow: 5px 5px 5px black; 
}

.title_font {
  /* font-family: 'Comfortaa', sans-serif; */
  font-family: 'Russo One', sans-serif;
  /* font-family: 'Vina Sans', sans-serif; */
}

.img_size {
  box-shadow: 10px 10px 10px black;
}
.icon_style {
  height: 40px;
}

.carousel__slide {
  padding: 5px;
}

.carousel__viewport {
  perspective: 2000px;
}

.carousel__track {
  transform-style: preserve-3d;
}

.carousel__slide--sliding {
  transition: 0.5s;
}

.carousel__slide {
  opacity: 0.9;
  transform: rotateY(-20deg) scale(0.9);
}

.carousel__slide--active ~ .carousel__slide {
  transform: rotateY(20deg) scale(0.9);
}

.carousel__slide--prev {
  opacity: 1;
  transform: rotateY(-10deg) scale(0.95);
}

.carousel__slide--next {
  opacity: 1;
  transform: rotateY(10deg) scale(0.95);
}

.carousel__slide--active {
  opacity: 1;
  transform: rotateY(0) scale(1.1);
}

.text_style {
  color: white;
}

.rank {
  position: absolute;
  color:white;
  /* font-size: 50px; */
}

</style>