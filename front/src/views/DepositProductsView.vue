<template>
    <div>
        <h1>정기 예금</h1>
    </div>
    <select class="bank" v-model="bank">
        <option value="" selected disable3d hidden>은행</option>
        <option value="하나은행">하나은행</option>
        <option value="국민은행">국민은행</option>
        <option value="SC제일은행">SC제일은행</option>
        <option value="신한은행">신한은행</option>
        <option value="우리은행">우리은행</option>
        <option value="외환은행">외환은행</option>
        <option value="한국시티은행">한국시티은행</option>
        <option value="기업은행">기업은행</option>
        <option value="농협">농협</option>
    </select>
    <select class="duration" v-model="duration">
        <option value="6">6개월</option>
        <option value="12">12개월</option>
        <option value="24">24개월</option>
        <option value="36">36개월</option>
    </select>
    <button @click="search">검색</button>
</template>

<script setup>
import { useServiceStore } from '@/stores/service'
import { ref, onMounted } from 'vue'
import axios from 'axios';

const store = useServiceStore()
const bank = ref(null)
const duration = ref(null)

onMounted(() => {
    store.getDepositProducts()
})

const click = function() {
    
}

</script>

<style scoped>

</style>