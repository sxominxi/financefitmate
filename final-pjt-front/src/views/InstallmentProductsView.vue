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
                     <h1 class="fs-3 fw-bold"><strong>정기 적금</strong></h1>
                  </div>
               </div>
            </div>
         </div>
         <div class="select-list">
            <select class="bank form-select" v-model="bank" aria-label="Default select example">
                <option :value=null>은행을 선택하세요.</option>
                <option v-for="bank_select in bank_list" :value="bank_select">{{ bank_select }}</option>
            </select>

            <select class="duration form-select" v-model="duration" aria-label="Default select example">
                <option :value=null selected>기간을 선택하세요.</option>
                <option v-for="duration_select in duration_list" :value="duration_select">{{ duration_select }}</option>
            </select>

         <button @click="installment_list" type="button" class="btn btn-success">검색</button>
         </div>

         <div class="card-list" v-if="isInstallment">
            <div class="card border-success mb-3 col-12" v-for="product in find_installment" :key="product.fin_prdt_cd" @click="goDetail(product.id)">
               <div class="card-header">{{ product?.kor_co_nm }}</div>
               <div v-for="product_info in product?.option_set" :key="product_info.id">
                  <div v-if="product_info.save_trm == duration">
                        <div class="card-body" >
                            <h5 class="card-title fs-3 fw-bold text-success">{{ product?.fin_prdt_nm }}</h5>
                            <div class="card-function">
                                <div class="card-main">
                                    <div class="card-info">
                                        <p class="card-text">저축 기간: {{ product_info.save_trm }} 개월</p>
                                        <p class="card-text">이자 계산 방식: {{ product_info.intr_rate_type_nm }}</p>
                                        <p class="card-text text-danger">적립 유형명: {{ product_info.rsrv_type_nm }}</p>
                                    </div>
                                </div>
                                <div class="intr">
                                    <p class="card-text text-danger">최고 우대 금리: {{ product_info.intr_rate2 }}</p>
                                    <p class="card-text">기본 금리: {{ product_info.intr_rate }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
               </div>
            </div>
         </div>
         <div v-if="!isInstallment">
            <h2 class="not">조회 가능한 상품이 없습니다.</h2>
        </div>
      </div>
   </div>
</template>

<script setup>
import { useServiceStore } from '@/stores/modules/service'
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useServiceStore()
const bank = ref(null)
const duration = ref(null)
const find_installment = ref([])
const isInstallment = ref(false)

const bank_list = ref(['우리은행', '한국스탠다드차타드은행', '대구은행', '부산은행', '광주은행', '부산은행', '제주은행', '제주은행', '전북은행', '경남은행', '한국산업은행', '국민은행', '신한은행', '농협은행주식회사', '하나은행', '주식회사 케이뱅크', '주식회사 카카오뱅크', '토스뱅크 주식회사'])
const duration_list = ref([6, 12, 24, 36])

onMounted(() => {
    store.getInstallmentProducts()
})

const installment_list = function() {
    find_installment.value = []
    isInstallment.value = false
    const filteredProducts = []

    for (const find_bank of store.installmentproducts) {
        if ( find_bank.kor_co_nm === bank.value) {
            for (const find_term of find_bank.option_set) {
                if ( find_term.save_trm == duration.value ) {
                    filteredProducts.push(find_bank)
                }
            }
        }
    } 

    find_installment.value = [...filteredProducts]
    isInstallment.value = find_installment.value.length > 0
}

const goDetail = function(installment_id) {
    router.push({
        name: 'installmentDetailView',
        params: { id: installment_id }
    })
}   

</script>

<style scoped>
.select-list {
   display: flex;
   flex-direction: row;
   justify-content: left;
   align-items: center;
   padding-left: 20px;
   padding-right: 20px;
 }

 .select-list select {
   width: 200px;
   height: 50px;
   margin: 30px 10px;
 }

 .select-list > button {
   width: 80px;
   height: 48px; 
   margin: 30px 10px;
 }

 .card {
    width: 99%;
 }
 .card-list{
    display: flex;
    flex-direction: column;
    align-items: left;
    padding-right: 20px;
    padding-left: 30px;
 }

 .not {
   padding-inline-start: 30px;
 }

 .card-main {
    display: flex;
    justify-content: space-between;
 }

 .card-text {
    margin: 0 0;
 }
 .intr {
    display: flex;
    flex-direction: column;
    align-items: end;
 }

 .card-function {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
 }
 
 .card:hover {
    cursor: pointer;
}
</style>