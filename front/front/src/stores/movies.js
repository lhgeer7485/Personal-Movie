import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useMovieStore = defineStore('movies', () => {




  //----------------------------------------------------------------------------------------------------------

  // // 영화 리스트 저장 리스트
  const movies = ref([])
    // 영화 디테일 저장 리스트
  const movieDetail = ref({})

  const PosterDetail = ref('')
  // 영화 진흥원 API / 맨끝에는 날짜를 입력
  const API_URL = 'http://127.0.0.1:8000'

  const idx = ref(0)

  // 나라별 영화 디테일 저장 리스트
  const genreKorea = ref({})
  const genreJapan = ref({})
  const genreChina = ref({})
  const genreForiegn = ref({})

  // 분류별 영화 디테일 저장 리스트
  const genreNor = ref({})
  const genreAni = ref({})
  const genreDocu = ref({})
  const genreLive = ref({})


  // 영화 진흥원에서 일간 박스오피스 정보를 가져온다
  const getMovies = function () {
    axios({
      method: 'get',
      url: API_URL
    })
      .then((response) => {
        // 영화 리스트를 저장
        // movies.value = response.data.boxOfficeResult.dailyBoxOfficeList
        
      })
      .catch((error) => {
        console.log(error)
      })
  }

  // //----------------------------------------------------------------------------------------------------------

  const mapInfo = ref('인동')























  return { movies, API_URL, movieDetail,PosterDetail, idx,
    genreKorea, genreJapan, genreChina, genreForiegn,
    genreNor, genreAni, genreDocu, genreLive, mapInfo
  }
}, { persist: true }
)
