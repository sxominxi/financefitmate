import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useServiceStore = defineStore('service', () => {
    const API_URL = 'http://127.0.0.1:8000'

    const depositproducts = ref([])
    const exchange = ref([])
    const getExchanges = function() {
        axios({
            method: 'get',
            url: `${API_URL}/service/exchange/`,
        })
        .then((res) => {
            exchange.value = res.data
        })
    }
    const getDepositProducts = function() {
        axios({
            method: 'get',
            url: `${API_URL}/service/deposit-products/`
        })
        .then((res) => {
            console.log(res.data)
            depositproducts.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
    }

    return { getExchanges, exchange, getDepositProducts, depositproducts}
}, { persist: true })