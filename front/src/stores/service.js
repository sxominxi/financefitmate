import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useServiceStore = defineStore('service', () => {
    const exchange = ref([])
    const getExchanges = function() {
        axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/service/exchange/',
        })
        .then((res) => {
            exchange.value = res.data
            console.log(res.data)
        })
    }
    return { getExchanges, exchange }
}, { persist: true })