<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1>회원가입</h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
            <form @submit.prevent="signUp">
               <p>username : <input type="text" v-model.trim="username"></p>
               <p>lastname : <input type="text" v-model.trim="last_name"></p>
               <p>firstname : <input type="text" v-model.trim="first_name"></p>
               <p>email: <input type="text" v-model.trim="email"></p>
               <p>password : <input type="password" v-model.trim="password1"></p>
               <p>password confirmation : <input type="password" v-model.trim="password2"></p>
               <p>nickname: <input type="text" v-model.trim="nickname"></p>
               <p>age: <input type="text" v-model.trim="age"></p>
               <p>money: <input type="text" v-model.trim="money"></p>
               <p>salary: <input type="text" v-model.trim="salary"></p>
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
const first_name = ref(null)
const last_name = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    first_name: first_name.value,
    last_name: last_name.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
  }
  store.signUp(payload)
}


</script>

<style scoped>

</style>
