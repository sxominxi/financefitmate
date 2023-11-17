<template>
    <div>
        <h1>Exchange</h1>
        <div class="exchange">
            <select name="cur_nm" v-model="country_info">
                <option v-for="country in store.exchange" :value="country">
                    {{ country.cur_nm }}
                </option>
            </select><br>
            <input type="number" id="kr_won" @input="exchange_won">{{ result_won }} 원 <br>
            <input type="number" id="another" @input="exchange_another">{{ result_another }} {{ country_info.cur_unit }} <br>
            <input type="submit">
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useServiceStore } from '@/stores/service';
import axios from 'axios'

const store = useServiceStore()
const country_info = ref([])
const result_won = ref(1)
const result_another = ref(1)

onMounted(() => {
    store.getExchanges()
})

const exchange_won = function (event)  {
    result_won.value =  event.target.value
    result_another.value =  event.target.value / country_info.value.tts
    console.log(country_info.value.cur_nm)
}

const exchange_another = function (event)  {
    result_another.value = event.target.value
    result_won.value =  event.target.value * country_info.value.ttb
    console.log(country_info.value.cur_nm)
}


</script>

<style scoped>

</style>