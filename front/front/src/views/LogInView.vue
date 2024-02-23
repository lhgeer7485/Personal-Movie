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
    <div style="display: grid; grid-template-columns: 1fr 2fr; padding: 50px;">
      <div class=" animate__animated  animate__slideInLeft">
        <img src="@/assets/background4.jpg" alt="" 
        style="width: 80%;"
        >
      </div>
      <div >
      
        <div class="form_style">
          <form @submit.prevent="logIn">
            <p class="form_title" >Login</p>
            <div>
              <span>
                <label for="username" class="text_style"  >ID </label>
                <input class="input_box" type="text" id="username" v-model.trim="username">
              </span>
            </div>
            
            <div>
              <label for="password" class="text_style"  >PASSWORD </label>
              <input class="input_box"  type="password" id="password" v-model.trim="password">
            </div>
            <div>
              <input class="submit_box" type="submit" value="Login">
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';
const username = ref(null)
const password = ref(null)

const userStore = useCounterStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  userStore.logIn(payload)
}

</script>

<style scoped>
.submit_box {
  width: 100%;
  height: 90px;
  border-radius: 7px;
  border: solid 1px #0B220E; 
  border-radius: 10px;
  font-size: 27px;
  font-weight: 900;
  letter-spacing: 1px;
  color: #335940;
  text-shadow: 1.5px 1.5px #0B220E;
  transition: color 0.75s ease-in-out;
  text-decoration: none;
  text-transform: uppercase;
  position: relative;
  box-shadow: 4px 4px 4px black;


}

.input_box {
  padding-left: 10px;
  font-size: 27px;
}

.submit_box:hover {
  color: #333;
  transition: color 0.75s ease-in-out;
}


/* ------------------------------------------------------- */

.container {
  margin: 0px;
  min-height: 100vh;
  background-color: #141517;
}

.title {
  color: white;
  padding: 50px;
  margin: 0px;
}


.text_style {
  color: white;
  text-align: start;
  font-size: 25px;
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

.nav_font {
  font-family: 'Jost', sans-serif;
}

.input_box {
  margin-top: 10px;
  margin-bottom: 40px;
  width: 100%;
  height: 40px;
  background-color: #DADADA;
  border: hidden;
  border-bottom: #0B220E solid 2px;
  border-radius: 5px;
  box-shadow: inset 6px 6px 10px gray;
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