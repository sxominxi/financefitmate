<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">

         <h1>Post Page</h1>
         <RouterLink :to="{ name: 'CreateView' }">
            [CREATE]
         </RouterLink>
         <PostList />
         </div>
      </div>
   </div>
 </template>
 
 <script setup>
 import { onMounted } from 'vue'
 import { useCounterStore } from '@/stores/modules/counter'
 import { RouterLink } from 'vue-router'
 import PostList from '@/components/PostList.vue'
 
 const store = useCounterStore()
 
 onMounted(() => {
   store.getPosts()
 })
 
 </script>
 
 <style scoped>
 </style>
 