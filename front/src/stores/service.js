import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useServiceStore = defineStore('service', () => {
    const API_URL = 'http://127.0.0.1:8000'

    const depositproducts = ref([])
    const installmentproducts = ref([])
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
            depositproducts.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
    }
    const getInstallmentProducts = function() {
        axios({
            method: 'get',
            url: `${API_URL}/service/installment-savings-products/`
        })
        .then((res) => {
            installmentproducts.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
    }

    const detailInstallment = ref([])
    const getDetailInstallment = function (id) {
        axios({
            method: 'get',
            url: `${API_URL}/service/installment-savings-products/${id}`
        })
        .then((res) => {
            detailInstallment.value = res.data
            console.log(res.data)
        })
        .catch((err) => {
            console.log(err)
        })
    }

    const detailDeposit = ref([])
    const getDetailDeposit = function (id) {
        axios({
            method: 'get',
            url: `${API_URL}/service/deposit-products/${id}`
        })
        .then((res) => {
            detailDeposit.value = res.data
            console.log(res.data)
        })
        .catch((err) => {
            console.log(err)
        })
    }

    return { 
        getExchanges, 
        exchange, 
        getDepositProducts, 
        depositproducts, 
        getInstallmentProducts, 
        installmentproducts,
        getDetailDeposit,
        detailDeposit,
        getDetailInstallment,
        detailInstallment
        }
}, { persist: true })