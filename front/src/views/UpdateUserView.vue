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
               <div class="form-box">
                  <label class="id">아이디: {{ store.username }}</label><br>
                  <div class="form-input">
                     <div class="form-label">
                        <label>이메일:</label>
                     </div>
                     <input class="form-control" type="email" v-model="email"><br>
                  </div>
                  <div class="form-input">
                     <div class="form-label">
                        <label>이름:</label>
                     </div>
                     <input class="form-control" type="text" v-model="firstName"><br>
                  </div>
                  <div class="form-input">
                     <div class="form-label">
                        <label>성:</label>
                     </div>
                     <input class="form-control" type="text" v-model="lastName"><br>
                  </div>
                  <div class="form-input">
                     <div class="form-label">
                        <label>닉네임:</label>
                     </div>
                     <input class="form-control" type="text" v-model="nickName"><br>
                  </div>
                  <div class="form-input">
                     <div class="form-label">
                        <label>나이:</label>
                     </div>
                     <input class="form-control" type="number" v-model="age"><br>
                  </div>
                  <div class="form-input">
                     <div class="form-label">
                        <label>현재 보유 자산:</label>
                     </div>
                     <input class="form-control" type="number" v-model="money"> <p class="input-p">원</p><br>
                  </div>
                  <div class="form-input">
                     <div class="form-label">
                        <label>연봉:</label>
                     </div>
                     <input class="form-control" type="number" v-model="salary"> <p class="input-p">원</p><br>
                  </div>
                  
                  <button class="input-btn btn btn-success">정보 업데이트</button>
               </div>

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
.form-box {
   margin-top: 40px;
}

.form-box input {
   width: 60%;
}

.form-input {
   display: flex;
}

.form-label {
   width: 120px;
}

.form-control {
   margin-top: 0px;
   margin-bottom: 20px;
}

.id {
   margin-bottom: 20px;
}

.input-p {
   margin-top: 5px;
   margin-left: 10px;
}

.input-btn {
   margin-top: 20px;
}
</style>