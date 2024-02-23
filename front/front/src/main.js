import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import VueCarousel from 'vue-carousel';
// import VueVideoPlayer from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'

const pinia = createPinia()
const app = createApp(App)
pinia.use(piniaPluginPersistedstate)
app.use(router)
app.use(VueCarousel);
app.use(pinia)
// app.use(VueVideoPlayer)

app.mount('#app')
