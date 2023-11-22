<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
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
const deposit_id = ref(route.params.id)
const existingProduct = JSON.parse(localStorage.getItem('become_deposit')) || []
const isOn = ref(true)


onMounted(() => {
    store.getDetailDeposit(deposit_id.value)
    store2.userFind()
})

const addProduct = (product, term) => {
    const isDuplicate = existingProduct.length > 0 && existingProduct.find((item) => item.id === product.id)
    if (!isDuplicate) {
        alert('현재 상품을 마이페이지에 추가합니다.')
        existingProduct.push([product, term, store2.userInfo])
    }
    localStorage.setItem('become_deposit', JSON.stringify(existingProduct))
    isOn.value = existingProduct.length > 0 && existingProduct.find((item) => item.id === product.id && store2.userInfo.pk === existingProduct[2].pk)
}

</script>

<style scoped>
#wrap {
  display: flex;
  justify-content: center;
  background-color: #f0f0f0;
  padding: 0px 50px; /* 기본값은 50px */
}

/* 페이지 내 컨텐츠를 감싸는 컨테이너 */

.check {
  background-color: #fff;
  padding: 20px 0;
  width: 100%;
  position: relative;
  overflow: hidden; /* 부모 요소의 내용이 넘칠 때 숨김 처리 */
}

/* 미디어 쿼리를 이용한 반응형 조정 */
@media screen and (max-width: 600px) {
  /* 현재 창 크기가 600px 이하인 경우 */
#wrap {
   padding: 0 10px; /* 좁은 화면에서는 양 옆 공백을 줄입니다. */
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