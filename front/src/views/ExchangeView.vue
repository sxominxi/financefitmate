<template>
   <div id="wrap">
      <div class="check">
         <div class="inner">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1 class="fs-3 fw-bold"><strong>환율 계산기</strong></h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
            <div class="exchange">
                <div class="uri-country">
                    <select class="form-select" aria-label="Disabled select example" disabled>
                        <option selected value="한국 원">한국 원
                        </option>
                    </select>
                    <input class="uri-input border border-start-0" type="number" id="kr_won" @input="exchange_won" v-model="result_won"><br>
                    <strong class="fs-4">원</strong>
                </div>
                <div class="another-country">
                    <select name="cur_nm" v-model="country_info" @change="clear" class="form-select" aria-label="Default select example">
                       <option :value=[]>나라를 선택하세요.</option>
                       <option v-for="country in store.exchange" :value="country">
                          {{ country.cur_nm }}
                       </option>
                    </select><br>
                    <input class="another-input border border-start-0" type="number" id="another" @input="exchange_another" v-model="result_another"><br>
                    <strong class="fs-4">{{ country_info.cur_unit }}</strong>
                </div>
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

onMounted(() => {
    store.getExchanges()
})

const clear = function(){
    result_won.value = null
    result_another.value = null
}

const exchange_won = function (event)  {
    result_won.value =  event.target.value
    result_another.value =  event.target.value / country_info.value.ttb.replace(',','')
}

const exchange_another = function (event)  {
    result_another.value = event.target.value
    if (country_info.value['cur_nm'] === '일본 옌' || country_info.value['cur_nm'] === '인도네시아 루피아') {
        result_won.value =  event.target.value * country_info.value.tts.replace(',','') / 100
    } else {
        result_won.value =  event.target.value * country_info.value.tts.replace(',','')
    }
}

</script>

<style scoped>
.another-country{
    display: flex;
    margin-top: 20px;
}

.another-country select {
    width: 20%;
}

.uri-country {
    display: flex;
    margin-top: 20px;
}

.uri-country strong{
    margin-bottom: 5px;
    margin-left: 5px;
}
.uri-country select {
    width: 20%;
}

.another-country strong{
    margin-bottom: 5px;
    margin-left: 5px;
}

.exchange {
    display: flex;
    flex-direction: column;
    margin-top: 50px;
}

.uri-input, .another-input {
    width: 500px;
}

</style>