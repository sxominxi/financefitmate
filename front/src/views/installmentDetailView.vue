<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success">
                  </div>
               </div>
               <div class="title">
                  
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1 class="fs-3 fw-bold"><strong>적금 상세 보기</strong></h1>
                  </div>
               </div>
            </div>

            <h3 class="togle-ment" v-if="!isOn"><strong>마이페이지에 저장된 상품입니다.</strong></h3>
            <h3 class="product-name"><strong>{{ store.detailInstallment.fin_prdt_nm }}</strong></h3>
            <div class="info-main">
               <p class="fs-6">가입 대상: {{ store.detailInstallment.join_member }} </p>
               <p class="fs-6">가입 방법: {{ store.detailInstallment.join_way }}</p>
               <p class="fs-6">금융회사명: {{ store.detailInstallment.kor_co_nm }}</p>
               <p class="fs-6">가입 방법: {{ store.detailInstallment.join_way }}</p>
               <p class="fs-6">특이사항: {{ store.detailInstallment.spcl_cnd }}</p>
               <hr>
               <p class="fs-6">저축 기간 별 금리 정보</p>
               <hr>
            </div>
            <div class="card-list">
               <div v-for="option in store.detailInstallment.option_set">
                  <div class="card border-success">
                     <p class="card-header fs-3 fw-bold text-success">저축 기간: {{ option.save_trm }} 개월</p>
                     <p class="card-text">저축 금리 유형: {{ option.intr_rate_type_nm }}</p>
                     <p class="card-text">저축 금리: {{ option.intr_rate }}</p>
                     <p class="card-text text-danger">최고 우대 금리: {{ option.intr_rate2 }}</p>
                     <p class="card-text text-danger">적립 유형명: {{ option.rsrv_type_nm }}</p>
                     <button class="card-button btn btn-success" v-if="isOn" @click="addProduct(store.detailInstallment, option.save_trm)">추가 하기</button>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useServiceStore } from '../stores/modules/service'
import { useCounterStore } from '../stores/modules/counter'
import { ref, onMounted } from 'vue';


const store = useServiceStore()
const store2 = useCounterStore()
const route = useRoute()
const installment_id = ref(route.params.id)
const existingProduct = JSON.parse(localStorage.getItem('become_installment')) || []
const isOn = ref(true)

onMounted(() => {
    store.getDetailInstallment(installment_id.value)
})

const addProduct = (product, term) => {
    const isDuplicate = existingProduct.length > 0 && existingProduct.find((item) => item.id === product.id)
    if (!isDuplicate) {
        alert('현재 상품을 마이페이지에 추가합니다.')
        existingProduct.push([product, term, store2.userInfo])
    }
    localStorage.setItem('become_installment', JSON.stringify(existingProduct))
    isOn.value = existingProduct.length > 0 && existingProduct.find((item) => item.id === product.id  && store2.userInfo.pk === existingProduct[2].pk)
}
</script>

<style scoped>
.card-button {
   width: 100px;
   margin-bottom: 5px;
}

.card {
   display: flex;
   flex-direction: column;
   align-items: center;
   width: 280px;
   margin: 30px 35px;
   
}
.product-name{
   margin-top: 30px;
}
.card-header {
   width: 100%;
}

.card-list {
   display: flex;
   flex-wrap: wrap;
   justify-content: center;
}

hr {
  color: green; 
}

.info-main {
   margin: 40px 0;
}

.togle-ment {
   margin-top: 30px;
}
</style>