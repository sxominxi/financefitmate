<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">

            <h1>사용자 정보 수정</h1>
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
      console.log(nickName.value)
      console.log(res.data)
       router.push({ name: 'MyPageView' })
     })
     .catch((err) => {
       console.log(err)
     })
};


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