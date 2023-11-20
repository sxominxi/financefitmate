<template>
    <div>
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
            <hr>
        </div>
    </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useServiceStore } from '../stores/service'
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';

const store = useServiceStore()
const route = useRoute()
const installment_id = ref(route.params.id)

onMounted(() => {
    store.getDetailInstallment(installment_id.value)
})
</script>

<style scoped>

</style>