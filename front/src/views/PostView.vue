<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="post-page">
               <div class="title-box">
                  <div class="title">
                     <div class="border border-3 border-bottom-0 border-success rounded-top">
                        <h1 class="fs-3 bw-bold"><strong>게시판</strong></h1>
                     </div>
                  </div>
                  <div class="title-etc">
                     <div class="border-3 border-bottom border-success"></div>
                  </div>
               </div>
               <PostList />
            </div>
         </div>
      </div>
   </div>
 </template>
 
 <script setup>
 import { onMounted } from 'vue'
 import { useCounterStore } from '@/stores/modules/counter'
 import { RouterLink } from 'vue-router'
 import { useRouter } from 'vue-router'
 import PostList from '@/components/PostList.vue'
 
 const store = useCounterStore()

 onMounted(() => {
   store.getPosts()
 })
 
 </script>
 
 <style scoped>
 .create-button {

 }


 </style>
 