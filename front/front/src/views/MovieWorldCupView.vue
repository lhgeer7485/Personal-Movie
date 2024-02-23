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





    <p class="title korean_font" style="display: flex; ">
        영화 이상형 월드컵
        <img src="@/assets/icon/trophy.png" alt="" style="height: 50px; margin-left: 15px;">
    </p>
    <div style="text-align: center;">
      <div v-if="flag">
        <div>
          <div class="winner_box">
            <!-- <h1 style="font-size: 40px;" >Winner</h1> -->
            <img src="@/assets/icon/winner.png" class="animate__animated animate__tada" alt="" style="height: 120px;">
            <br>
            <img style="height: 500px; border-radius: 5px;" :src=win_img alt="사진이 없습니다" @click="">
            <p class="text_style">{{ win.title }}</p>
          </div>
          <div style="display: flex; justify-content: center;">
            <button class="recommend_btn" style="display: flex; align-items: center;" @click="fnc">관련영화 추천받기 &nbsp;
              <img src="@/assets/icon/recommend.png" class="animate__animated animate__rubberBand animate__infinite" alt="" style="height: 40px;">
            </button>
          </div>
        </div>
      </div>
      
      <div v-else>
        <h1 class="korean_font" style="font-size: 40px;" v-if="stage>1"> {{ stage }} 강 - {{ cnt }} / {{ stage }} </h1>
        <h1 class="korean_font" style="font-size: 40px;" v-else> 파이널 - {{ cnt }} / {{ stage }} </h1>
        <br>
        <div style="display: grid; grid-template-columns: 2fr 1fr 2fr;">
          <div style="width: 600px; margin-left: auto; margin-right: auto;" >
            <img :src=img1 alt="사진이 없습니다" style="height: 500px; border-radius: 5px; cursor: pointer; box-shadow: 5px 5px 5px black;" @click="img1Event">
            <p class="text_style">{{ img1_title }}</p>
          </div>
          <div>
            <!-- <p style="color: white; font-size: 40px;">VS</p> -->
            <img src="@/assets/icon/vs2.png" alt="" style="height: 200px; margin-top: 100px;" class="animate__animated animate__headShake animate__infinite">
          </div>
          <div  style="width: 600px; margin-left: auto; margin-right: auto;">
            <img :src=img2 alt="사진이 없습니다" style="height: 500px; border-radius: 5px; cursor: pointer; box-shadow: 5px 5px 5px black;" @click="img2Event">
            <p class="text_style">{{ img2_title }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios, { Axios } from 'axios'
import { ref, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { useMovieStore } from '@/stores/movies'

const userStore = useCounterStore()
const route = useRoute()
const movieStore = useMovieStore()

const img1 = ref('')
const img2 = ref('')

const img1_title = ref('')
const img2_title = ref('')

const list_16 = ref([])
const list_8 = ref([])
const list_4 = ref([])
const list_2 = ref([])
const win = ref([])

const win_img = ref('')

const stage = ref(8)

const cnt = ref(1)



const flag = ref(false)
const router = useRouter()


const fnc = function () {
  console.log(win.value.id)
  router.push({name: 'worldcup_result', params:{idx:win.value.id}})
}




const img1Event = function () {

  if (cnt.value <= 8 && list_16.value.length > 0 && stage.value == 8) {
      if (list_16.value.length == 2) {
          const tmp1 = list_16.value.shift()
          const tmp2 = list_16.value.shift()
          list_8.value.push(tmp1)
          cnt.value = 1
          stage.value = 4
          img1.value = list_8.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img1_title.value = list_8.value[0].title

          img2.value = list_8.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img2_title.value = list_8.value[1].title

      }
      else{
          const tmp1 = list_16.value.shift()
          const tmp2 = list_16.value.shift()
          list_8.value.push(tmp1)

          img1.value = list_16.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img1_title.value = list_16.value[0].title

          img2.value = list_16.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img2_title.value = list_16.value[1].title

          cnt.value += 1
      }

  }  

  else if (cnt.value <= 8 && list_8.value.length > 0 && stage.value == 4) {

      if (list_8.value.length == 2) {
          const tmp1 = list_8.value.shift()
          const tmp2 = list_8.value.shift()
          list_4.value.push(tmp1)
          cnt.value = 1
          stage.value = 2

          img1.value = list_4.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img1_title.value = list_4.value[0].title

          img2.value = list_4.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img2_title.value = list_4.value[1].title

      }
      else{
          const tmp1 = list_8.value.shift()
          const tmp2 = list_8.value.shift()
          list_4.value.push(tmp1)

          img1.value = list_8.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img1_title.value = list_8.value[0].title

          img2.value = list_8.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img2_title.value = list_8.value[1].title

          cnt.value += 1
      }

  }  

  else if (cnt.value <= 4 && list_4.value.length > 0 && stage.value == 2) {


      if (list_4.value.length == 2) {
          const tmp1 = list_4.value.shift()
          const tmp2 = list_4.value.shift()
          list_2.value.push(tmp1)
          cnt.value = 1
          stage.value = 1

          img1.value = list_2.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img1_title.value = list_2.value[0].title

          img2.value = list_2.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img2_title.value = list_2.value[1].title

      }
      else{
          const tmp1 = list_4.value.shift()
          const tmp2 = list_4.value.shift()
          list_2.value.push(tmp1)

          img1.value = list_4.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img1_title.value = list_4.value[0].title

          img2.value = list_4.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
          img2_title.value = list_4.value[1].title

          cnt.value += 1
      }

  } 

  else {
      win.value = list_2.value[0]
      console.log(win.value)
      flag.value = true
      win_img.value = list_2.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
      
  }
      

}

//-------------------------------------------------------------------------------------------------------------------------------------------------


const img2Event = function () {

if (cnt.value <= 8 && list_16.value.length > 0 && stage.value == 8) {
    if (list_16.value.length == 2) {
        const tmp1 = list_16.value.shift()
        const tmp2 = list_16.value.shift()
        list_8.value.push(tmp2)
        cnt.value = 1
        stage.value = 4
        img1.value = list_8.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img1_title.value = list_8.value[0].title

        img2.value = list_8.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img2_title.value = list_8.value[1].title

    }
    else{
        const tmp1 = list_16.value.shift()
        const tmp2 = list_16.value.shift()
        list_8.value.push(tmp2)

        img1.value = list_16.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img1_title.value = list_16.value[0].title

        img2.value = list_16.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img2_title.value = list_16.value[1].title

        cnt.value += 1
    }

}  

else if (cnt.value <= 8 && list_8.value.length > 0 && stage.value == 4) {

    if (list_8.value.length == 2) {
        const tmp1 = list_8.value.shift()
        const tmp2 = list_8.value.shift()
        list_4.value.push(tmp2)
        cnt.value = 1
        stage.value = 2

        img1.value = list_4.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img1_title.value = list_4.value[0].title

        img2.value = list_4.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img2_title.value = list_4.value[1].title

    }
    else{
        const tmp1 = list_8.value.shift()
        const tmp2 = list_8.value.shift()
        list_4.value.push(tmp2)

        img1.value = list_8.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img1_title.value = list_8.value[0].title

        img2.value = list_8.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img2_title.value = list_8.value[1].title

        cnt.value += 1
    }

}  

else if (cnt.value <= 4 && list_4.value.length > 0 && stage.value == 2) {


    if (list_4.value.length == 2) {
        const tmp1 = list_4.value.shift()
        const tmp2 = list_4.value.shift()
        list_2.value.push(tmp2)
        cnt.value = 1
        stage.value = 1

        img1.value = list_2.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img1_title.value = list_2.value[0].title

        img2.value = list_2.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img2_title.value = list_2.value[1].title

    }
    else{
        const tmp1 = list_4.value.shift()
        const tmp2 = list_4.value.shift()
        list_2.value.push(tmp2)

        img1.value = list_4.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img1_title.value = list_4.value[0].title

        img2.value = list_4.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
        img2_title.value = list_4.value[1].title

        cnt.value += 1
    }

} 

else {
    win.value = list_2.value[1]
    console.log(win.value)
    flag.value = true
    win_img.value = list_2.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
    
}
    

}






// watch(img1, (newValue, oldValue) => {img1.value = newValue})
// watch(img2, (newValue, oldValue) => {img2.value = newValue})

axios({
  method: 'get',
  url: 'http://127.0.0.1:8000/api/v1/movies/worldcup/'
})
.then((res) => {
  list_16.value = res.data
  
  // 포스터 하나
  img1.value = list_16.value[0].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]
  img2.value = list_16.value[1].posters.replace('[',"").replace(']',"").replace("'","").replace("'","").split(',')[0]

  img1_title.value = list_16.value[0].title
  img2_title.value = list_16.value[1].title
  
})
</script>


<style scoped>
.container {
  margin: 0px;
  min-height: 100vh;
  background-color: #141517;
}

.title {
  color: white;
  padding: 50px;
  margin: 0px;
  font-size: 50px;
  /* font-weight: bold; */
  text-shadow: black 2px 2px;
}


.text_style {
  color: white;
  font-size: 35px;
  font-family: 'Russo One', sans-serif;
  text-shadow: 3px 3px 2px #0B220E;


}

.form_style {
  border: solid 1px wheat;
  border-radius: 5px;
  border: hidden;
  width: 90%;
  height: 300px;
  padding: 50px;
  margin-left: auto;
  margin-right: auto;
}

.form_title {
  color: antiquewhite;
  font-size: 80px;
  font-weight: bold;
  text-shadow: 3px 3px 2px #0B220E;
  font-family: 'Jost', sans-serif;
}

.winner_box {
  width: 500px;
  background-color: black;
  border-radius: 10px;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
  margin-bottom: 20px;
}
.recommend_btn {
  background-color:  #FFC300 ;
  font-size: 25px;
  font-weight: bold;
  border-radius: 10px;
  padding: 10px;
  margin-bottom: 50px;
  cursor: pointer;
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
.korean_font {
  font-family: 'Black Han Sans', sans-serif;
}
</style>