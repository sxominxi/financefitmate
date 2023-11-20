<template>
    <div>
        <h3 v-if="!isOn">마이페이지에 저장된 상품입니다.</h3>
        <h3>{{ store.detailDeposit.fin_prdt_nm }}</h3>
        <p>가입 대상: {{ store.detailDeposit.join_member }} </p>
        <p>가입 방법: {{ store.detailDeposit.join_way }}</p>
        <p>금융회사 명: {{ store.detailDeposit.kor_co_nm }}</p>
        <hr>
        <p>저축 기간 별 금리 정보</p>
        <hr>
        <div v-for="option in store.detailDeposit.option_set">
            <p>저축 기간: {{ option.save_trm }} 개월</p>
            <p>저축 금리 유형: {{ option.intr_rate_type_nm }}</p>
            <p>저축 금리: {{ option.intr_rate }}</p>
            <p>최고 우대 금리: {{ option.intr_rate2 }}</p>
            <button v-if="isOn" @click="addProduct(store.detailDeposit, option.save_trm)">추가 하기</button>
            <hr>
        </div>
    </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useServiceStore } from '../stores/modules/service'
import { ref, onMounted } from 'vue';
import axios from 'axios';

const store = useServiceStore()
const route = useRoute()
const deposit_id = ref(route.params.id)
const existingProduct = JSON.parse(localStorage.getItem('become_deposit')) || []
const isOn = ref(true)


onMounted(() => {
    store.getDetailDeposit(deposit_id.value)
})

const addProduct = (product, term) => {
    const isDuplicate = existingProduct.length > 0 && existingProduct.find((item) => item.id === product.id)
    if (!isDuplicate) {
        alert('현재 상품을 마이페이지에 추가합니다.')
        existingProduct.push([product, term])
        console.log(existingProduct)
        console.log(isOn.value)
    }
    localStorage.setItem('become_deposit', JSON.stringify(existingProduct))
    isOn.value = existingProduct.length > 0 && existingProduct.find((item) => item.id === product.id)
}

</script>

<style scoped>

</style>