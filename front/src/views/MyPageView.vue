<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <h1>마이 페이지</h1>
            <div class="box">
                <div class="my-info card border-light mb-3">
                    <h2><strong>{{ userDetailInfo.first_name }}</strong> 님</h2>
                    <p>{{ userDetailInfo.nickname }}</p>
                    <p>나의 보유 자산: {{ formatNumber(userDetailInfo.money) }}원</p>
                    <p>나의 연봉 정보: {{ formatNumber(userDetailInfo.salary)  }}원</p>
                    <button @click="goToUpdateProfile" class="btn btn-outline-success">회원정보 수정</button>
                </div>
                <div class="products-box">
                    <div class="my-products">
                       <h2>내가 가입한 예금 상품</h2>
                       <button @click="goMydeposit">{{ depositlength }} 개</button>
                       <h2>내가 가입한 적금 상품</h2>
                       <button @click="goMyinstallment">{{ installmentlength }} 개</button>
                    </div>
                    <div class="recommend">
                        <div class="subtitle">
                            <h2>맞춤 상품 추천</h2>
                        </div>
                        <Carousel />
                        <RouterView/>
                    </div>
                </div>
            </div>

         </div>
      </div>
   </div>
</template>



<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import { useCounterStore } from '../stores/modules/counter';
import axios from 'axios';
import { RouterView } from 'vue-router'
import Carousel from '@/components/Carousel.vue';

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

const userDetailInfo = ref([])
const userDetail = function() {
    axios({
            method: 'get',
            url: `${store.API_URL}/account/user-info/${store.userInfo.pk}`,
            headers: {Authorization: `Token ${store.token}`}
        })
        .then((res) => {
            userDetailInfo.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
}

const formatNumber = (number) => {
    if (number === null || number === undefined) {
        return 
    }

    const parts = number.toString().split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return parts.join('.');
};


onMounted(() => {
    getX(),
    getX2(),
    store.userFind(),
    userDetail()
})

</script>

<style scoped>
.box {
    display: flex;
}

.my-info {
    width: 40%;
    padding: 10px;
    border-radius: 15px;
    height: 500px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.my-info button {
    margin: 30px 0 ;
    width: 60%;
}

.my-info h2 {
    margin: 10px 0;
}
.products-box {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.recommend {
    width: 100%;
    height: 100%;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.recommend h2{
    margin-top: 20px;
}

</style>