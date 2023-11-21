<template>
  <div>
    <h1>Detail</h1>
    <div v-if="post">
      <p>제목 : {{ post.title }}</p>
      <p>내용 : {{ post.content }}</p>
      <p>작성일 : {{ post.created_at }}</p>
      <p>수정일 : {{ post.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/modules/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const post = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/posts/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      post.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<style>

</style>
