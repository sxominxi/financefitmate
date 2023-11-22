<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
         <h1>게시글 작성</h1>
         <form @submit.prevent="createPost">
            <div>
               <label for="title">제목:</label>
               <input type="text" v-model.trim="title" id="title">
            </div>
            <div>
               <label for="content">내용:</label>
               <textarea v-model.trim="content" id="content"></textarea>
            </div>
            <input type="submit">
         </form>
         </div>
      </div>
   </div>
 </template>
 
 <script setup>
 import { ref } from 'vue'
 import axios from 'axios'
 import { useCounterStore } from '@/stores/modules/counter'
 import { useRouter } from 'vue-router'
 
 const title = ref(null)
 const content = ref(null)
 const store = useCounterStore()
 const router = useRouter()
 
 const createPost = function () {
   axios({
     method: 'post',
     url: `${store.API_URL}/posts/`,
     data: {
       title: title.value,
       content: content.value
     },
     headers: {
       Authorization: `Token ${store.token}`
     }
   })
     .then((res) => {
       // console.log(res)
       router.push({ name: 'PostView' })
     })
     .catch((err) => {
       console.log(err)
     })
 }
 
 
 
 </script>
 
 <style scoped>
 #wrap {
  display: flex;
  justify-content: center;
  padding: 0px 100px; /* 기본값은 50px */
}

/* 페이지 내 컨텐츠를 감싸는 컨테이너 */

.check {
  background-color: #fff;
  padding: 20px 0;
  width: 80%;
  position: relative;
  overflow: hidden; /* 부모 요소의 내용이 넘칠 때 숨김 처리 */
}

/* 미디어 쿼리를 이용한 반응형 조정 */
@media screen and (max-width: 1000px) {
  /* 현재 창 크기가 600px 이하인 경우 */
#wrap {
   padding: 0; /* 좁은 화면에서는 양 옆 공백을 줄입니다. */
   }

.deposit {
   padding: 20px 0; /* 상하 여백은 필요에 따라 조절하세요 */
  }
.check{
   width: 100%;
   }
}

.inner {
   border: 1px solid #ddd;
   border-radius: 8px;
   padding: 20px;
   background-color: #fff;
}
 
 </style>
 