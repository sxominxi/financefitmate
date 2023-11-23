<template>
  <div>
    <div class="top-box">
      <h3>게시글 리스트</h3>
      <button class="create-button btn btn-success" @click="createPost">게시글 작성</button>
    </div>
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
 import { useRouter } from 'vue-router'
 
 const store = useCounterStore()
 const router = useRouter()

 const createPost = function() {
   router.push({ name: 'CreateView' }); 
 }
 </script>

<style scoped>
.create-button {


}
.top-box {
  margin: 30px 0; 
  display: flex;
  justify-content: space-between;
}
</style>