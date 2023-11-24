import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const posts = ref([])
  const username = ref('')
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const post = ref('')
   const getDetail = function (a) {
      axios({
         method: 'get',
         url: `${API_URL}/posts/${a}/`
      })
      .then((res) => {
         post.value = res.data
      })
      .catch((err) => {
         console.log(err)
      })
   }
   
  const getPosts = function () {
    axios({
      method: 'get',
      url: `${API_URL}/posts/`,
      headers: {Authorization: `Token ${token.value}`}
    })
      .then((res) =>{
        posts.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const comments = ref([])
  const getComment = function () {
      axios({
          method: 'get',
          url: `${API_URL}/posts/comments/`
      })
      .then((res) => {
          comments.value = res.data
      })
      .catch((err) => {
          console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, first_name, last_name, email, password1, password2, nickname, age, money, salary } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, first_name, last_name, email, password1, password2, nickname, age, money, salary
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        window.alert('모든 정보를 입력해주세요.')
        console.log(err)
      })
  }

  const logIn = function (payload) {
    username.value = payload.username
    const password = payload.password

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username : username.value,
        password
      }
    })
      .then((res) => {
        token.value = res.data.key
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        window.alert('아이디/패스워드가 틀렸습니다.')
        console.log(err)
      })
  }

  const userInfo = ref([])
  const userFind = function() {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/`,
      headers: {Authorization: `Token ${token.value}`}
    })

    .then((res) => {
      userInfo.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'HomeView' })
        
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const customProduct = ref([])
    const recommendProducts = function() {
        axios({
            method: 'get',
            url: `${API_URL}/service/recommend-service/`,
            headers: {Authorization: `Token ${token.value}`}
        })
        .then((res) => {
            customProduct.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
    }

  return {  posts, 
            API_URL, 
            getPosts, 
            signUp, 
            logIn, 
            token, 
            isLogin, 
            logOut, 
            getComment, 
            comments, 
            getDetail, 
            post, 
            username, 
            userInfo, 
            userFind, 
            customProduct,
            recommendProducts  
          }
}, { persist: true })
