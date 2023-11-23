<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1>금융 상품 추천</h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
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
    store.recommendProducts()
    store.userFind()
    store2.getDepositProducts()
    store2.getInstallmentProducts()
    recommendDepoist()
    recommendInstallment()
})


</script>

<style scoped>

</style>