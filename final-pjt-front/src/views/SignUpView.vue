<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1><strong>회원가입</strong></h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
            
            <form @submit.prevent="signUp">
               <div class="form-box">
                  <div class="form-input">
                     <label class="form-label" for="id">아이디:</label>
                     <input class="form-control" id="id" type="text" v-model.trim="username"><p class="input-p text-danger">(필수)</p><br>
                  </div>
                  <div class="form-input">
                     <label class="form-label" for="password1">패스워드:</label>
                     <input class="form-control" id="password1" type="password" v-model.trim="password1"><p class="input-p text-danger">(필수)</p><br>
                  </div>
                  <div class="form-input">
                     <label class="form-label" for="password2">패스워드확인:</label>
                     <input class="form-control" type="password" id="password2" v-model.trim="password2"><p class="input-p text-danger">(필수)</p><br>
                  </div>
                  
                  <div class="form-input">
                     <label class="form-label" for="email">이메일:</label>
                     <input class="form-control" type="email" id="email" v-model.trim="email"><p class="input-p text-danger"></p><br>
                  </div>
                  <div class="form-input">
                     <label class="form-label" for="firstname">이름:</label>
                     <input class="form-control" type="text" id="firstname" v-model.trim="first_name"><p class="input-p text-danger"></p><br>
                  </div>
                  <div class="form-input">
                     <label class="form-label" for="lastname">성:</label>
                     <input class="form-control" type="text" id="lastname" v-model.trim="last_name"><p class="input-p text-danger"></p><br>
                  </div>
                  <div class="form-input">
                     <label class="form-label" for="nickname">닉네임:</label>
                     <input class="form-control" type="text" id="nickname" v-model.trim="nickname"><p class="input-p text-danger"></p><br>
                  </div>
                  <div class="form-input">
                     <label class="form-label" for="age">나이:</label>
                     <input class="form-control" type="number" id="age" v-model.trim="age"><p class="input-p text-danger">(필수)</p><br>
                  </div>
                  <div class="form-input">
                     <label class="form-label" for="money">현재 보유 자산:</label>
                     <input class="form-control" type="number" id="money" v-model.trim="money"> <p class="input-p">원 </p><p class="input-p text-danger">(필수)</p><br>
                  </div>
                  <div class="form-input">
                     <label class="form-label" for="salary">연봉:</label>
                     <input class="form-control" type="number" id="salary" v-model.trim="salary"> <p class="input-p">원</p><p class="input-p text-danger">(필수)</p><br>
                  </div>
                  <button type="submit" class="input-btn btn btn-success">회원 가입</button>
            </div>
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
