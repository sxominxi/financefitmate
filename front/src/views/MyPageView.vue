<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1>마이 페이지</h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
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
                        <div class="my-deposit">
                            <h2>내가 가입한 예금 상품</h2>
                            <button @click="goMydeposit">{{ depositlength }} 개</button>
                        </div>
                        <div class="my-installment">
                            <h2>내가 가입한 적금 상품</h2>
                            <button @click="goMyinstallment">{{ installmentlength }} 개</button>
                        </div>
                    </div>
                    <div class="recommend">
                        <div class="subtitle">
                            <h2>알고리즘 기반 맞춤 상품 추천</h2>
                        </div>
                        <!-- 캐루젤 시작 -->
                        <div id="carouselExampleCaptions" class="carousel slide">
                            <div class="carousel-indicators">
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Slide 4"></button>
                            </div>
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <div class="box1">
                                    </div>
                                    <div class="carousel-caption d-none d-md-block" @click="goDetailDeposit(DepositProduct[0].id)">
                                        <h5>{{DepositProduct[0]?.fin_prdt_nm}}</h5>
                                        <button type="button" class="btn btn-outline-secondary" disabled>누구나 가입</button>
                                        <button type="button" class="btn btn-outline-secondary" disabled>방문없이 가입</button>
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <div class="box2">
                                    </div>
                                    <div class="carousel-caption d-none d-md-block" @click="goDetailDeposit(DepositProduct[1].id)">
                                        <h5>{{ DepositProduct[1]?.fin_prdt_nm }}</h5>
                                        <button type="button" class="btn btn-outline-secondary" disabled>누구나 가입</button>
                                        <button type="button" class="btn btn-outline-secondary" disabled>방문없이 가입</button>
                                    </div>
                                </div>
                                <div class="carousel-item" @click="goDetailInstallment(InstallmentProduct[0].id)">
                                    <div class="box3">
                                    </div>
                                    <div class="carousel-caption d-none d-md-block" >
                                        <h5>{{ InstallmentProduct[0]?.fin_prdt_nm }}</h5>
                                        <button type="button" class="btn btn-outline-secondary" disabled>누구나 가입</button>
                                        <button type="button" class="btn btn-outline-secondary" disabled>방문없이 가입</button>
                                    </div>
                                </div>
                                <div class="carousel-item" @click="goDetailInstallment(InstallmentProduct[1].id)">
                                    <div class="box4">
                                    </div>
                                    <div class="carousel-caption d-none d-md-block">
                                        <h5>{{InstallmentProduct[1]?.fin_prdt_nm}}</h5>
                                        <button type="button" class="btn btn-outline-secondary" disabled>누구나 가입</button>
                                        <button type="button" class="btn btn-outline-secondary" disabled>방문없이 가입</button>
                                    </div>
                                </div>
                            </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                        <!-- 캐루젤 끝 -->
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
import { useServiceStore } from '../stores/modules/service';
import axios from 'axios';

const store2 = useServiceStore()
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

const goDetailDeposit = function(deposit_id) {
    router.push({
        name: 'DepositDetailView',
        params: { id: deposit_id}
    })
}

const goDetailInstallment = function(installment_id) {
    router.push({
        name: 'installmentDetailView',
        params: { id: installment_id }
    })
}  

const DepositProduct = ref([])
const recommendDepoist = function() {
    for (const item of store2.depositproducts) {
        for (const recommenditem of store.customProduct) {
            if ( item.fin_prdt_cd === recommenditem) {
                DepositProduct.value.push(item)
            }
        }
    }
}

console.log(DepositProduct.value)

const InstallmentProduct = ref([])
const recommendInstallment = function() {
    for (const item2 of store2.installmentproducts) {
        for (const recommenditem of store.customProduct) {
            if ( item2.fin_prdt_cd === recommenditem) {
                InstallmentProduct.value.push(item2)
            }
        }
    }
}


onMounted(() => {
    userDetail()
    getX()
    getX2()
    store.userFind()
    recommendDepoist()
    recommendInstallment()
})

</script>

<style scoped>
.box {
    display: flex;
    margin-top: 30px;
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

.carousel-inner {
    width: 100%;
    height: 100%; /* Make the carousel-inner fill the available height */
}
.carousel-item {
    width: 100%;
    height: 100%;
}

img {
    object-fit: cover; /* Maintain aspect ratio while covering the entire container */
    width: 100%; /* Make the image fill the container width */
    height: 100%; /* Make the image fill the container height */
}

.box1 {
    border: 1px solid blue;
    width: 100%;
    height: 100%
}
.box2 {
    border: 1px solid red;
    width: 100%;
    height: 100%
}
.box3 {
    border: 1px solid yellow;
    width: 100%;
    height: 100%
}
.box4 {
    border: 1px solid green;
    width: 100%;
    height: 100%
}
.carousel {
    margin-top: 20px;
    width: 90%;
    height: 60%;
}
.carousel h5 {
    color: black
}

.carousel-control-prev span{
    background-color: black;
}
.carousel-control-next span{
    background-color: black;
}

.carousel:hover {
    cursor: pointer;
}

.carousel-indicators button{
    background-color: black;
}

.my-products {
    display: flex;
    justify-content: space-between;
}
.my-products div {
    margin: 10px;
    border: 1px solid black;
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>