<template>
    <div>
        <h1>Exchange</h1>
        <div class="exchange">
            <select name="cur_nm" v-model="cur_another">
                <option v-for="country in store.exchange">{{ country.cur_nm }}</option>
            </select>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useServiceStore } from '@/stores/service';
import axios from 'axios'

const cur_kr = ref(null)
const cur_another = ref(null)
const store = useServiceStore()

onMounted(() => {
    store.getExchanges()
})

</script>

<style scoped>

</style>