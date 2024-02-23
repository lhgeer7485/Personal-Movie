<template>
  <body>
    <section class="background-section">
      <!-- 내용을 이곳에 추가하세요 -->
      <h1 class="main_font animate__animated animate__slideInRight">Play Personal Movie</h1>
    </section>
    <div>
      
    </div>
    <div>
      <div style="height: 500px;">

      </div>
      <div class="div1 " >
        <div style="display: flex; justify-content: center;">
          <button :class="item_animate"
          @mouseenter="mouse1"
          @mouseleave="mouse2"
          @click="goMain()" class="main_btn btn_font animate__animated " id="div1">Enter</button>
        </div>
        <img class="second" src="@/assets/background1.jpg"  alt="">
      </div>
    </div>
  </body>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useRouter } from 'vue-router';  
import { onMounted,ref } from 'vue';
const router = useRouter()

const goMain = function() {
  router.push({ name: 'main' })
}

onMounted(()=>{
  let observer = new IntersectionObserver((e) => {
        e[0].target.classList.add('animate__fadeInUpBig')
        e[0].target.classList.add('animate__delay-2s')


  
      
  })
  
  let div1 = document.querySelector('#div1')
  observer.observe(div1)


})

const item_animate = ref({
  'animate__pulse' : false
})
const mouse1 = function(event){
    item_animate.value.animate__pulse = true
}
const mouse2 = function(event){
    event.currentTarget.classList.remove('animate__pulse')
}
// -----------------------------------------------------------------//


</script>


<style scoped>


body {
  margin: 0;
  min-height: 100vh;
  background-color: black;
}

.background-section {
  margin: 0;
  min-height: 100vh;
  background-color: black;
  background: url("@/assets/background2.jpg");
  background-size: cover;
}

section:before {
  content:'';
  background: linear-gradient(to top, black, transparent);
  filter: brightness(90%);
  position: absolute;
  right: 0;
  height: 100vh;
  width: 100%;
}

.second {
  width: 100% ;
}

/* .main_line {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 120px;
  margin-left: auto;
  margin-right: auto;
  padding-top: 200px;

} */


.main_font {
  position: absolute;
  top: 150px;
  right: 50px;
  text-align: right;
  font-family: 'Russo One', sans-serif;
  font-size: 60px;
  color: white;
}

.main_btn {
  display: flex;
  justify-content: center;
  border: 1px solid white;
  padding: 15px 30px 15px 30px;
  text-decoration: none;
  color: white;
  background-color: black;
  cursor: pointer;
}
.btn_font {
  color: white;

}
</style>
