<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
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
 #wrap {
  display: flex;
  justify-content: center;
  padding: 0px 100px; /* 기본값은 50px */
}

/* 페이지 내 컨텐츠를 감싸는 컨테이너 */

.check {
  background-color: #fff;
  padding: 20px 0;
  width: 80%;
  position: relative;
  overflow: hidden; /* 부모 요소의 내용이 넘칠 때 숨김 처리 */
}

/* 미디어 쿼리를 이용한 반응형 조정 */
@media screen and (max-width: 1000px) {
  /* 현재 창 크기가 600px 이하인 경우 */
#wrap {
   padding: 0; /* 좁은 화면에서는 양 옆 공백을 줄입니다. */
   }
   .check{
   width: 100%;
   }
.deposit {
   padding: 20px 0; /* 상하 여백은 필요에 따라 조절하세요 */
  }
}

.inner {
   border: 1px solid #ddd;
   border-radius: 8px;
   padding: 20px;
   background-color: #fff;
}

</style>