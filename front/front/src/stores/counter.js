import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const sex =  ref(["여성", "남성"])
  const ages =  ref(["10대", "20대", "30대", "40대", "50대", "60대", "70대", "80대", "90대",])
  const userInfo = ref([])


  const login = ref(false)

  const isLogin = computed(() => {
    if (token.value === null){
      return false
    } else{
      return true
    }
  })
  const token = ref(null)

  const API_URL = 'http://127.0.0.1:8000'


  const signUp = function (payload) {
    const { userid, username, password1, password2, sex, age } = payload 

    axios({
      method: 'post',
      url : `${API_URL}/accounts/signup/`,
      data: {
        userid, username, password1, password2, sex, age
      }
    }).then(res => {
      const password = password1
      logIn({ username, password })
      console.log('회원가입이 완료되었습니다.')
      // console.log(data)
    }).catch(err => console.log(err))
  }



  const logIn = function (payload) {
    const {username, password} = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then(res => {
      token.value = res.data.key
      router.push({name:'main'})
      console.log('로그인이 완료되었습니다.')
      console.log(res.data)
      console.log(token.value)
      axios({
        method:'get',
        url: `${API_URL}/accounts/info/`,
        headers :{
          Authorization : `Token ${token.value}`
        }
      })
      .then((res)=>{
        userInfo.value = res.data
        console.log(userInfo.value)
      })
    })
    .catch(err => console.log(err))
  }




  const logOut = function () {

    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
    .then(res => {
      token.value = null
      router.push({name:'LogInView'})
      console.log('로그아웃이 완료되었습니다.')
      console.log(res.data)
      console.log(token.value)
    })
    .catch(err => console.log(err))
  }



  return { API_URL, signUp, logIn, logOut, userInfo, token, isLogin, sex, ages }
}, { persist: true })
