<template>
   <div>
     <h1>Detail</h1>
     <div v-if="store.post">
       <p>제목 : {{ store.post.title }}</p>
       <p>내용 : {{ store.post.content }}</p>
       <p>작성일 : {{ store.post.created_at }}</p>
       <p>수정일 : {{ store.post.updated_at }}</p>
     </div>
     <div v-if="store.post.user == store.username">
       <button @click="goUpdate">수정</button> <button @click="deletePost">제거</button>
     </div>
   </div>
   <form @submit.prevent="createComment">
       <label class="me-2">내용 :</label>
       <input type="text" v-model="content">
       <input type="submit" value="댓글 작성">
    </form>
    <div v-if="computedComments.length > 0">
    <div v-for="comment in computedComments" :key="comment.id">
    <p>{{ comment.content }}</p>
      <div v-if="comment.user === store.username">
        <button @click="editComment(comment)">수정</button>
        <button @click="deleteComment(comment.id)">제거</button>
      </div>
    </div>
      <hr>
    </div>
 </template>
 
 <script setup>
 import axios from 'axios'
 import { onMounted, ref, computed } from 'vue'
 import { useCounterStore } from '@/stores/modules/counter'
 import { useRoute, useRouter } from 'vue-router'
 
 const store = useCounterStore()
 const route = useRoute()
 const postId = ref(route.params.id)
 const router = useRouter()
 
 onMounted(() => {
    store.getComment()
   store.getDetail(postId.value)
 })
 

 const goUpdate = function () {
   router.push({
             name: 'UpdateView',
             params: { id: postId.value }
     })
 }
 
 const deletePost = function () {
     axios({
         method: 'delete',
         url: `${store.API_URL}/posts/${postId.value}/`
     })
     .then((res) => {
       router.push({ name: 'PostView'})
     })
     .catch((err) => {
         console.log(err)
     })
 }
 
 const content = ref('')
 const createComment = function () {
   axios({
     method: 'post',
     url: `${store.API_URL}/posts/${postId.value}/comments/`,
     data: {
       content: content.value
     }
   })
   .then((res) => {
     store.getComment()
     content.value = ''
   })
   .catch((err) => {
     console.log(err)
   })
 }

//   const commentUpdate = function () {
//     router.push({
//              name: 'UpdateView',
//              params: { id: postId.value }
//      })
//  }
 
 const deleteComment = function () {
     axios({
         method: 'delete',
         url: `${store.API_URL}/comments/${postId.value}/`
     })
     .then((res) => {
       router.push({ name: 'DetailView'})
     })
     .catch((err) => {
         console.log(err)
     })
 }
 
 const computedComments = computed(() => {
   const filterComments = store.comments.filter((comment) => comment.post == postId.value)
   return filterComments
 })
 
 </script>
 
 <style>
 
 </style>
 