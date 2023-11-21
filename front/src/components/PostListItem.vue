<template>
   <div>
     <h5>{{ post.pk }}번째 게시글</h5>
     <p>{{ post.title }}</p>
     <p>{{ post.content }}</p>
     <p>{{ post.user }}</p>
     <RouterLink :to="{ name: 'DetailView', params: { id: post.pk }}">
       [Detail]
     </RouterLink>
     <hr>
   </div>
 </template>
 
 <script setup>
 import { RouterLink } from 'vue-router'
 
 defineProps({
   post: Object
 })
 </script>
 
 