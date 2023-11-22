<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">

            <h1>Exchange</h1>
            <div class="exchange">
                  <select name="cur_nm" v-model="country_info" @change="clear">
                     <option :value=[]>나라를 선택하세요.</option>
                     <option v-for="country in store.exchange" :value="country">
                        {{ country.cur_nm }}
                     </option>
                  </select><br>
                  <input type="number" id="kr_won" @input="exchange_won" ref="input1">구매하실 때: {{ result_won }}원 <br>
                  <input type="number" id="another" @input="exchange_another" ref="input2">판매하실 때: {{ result_another }}{{ country_info.cur_unit }} <br>
            </div>
         </div>
      </div>
   </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useServiceStore } from '@/stores/modules/service';
import axios from 'axios'

const store = useServiceStore()
const country_info = ref([])
const result_won = ref(null)
const result_another = ref(null)
const input1 = ref(null)
const input2 = ref(null)

onMounted(() => {
    store.getExchanges()
})

const clear = function(){
    input1.value.value = ''
    input2.value.value = ''
    result_won.value = null
    result_another.value = null
}

const exchange_won = function (event)  {
    result_won.value =  event.target.value
    result_another.value =  event.target.value / country_info.value.tts.replace(',','')
}

const exchange_another = function (event)  {
    result_another.value = event.target.value
    if (country_info.value['cur_nm'] === '일본 옌' || country_info.value['cur_nm'] === '인도네시아 루피아') {
        result_won.value =  event.target.value * country_info.value.ttb.replace(',','') / 100
    } else {
        result_won.value =  event.target.value * country_info.value.ttb.replace(',','')
    }
}

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