<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">

            <h1>Login</h1>
            <form @submit.prevent="logIn">
               <input type="text" v-model.trim="username">
               <input type="password" v-model.trim="password">
               <input type="submit">
            </form>
         </div>
      </div>
   </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/modules/counter'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
</style>
