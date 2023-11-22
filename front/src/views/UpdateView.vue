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
</style>