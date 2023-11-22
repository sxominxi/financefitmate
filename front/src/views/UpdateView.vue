<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <h1>게시글 수정 페이지</h1>
            <div class="card">
               <div class="card-body">
                     <form @submit.prevent="update">
                        <p class="card-title">제목:</p>
                        <input type="text" v-model="title">
                        <p class="card-title">내용:</p>
                        <input type="textarea" v-model="content">
                        <br>
                        <input type="submit" value="게시글 수정">
                     </form>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/modules/counter'
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const store = useCounterStore()
const router = useRouter()
const route = useRoute()
const postId = ref(route.params.id)

const formerPost = ref(null)

onMounted(() => {
   store.getPosts()
})

const selected = ref('')
const title = ref('')
const content = ref('')


watch(() => store.posts, (newValue, oldValue) => {
   const former = computed(() => {return store.posts.find((item) => item.pk == postId.value)})
   formerPost.value = former.value
   title.value = formerPost.value.title
   content.value = formerPost.value.content
})

const update = function () {
   axios({
       method: 'put',
       url: `${store.API_URL}/posts/${postId.value}/`,
       data: {
           title: title.value,
           content: content.value
       }
   })
   .then((res) => {
       store.post.value = res.data
   })
   .catch((err) => {
       console.log(err)
   })
   
   router.push({
       name: 'DetailView',
       params: { id: postId.value }
   })
}

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