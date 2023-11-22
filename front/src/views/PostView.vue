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
 #wrap {
  display: flex;
  justify-content: center;
  background-color: #f0f0f0;
  padding: 0px 50px; /* 기본값은 50px */
}

/* 페이지 내 컨텐츠를 감싸는 컨테이너 */

.check {
  background-color: #fff;
  padding: 20px 0;
  width: 100%;
  position: relative;
  overflow: hidden; /* 부모 요소의 내용이 넘칠 때 숨김 처리 */
}

/* 미디어 쿼리를 이용한 반응형 조정 */
@media screen and (max-width: 600px) {
  /* 현재 창 크기가 600px 이하인 경우 */
#wrap {
   padding: 0 10px; /* 좁은 화면에서는 양 옆 공백을 줄입니다. */
   }

.deposit {
   padding: 20px 0; /* 상하 여백은 필요에 따라 조절하세요 */
  }
}

.inner {
   border: 1px solid #ddd;
   border-radius: 8px;
   padding: 20px;
   background-color: #fff;
}
 
 </style>
 