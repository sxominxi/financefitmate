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
                    <img src="@/assets/profile.png" class="circular-image" alt="Your Image">
                    <h2><strong>{{ userDetailInfo.last_name }}</strong><strong>{{ userDetailInfo.first_name }}</strong> 님</h2>
                    <p>{{ userDetailInfo.nickname }}</p>
                    <p></p>
                    <p>나의 보유 자산 : {{ formatNumber(userDetailInfo.money) }}원</p>
                    <p>나의 연봉 정보 : {{ formatNumber(userDetailInfo.salary)  }}원</p>
                    <button @click="goToUpdateProfile" class="btn btn-success">회원정보 수정</button>
                </div>
                <div class="products-box">
                    <div class="my-products">
                        <div class="my-deposit">
                            <h2><strong>내가 추가한 예금 상품</strong></h2>
                            <button @click="goMydeposit">{{ depositlength }} 개</button>
                        </div>
                        <div class="my-installment">
                            <h2><strong>내가 추가한 적금 상품</strong></h2>
                            <button @click="goMyinstallment">{{ installmentlength }} 개</button>
                        </div>
                    </div>
                    <div class="recommend">
                        <div class="subtitle">
                            <h2><strong>알고리즘 기반 맞춤 상품 추천</strong></h2>
                        </div>
                        <!-- 캐루젤 시작 -->
                        <!-- <div id="carouselExampleCaptions" class="carousel slide">
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
                                        <div class="carousel-item">
                                            <img src="@/assets/c001.png" class="d-block w-100" alt="...">
                                        </div>
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
                        </div> -->
                        <!-- 캐루젤 끝 -->
                        <div id="carouselExampleDark" class="carousel carousel-dark slide">
                            <div class="carousel-indicators">
                                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
                                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
                                <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Slide 4"></button>
                            </div>
                            <div class="carousel-inner">
                                <div class="carousel-item active" data-bs-interval="10000">
                                <img src="@/assets/c001.png" class="d-block w-100" alt="...">
                                <div class="carousel-caption d-none d-md-block" @click="goDetailDeposit(DepositProduct[0].id)">
                                        <h5><strong>{{ DepositProduct[0]?.fin_prdt_nm }}</strong></h5>
                                        <div class="carousel-btn">
                                            <p># 누구나 가입</p>
                                            <p># 방문없이 가입</p>
                                        </div>
                                </div>
                                </div>
                                <div class="carousel-item" data-bs-interval="2000">
                                    <img src="@/assets/c002.png" class="d-block w-100" alt="...">
                                    <div class="carousel-caption d-none d-md-block" @click="goDetailDeposit(DepositProduct[1].id)">
                                        <h5><strong>{{ DepositProduct[1]?.fin_prdt_nm }}</strong></h5>
                                        <div class="carousel-btn">
                                            <p># 누구나 가입</p>
                                            <p># 방문없이 가입</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="carousel-item" @click="goDetailInstallment(InstallmentProduct[0].id)">
                                    <img src="@/assets/c003.png" class="d-block w-100" alt="...">
                                    <div class="box3">
                                    </div>
                                    <div class="carousel-caption d-none d-md-block" >
                                        <h5><strong>{{ InstallmentProduct[0]?.fin_prdt_nm }}</strong></h5>
                                        <div class="carousel-btn1">
                                            <p># 누구나 가입</p>
                                            <p># 방문없이 가입</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="carousel-item" @click="goDetailInstallment(InstallmentProduct[1].id)">
                                    <img src="@/assets/c004.png" class="d-block w-100" alt="...">
                                    <div class="box3">
                                    </div>
                                    <div class="carousel-caption d-none d-md-block" >
                                        <h5><strong>{{ InstallmentProduct[1]?.fin_prdt_nm }}</strong></h5>
                                        <div class="carousel-btn1">
                                            <p># 누구나 가입</p>
                                            <p># 방문없이 가입</p>
                                        </div>
                                    </div>
                                </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                            </button>
                            </div>
                        </div>
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
    margin-top: 50px;
}

.btn:hover {
    transform: translateY(-10px); /* 호버 시 카드 약간 위로 이동 */
  box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2); /* 호버 시 그림자 크게 */
  /* 추가적인 호버 효과 스타일링 */
}

.my-info {
    width: 40%;
    border-radius: 15px;
    height: 500px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.my-info button {
    margin: 30px 0 ;
    width: 60%;
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2);
}

.my-info h2 {
    margin: 25px;
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
    margin-top: 50px;
    font-size: 25px;
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
    border-radius: 20px;
}

.box1 {
    /* border: 1px solid blue; */
    width: 100%;
    height: 100%
}
.box2 {
    /* border: 1px solid red; */
    width: 100%;
    height: 100%
}
.box3 {
    /* border: 1px solid yellow; */
    width: 100%;
    height: 100%
}
.box4 {
    /* border: 1px solid green; */
    width: 100%;
    height: 100%
}
.carousel {
    margin-top: 20px;
    width: 90%;
    height: 60%;
    border-radius: 20px;
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2);
}

.carousel-caption {
    margin-bottom: 20px;
}

.carousel-btn {
    width: 40%;
    margin-top: 30px;
    text-align: left;
    color: black
}

.carousel-btn1 {
    width: 100%;
    margin-top: 30px;
    text-align: right;
    color: black
}

.carousel h5 {
    color: black
}

/* .carousel-control-prev span{
    background-color: black;
}
.carousel-control-next span{
    background-color: black;
}

.carousel:hover {
    cursor: pointer;
} */

.carousel-indicators button{
    background-color: black;
}

.my-products {
    display: flex;
    justify-content: space-between;
    width: 95%;
}
.my-products div {
    margin: 10px;
    border: 1px solid #ddd;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 85%;
}

.my-deposit > h2 {
    font-size: 17px;
    padding: 10px;
}
.my-installment > h2 {
    font-size: 17px;
    padding: 10px;
}

.my-deposit > button {
    border: none;
    background-color: inherit;
    font-size: 17px;
}
.my-installment > button {
    border: none;
    background-color: inherit;
    font-size: 17px;
}

.my-deposit,
.my-installment
{
    width: 50%; /* 카드 너비 조정 */
    height: 150px;
    border-radius: 20px;
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2);
    padding: 10px;
    box-sizing: border-box;
    position: relative;
}

.my-deposit:hover{
    transform: translateY(-10px); /* 호버 시 카드 약간 위로 이동 */
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2); /* 호버 시 그림자 크게 */
}
.my-installment:hover{
    transform: translateY(-10px); /* 호버 시 카드 약간 위로 이동 */
    box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.2); /* 호버 시 그림자 크게 */
}

.circular-image {
    padding: 10px;
    width: 200px; /* 이미지의 가로 크기를 지정합니다. */
    height: 200px; /* 이미지의 세로 크기를 지정합니다. */
    object-fit: cover; /* 이미지가 잘리지 않고 비율을 유지하도록 설정합니다. */
    border-radius: 50%; /* 50%로 설정하여 이미지를 원형으로 만듦 */
    /* 필요에 따라 추가적인 스타일링을 적용할 수 있음 */
}
</style>