<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <h1>Signup</h1>
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
