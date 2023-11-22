<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">

            <h1>마이 페이지</h1>
            <h2>{{ store.userInfo.first_name }}님 반갑습니다.</h2>

            <!-- 회원 정보 수정 페이지로 이동하는 버튼 -->
            <button @click="goToUpdateProfile">회원정보 수정</button>

            <h2>내가 가입한 예금 상품</h2>
           <button @click="goMydeposit">{{ depositlength }} 개</button>

           <h2>내가 가입한 적금 상품</h2>
           <button @click="goMyinstallment">{{ installmentlength }} 개</button>
         </div>
      </div>
   </div>
</template>



<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import { useCounterStore } from '../stores/modules/counter';

const store = useCounterStore()
const router = useRouter()

const deposits = ref([])
deposits.value = JSON.parse(localStorage.getItem('become_deposit')) || []

const installments = ref([])
installments.value = JSON.parse(localStorage.getItem('become_installment')) || []

const depositlength = ref(0)
const installmentlength = ref(0)

const getX = function() {
    for (const x_nm of deposits.value) {
        if (x_nm[2].pk == store.userInfo.pk) {
            depositlength.value += 1
        }
    }
}

const getX2 = function() {
    for (const x2_nm of installments.value) {
        if (x2_nm[2].pk == store.userInfo.pk) {
            installmentlength.value += 1
        }
    }
}

const goToUpdateProfile = () => {
  router.push({ name: 'UpdateUserView' }); 
};

const goMydeposit = function() {
    router.push({
        name: 'MydepositView',
    })
}

const goMyinstallment = function() {
    router.push({
        name: 'MyinstallmentView',
    })
}

onMounted(() => {
    getX(),
    getX2(),
    store.userFind()
})

</script>

<style scoped>

</style>