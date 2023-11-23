<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1>적금 상세 보기</h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>

            <h3 v-if="!isOn">마이페이지에 저장된 상품입니다.</h3>
            <h3>{{ store.detailInstallment.fin_prdt_nm }}</h3>
            <p>가입 대상: {{ store.detailInstallment.join_member }} </p>
            <p>가입 방법: {{ store.detailInstallment.join_way }}</p>
            <p>금융회사 명: {{ store.detailInstallment.kor_co_nm }}</p>
            <hr>
            <p>저축 기간 별 금리 정보</p>
            <hr>
            <div v-for="option in store.detailInstallment.option_set">
                  <p>저축 기간: {{ option.save_trm }} 개월</p>
                  <p>저축 금리 유형: {{ option.intr_rate_type_nm }}</p>
                  <p>적립 유형명: {{ option.rsrv_type_nm }}</p>
                  <p>저축 금리: {{ option.intr_rate }}</p>
                  <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
                  <button v-if="isOn" @click="addProduct(store.detailInstallment, option.save_trm)">추가 하기</button>
                  <hr>
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
</style>