<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">

            <h1>정기 적금</h1>
         </div>
         <select class="bank" v-model="bank">
            <option :value=null>은행을 선택하세요.</option>
            <option v-for="bank_select in bank_list" :value="bank_select">{{ bank_select }}</option>
         </select>

         <select class="duration" v-model="duration">
            <option :value=null selected>기간을 선택하세요.</option>
            <option v-for="duration_select in duration_list" :value="duration_select">{{ duration_select }}</option>
         </select>

         <button @click="installment_list">검색</button>
         <div v-for="product in find_installment" :key="product.id" @click="goDetail(product.id)">
            <p>금융 회사: {{ product.kor_co_nm }}</p>
            <p>금융 상품명: {{ product.fin_prdt_nm }}</p>
            <div v-for="product_info in product.option_set" :key="product_info.id">
                  <div v-if="product_info.save_trm == duration">
                     <p>저축 기간: {{ product_info.save_trm }} 개월</p>
                     <p>저축 방식: {{ product_info.rsrv_type_nm }}</p>
                     <p>이자 계산 방식: {{ product_info.intr_rate_type_nm }}</p>
                     <p>최고 우대 금리: {{ product_info.intr_rate2 }}</p>
                     <button @click="goDetail(product.id)">자세히 보기</button>
                     <hr>
                  </div>
            </div>
            <hr>
         </div>
      </div>
   </div>
</template>

<script setup>
import { useServiceStore } from '@/stores/modules/service'
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter()
const store = useServiceStore()
const bank = ref(null)
const duration = ref(null)
const find_installment = ref([])

const bank_list = ref(['우리은행', '한국스탠다드차타드은행', '대구은행', '부산은행', '광주은행', '부산은행', '제주은행', '제주은행', '전북은행', '경남은행', '한국산업은행', '국민은행', '신한은행', '농협은행주식회사', '하나은행', '주식회사 케이뱅크', '주식회사 카카오뱅크', '토스뱅크 주식회사'])
const duration_list = ref([6, 12, 24, 36])

onMounted(() => {
    store.getInstallmentProducts()
})

const installment_list = function() {
    find_installment.value = []

    for (const find_bank of store.installmentproducts) {
        if ( find_bank.kor_co_nm === bank.value) {
            for (const find_term of find_bank.option_set) {
                if ( find_term.save_trm == duration.value ) {
                    find_installment.value.push(find_bank)
                }
            }
        }
    }
}

const goDetail = function(installment_id) {
    router.push({
        name: 'installmentDetailView',
        params: { id: installment_id }
    })
}   

</script>

<style scoped>

</style>