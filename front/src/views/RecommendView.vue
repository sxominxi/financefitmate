<template>
    <div>
        <h1>상품 추천 리스트</h1>
        <h2>예금 상품 추천</h2>
        <div v-for="product in store2.depositproducts">
            <div v-for="recommends in store.customProduct">
                <div v-if="product.fin_prdt_cd == recommends">
                    {{ product.fin_prdt_nm }}
                    <p>금융회사명: {{ product.kor_co_nm }}</p>
                    <button @click="goDetailDeposit(product.id)">상세 페이지</button>
                    <hr>
                </div>
            </div>
        </div>

        <h2>적금 상품 추천</h2>
        <div v-for="product in store2.installmentproducts">
            <div v-for="recommends in store.customProduct">
                <div v-if="product.fin_prdt_cd == recommends">
                    {{ product.fin_prdt_nm }}
                    <p>금융회사명: {{ product.kor_co_nm }}</p>
                    <button @click="goDetailInstallment(product.id)">상세 페이지</button>
                    <hr>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '../stores/modules/counter';
import { useServiceStore } from '@/stores/modules/service';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useCounterStore()
const store2 = useServiceStore()
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


onMounted(() => {
    store.recommendProducts()
    store.userFind()
    store2.getDepositProducts()
    store2.getInstallmentProducts()
})
</script>

<style scoped>

</style>