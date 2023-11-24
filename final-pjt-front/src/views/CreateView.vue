<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1><strong>게시글 작성</strong></h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
            <div class="card-box">
               <div class="card">
                  <div class="card-body">
                     <form @submit.prevent="createPost">
                           <p class="card-title">제목:</p>
                           <input class="form-control text-left" type="text" v-model.trim="title">
                           <p class="card-title">내용:</p>
                           <input class="form-control text-left" type="textarea" v-model="content">
                           <br>
                           <div class="card-button">
                              <button class="btn btn-success">게시글 작성</button>
                           </div>
                     </form>
                  </div>
               </div>
            </div>
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
       router.push({ name: 'PostView' })
     })
     .catch((err) => {
       console.log(err)
     })
 }
 
 
 
 </script>
 
 <style scoped>

.card {
   margin-top: 40px;
}

.form-control {
   width: 100%;
   height: 300px;
   margin-bottom: 30px;
}

.card-button {
   display: flex;
   justify-content: end;
}

 </style>
 