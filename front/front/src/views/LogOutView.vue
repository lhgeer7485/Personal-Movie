<template>
  <div>
  </div>
</template>
<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
// import { useMovieStore } from '@/stores/movies'
import { useCounterStore} from '@/stores/counter'

const store = useCounterStore()

const router = useRouter()
onMounted(()=> {
          const result = confirm("로그아웃 하시겠습니까?");
          console.log(result)
          if(result) {
            store.token = null
            // localStorage.removeItem("TOKEN");
              router.push({name:'LogInView'}); //성공 시 login으로 이동
          }
      })
</script>
<style scoped>
</style>