<template>
    <div>
        <h1>Exchange</h1>
        <div class="exchange">
            <select name="cur_nm" v-model="country_info" @change="clear">
                <option v-for="country in store.exchange" :value="country">
                    {{ country.cur_nm }}
                </option>
            </select><br>
            <input type="number" id="kr_won" @input="exchange_won" ref="input1">구매하실 때: {{ result_won }}원 <br>
            <input type="number" id="another" @input="exchange_another" ref="input2">판매하실 때: {{ result_another }}{{ country_info.cur_unit }} <br>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useServiceStore } from '@/stores/service';
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

</style>