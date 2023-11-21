<template>
   <div>
     <h1>Post Page</h1>
     <RouterLink :to="{ name: 'CreateView' }">
       [CREATE]
     </RouterLink>
     <PostList />
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
 
 <style>
 
 </style>
 