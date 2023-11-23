<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">

            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1>회원정보 수정</h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
            <form @submit.prevent="updateUserProfile">
               <label>이름: {{ store.username }}</label><br>
               <!-- <input type="text" v-model="username"><br> -->
               <label>이메일:</label>
               <input type="email" v-model="email"><br>
               <label>이름:</label>
               <input type="text" v-model="firstName"><br>
               <label>성:</label>
               <input type="text" v-model="lastName"><br>

               <label>닉네임:</label>
               <input type="text" v-model="nickName"><br>
               <label>나이:</label>
               <input type="number" v-model="age"><br>
               <label>현재 보유 자산:</label>
               <input type="number" v-model="money"><br>
               <label>연봉:</label>
               <input type="number" v-model="salary"><br>
               
               <button type="submit">정보 업데이트</button>

            </form>
         </div>
      </div>
   </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useCounterStore } from '@/stores/modules/counter'
import { useRouter } from 'vue-router';

const router = useRouter()

const email = ref()
const firstName = ref()
const lastName = ref()
const nickName = ref()
const age = ref()
const money = ref()
const salary = ref()
const store = useCounterStore()


const updateUserProfile = function () {
  const userId = '현재 사용자의 ID 또는 다른 방식으로 사용자 식별';
  axios({
   method: 'put',
   url: `${store.API_URL}/account/update-profile/`,
     data: {
      username: store.username,
      email: email.value, 
      first_name: firstName.value, 
      last_name: lastName.value, 
      nickname: nickName.value, 
      age: age.value, 
      money: money.value, 
      salary: salary.value, 
     },
     headers: {
       Authorization: `Token ${store.token}`
     }
  })
  .then((res) => {
       router.push({ name: 'MyPageView' })
     })
     .catch((err) => {
       console.log(err)
     })
};


</script>

<style scoped>
</style>