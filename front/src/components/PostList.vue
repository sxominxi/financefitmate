<template>
   <div>
     <h3>Post List</h3>
     <PostListItem 
       v-for="post in store.posts"
       :key="post.pk"
       :post="post"
     />
   </div>
 </template>
 
 <script setup>
 import { useCounterStore } from '@/stores/modules/counter'
 import PostListItem from '@/components/PostListItem.vue'
 
 const store = useCounterStore()
 </script>
