<template>
   <div>
     <h5>{{ post.pk }}번째 게시글</h5>
     <p>제목 :{{ post.title }}</p>
     <p>내용 : {{ post.content }}</p>
     <p>작성자 : {{ post.user }}</p>
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
 
 