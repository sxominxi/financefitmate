<template>
  <div class="card border-success" @click="goComment(post.pk)">
   <div class="card-main">
     <div class="card-top">
       <h5 class="card-title fs-4"><strong>{{ post.title }}</strong></h5>
       <div class="card-side">
         <p class="card-text1">작성자 : {{ post.user }}</p>
         <h6 class="card-subtitle mb-2 text-body-secondary">{{ post.pk }}번째 게시글</h6>
       </div>
     </div>
   </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()
const goComment = function (post_id) {
   router.push({
         name: 'DetailView',
         params: { id: post_id }
     })
}

defineProps({
  post: Object
})
</script>

<style scoped>
.card {
 margin: 20px 0;
}
.card-main {
 margin: 20px;
}

.card-top {
 display: flex;
 justify-content: space-between;
}

.card-main h6 {
 display: flex;
 justify-content: end;
}

.card:hover {
   cursor: pointer;
}
</style>