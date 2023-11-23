<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1><strong>게시글 수정</strong></h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
            <div class="card">
               <div class="card-body">
                     <form @submit.prevent="update">
                        <p class="card-title">제목:</p>
                        <input class="form-control text-left" type="text" v-model="title">
                        <p class="card-title">내용:</p>
                        <input class="form-control text-left" type="textarea" v-model="content">
                        <br>
                        <div class="card-button">
                           <button class="btn btn-info">게시글 수정</button>
                        </div>
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

.card {
   margin-top: 40px;
}

.form-control {
   width: 100%;
   height: 300px;
   margin-bottom: 30px;
}

.card-button {
   display: flex;
   justify-content: end;
}
</style>