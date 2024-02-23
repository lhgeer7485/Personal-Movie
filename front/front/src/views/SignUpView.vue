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
    <div style="display: grid;  grid-template-columns: 1fr 1fr; padding: 50px; ">
      <div class="form_style">
        <p class="form_title">Sign Up</p>
        <form @submit.prevent="signUp">
        <div>
          <br>
          <label class="text_style" for="username">아이디</label>
        </div>
        <div>
          <input class="input_box " type="text" id="username" v-model.trim="username">
        </div>
        <div>
          <br>
          <label class="text_style" for="userid">이메일</label>
        </div>
        <div>
          <input class="input_box " type="text" id="userid" v-model.trim="userid">
        </div>
        <div>
          <br>
          <label class="text_style"  for="password1">비밀번호</label>
        </div>
        <div>
          <input class="input_box " type="password" id="password1" v-model.trim="password1">
        </div>
        
        <div>
          <br>
          <label class="text_style"  for="password2">비밀번호 재확인</label>
        </div>
        <div>
          <input class="input_box " type="password" id="password2" v-model.trim="password2">
        </div>       

        <div>
          <br>
          <label class="text_style"  for="age">나이</label>
        </div>
        <select style="font-size: 20px" name="age" id="age" v-model="age" class="st-font">
          <option :value="age" v-for="(age, idx) in userStore.ages" :key="idx">{{ age }}</option>
        </select>
        <div>
          <br>
          <label class="text_style" for="sex">성별</label>
        </div>
        <select style="font-size: 20px" name="sex" id="sex" v-model="sex" class="st-font">
          <option :value="sex" v-for="(sex, idx) in userStore.sex" :key="idx">{{ sex }}</option>
        </select>
        
        <div>
          <br>
          <input class="submit_box" type="submit" value="회원가입">
        </div>
        
        </form>
      </div>
      <div class="animate__animated animate__slideInUp" style="width: 60%;">
        <img src="@/assets/background8.jpg" alt="" style="border-radius: 5px;" 
        >
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const userid = ref(null)
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const sex = ref(null)
const age = ref(null)

const userStore = useCounterStore()

const signUp = function () {
    const payload = {
      userid : userid.value,
      username : username.value,
      password1 : password1.value,
      password2 : password2.value,
      sex : sex.value,
      age : age.value

    }
    userStore.signUp(payload)
  }

  // .---------------------------------


</script>

<style scoped>
.submit_box {
  width: 100%;
  height: 70px;
  border-radius: 10px;
  border: solid 1px #0B220E; 
  font-size: 25px;
  font-weight: 900;
  letter-spacing: 1px;
  color: #C31147;
  transition: color 0.75s ease-in-out;
  text-decoration: none;
  text-transform: uppercase;
  position: relative;

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

.sub_title {
  font-size: 40px;
  margin-bottom: 10px;
  color: beige;
}
.text_style {
  color: beige;
  text-align: start;
  font-size: 25px;
}

.form_style {
  border: hidden;
  border-radius: 10px;
  width: 70%;
  padding: 10px;
  margin-left: auto;
  margin-right: auto;
  /* text-align: center; */
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
  padding-left: 10px;
  font-size: 27px;
  margin-top: 10px;
  margin-bottom: 10px;
  width: 100%;
  height: 40px;
  background-color: #DADADA;
  border: hidden;
  border-bottom: #0B220E solid 2px;
  border-radius: 5px;
  box-shadow: inset 6px 6px 10px gray;
}


.radio_box {
  margin-left: 30px;
  margin-right: 10px;
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