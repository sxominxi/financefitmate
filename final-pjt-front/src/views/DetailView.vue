<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1 class="fs-3 fw-bold">게시글 상세 조회</h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
            <div class="post-main" v-if="store.post">
              <h3>{{ store.post.title }}</h3>
              <hr>
              <div class="post-content">
                <p>{{ store.post.content }}</p>
      
              </div>
              <hr>
              <div class="post-bot">
                <div class="post-side">
                  <p>작성자: {{ store.post.user }}</p>
                  <p>작성일: {{ store.post.created_at }}</p>
                </div>
                <div v-if="store.post.user == store.username">
                   <button class="btn btn-outline-info" @click="goUpdate">수정</button> <button class="btn btn-outline-warning" @click="deletePost">제거</button>
                </div>
              </div>
            </div>
            
            <form @submit.prevent="createComment">
              <div class="comment-list">
                <div class="comment-input input-group input-group-sm mb-3">
                  <span class="input-group-text border-success" id="inputGroup-sizing-sm">{{ store.post.user }}</span>
                  <input type="text" class="form-control border-success" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm"  v-model="content">
                </div>
                 <button class="btn btn-outline-success">댓글 작성</button>
              </div>
            </form>
            <div class= "comment-st" v-if="computedComments.length > 0">
               <div v-for="comment in computedComments" :key="comment.id">
                <div class="comment-pr card">
                  <div class="comment-content">
                    <p> 익명 댓글 : {{ comment.content }}</p>
                  </div>
                  <div class="comment-actions" v-if="comment.user == store.userInfo.pk">
                      <button class="btn btn-outline-warning" @click="deleteComment(comment)">삭제하기</button>
                  </div>
                </div>
               </div>
            </div>
         </div>
      </div>
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
    store.userFind()
    userDetail()
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
       content: content.value,
     },
     headers: {
       Authorization: `Token ${store.token}`
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

const deleteComment = function (comment) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/posts/comments/${comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    store.getComment()
    router.push({ name: 'DetailView' })
  })
  .catch((err) => {
    console.log(err)
  })
}

 
const computedComments = computed(() => {
  const filterComments = store.comments.filter((comment) => comment.post == postId.value)
  return filterComments
})

const userDetailInfo = ref([])
const userDetail = function() {
    axios({
            method: 'get',
            url: `${store.API_URL}/account/user-info/${store.userInfo.pk}`,
            headers: {Authorization: `Token ${store.token}`}
        })
        .then((res) => {
            userDetailInfo.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
}
 
 </script>
 
 <style scoped>
 .post-main {
  margin-top: 50px;
 }

 .post-main h3{
    margin-bottom: 30px;
 }

 .post-side p {
  margin-bottom: 5px;
 }

 .post-content {
  height: 300px;
 }

 .post-bot {
  display: flex;
  justify-content: space-between;
  margin-bottom: 30px;
 }

 .comment-input {
  width: 88%;

 }
 
 .comment-input input {
  height: 50px;
 }

 .comment-list {
  display: flex;
  justify-content: space-between;
 }

 .comment-list button{
  height: 50px;
 }

 .comment-pr {
    width: 100%;
    height: 80px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding-top: 10px;
    margin-bottom: 20px;
  }

  .comment-content {
    width: 80%;
    margin-left: 20px;
  }

  .comment-actions {
    margin-right: 20px;
  }

 </style>
 