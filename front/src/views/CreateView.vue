<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1>게시글 작성</h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
         <form @submit.prevent="createPost">
            <div>
               <label for="title">제목:</label>
               <input type="text" v-model.trim="title" id="title">
            </div>
            <div>
               <label for="content">내용:</label>
               <textarea v-model.trim="content" id="content"></textarea>
            </div>
            <input type="submit">
         </form>
         </div>
      </div>
   </div>
 </template>
 
 <script setup>
 import { ref } from 'vue'
 import axios from 'axios'
 import { useCounterStore } from '@/stores/modules/counter'
 import { useRouter } from 'vue-router'
 
 const title = ref(null)
 const content = ref(null)
 const store = useCounterStore()
 const router = useRouter()
 
 const createPost = function () {
   axios({
     method: 'post',
     url: `${store.API_URL}/posts/`,
     data: {
       title: title.value,
       content: content.value
     },
     headers: {
       Authorization: `Token ${store.token}`
     }
   })
     .then((res) => {
       // console.log(res)
       router.push({ name: 'PostView' })
     })
     .catch((err) => {
       console.log(err)
     })
 }
 
 
 
 </script>
 
 <style scoped>
 </style>
 