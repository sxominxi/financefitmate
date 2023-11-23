<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1>로그인</h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
            <div class="login-box">
               <div class="form-tag">
                  <form @submit.prevent="logIn">
                     <div>
                        <label for="id">아이디: </label>
                        <input class="form-control" type="text" id="id" v-model.trim="username"><br>
                        <label for="password">패스워드: </label>
                        <input class="form-control" type="password" id="password" v-model.trim="password">
                     </div>
                     <div class="form-button">
                        <button class="btn btn-success">로그인</button>
                     </div>
                  </form>
               </div>
            </div>
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
.form-tag {
   display: flex;
   flex-direction: column;
   align-items: center;
   justify-content: center;
   width: 30%;
   height: 70%;
   border: 1px solid #ddd;
   border-radius: 15px;
}

.login-box {
   display: flex;
   flex-direction: column;
   align-items: center;
   justify-content: center;
   height: 600px;
}

.form-tag button {
   text-align: center;
   margin-top: 40px;
}

.form-button {
   display: flex;
   flex-direction: column;
}
</style>
