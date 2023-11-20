<template>
    <div>
        <h1>마이 페이지</h1>
        <h2>가입한 정기 예금 상품</h2>
        <div v-if="deposits.length > 0">
            <div v-for="product in deposits">
                <h4>가입 상품: {{ product[0].fin_prdt_nm }}</h4>
                <p>금융회사 명: {{ product[0].kor_co_nm }}</p>
                <div v-for="option in product[0].option_set">
                    <div v-if="option.save_trm === product[1]">
                        <p>기간: {{ option.save_trm }} 개월</p>
                        <p>저축 금리 유형: {{ option.intr_rate_type_nm }}</p>
                        <p>저축 금리: {{ option.intr_rate }}</p>
                        <p>최대 우대 금리: {{ option.intr_rate2 }}</p>
                    </div>
                </div>
                <hr>
            </div>
        </div>
        <div v-else>
            <strong>가입한 정기 예금 상품이 없습니다.</strong>
        </div>
        <hr>
        <h2>가입한 정기 적금 상품</h2>
        <div v-if="installments.length > 0">
            <div v-for="product in installments">
                <h4>가입 상품: {{ product[0].fin_prdt_nm }}</h4>
                <p>금융회사 명: {{ product[0].kor_co_nm }}</p>
                <div v-for="option in product[0].option_set">
                    <div v-if="option.save_trm === product[1]">
                        <p>기간: {{ option.save_trm }} 개월</p>
                        <p>저축 금리 유형: {{ option.intr_rate_type_nm }}</p>
                        <p>저축 금리: {{ option.intr_rate }}</p>
                        <p>최대 우대 금리: {{ option.intr_rate2 }}</p>
                    </div>
                </div>
                <hr>
            </div>
        </div>
        <div v-else>
            <strong>가입한 정기 적금 상품이 없습니다.</strong>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { useServiceStore } from '../stores/service';

const store = useServiceStore()

const deposits = ref([])
deposits.value = JSON.parse(localStorage.getItem('become_deposit')) || []


const installments = ref([])
installments.value = JSON.parse(localStorage.getItem('become_installment')) || []


</script>

<style scoped>

</style>