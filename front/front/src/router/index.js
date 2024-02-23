import { createRouter, createWebHistory } from 'vue-router'
import DetailView from '@/views/DetailView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import LogOutView from '@/views/LogOutView.vue'
import HomeView from '@/views/HomeView.vue'
import MainView from '@/views/MainView.vue'
import MovieListView from '@/views/MovieListView.vue'
import MovieTeaserView from '@/views/MovieTeaserView.vue'
import NationalDetailView from '@/views/NationalDetailView.vue'
import MypageView from '@/views/MypageView.vue'
import CategoryDetailView from '@/views/CategoryDetailView.vue'
import CategoryNationalView from '@/views/CategoryNationalView.vue'
import MovieWorldCupView from '@/views/MovieWorldCupView.vue'
import CinemaView from '@/views/CinemaView.vue'
import RecommendView from '@/views/RecommendView.vue'
import WorldCupResultView from '@/views/WorldCupResultView.vue'

import { useCounterStore } from '@/stores/counter'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/main',
      name: 'main',
      component: MainView
    },
    {
      path: '/movies',
      name: 'movies',
      component: MovieListView
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendView
    },
    {
      path: '/movies/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/logout',
      name: 'LogOutView',
      component: LogOutView
    },
    {
      path: '/teaser/:id',
      name: 'teaser',
      component: MovieTeaserView
    },
    {
      path: '/national/:id',
      name: 'national',
      component: NationalDetailView
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: MypageView
    },
    {
      path: '/category/:moviename',
      name: 'category',
      component: CategoryDetailView
    },
    {
      path: '/category_national/:idx',
      name: 'category_national',
      component: CategoryNationalView
    },
    {
      path: '/cinema',
      name: 'cinema',
      component: CinemaView
    },
    {
    path: '/worldcup',
    name: 'worldcup',
    component: MovieWorldCupView
    },
    {
      path: '/worldcup_result/:idx',
      name: 'worldcup_result',
      component: WorldCupResultView
      },
    
  ]
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'main' && !store.isLogin){
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView'}
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)){
    window.alert('이미 로그인이 되어있습니다.')
    return { name: 'main'}
  }
})

export default router
