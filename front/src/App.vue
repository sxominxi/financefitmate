<script setup>
import { RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/modules/counter'
import NavBar from '@/components/NavBar.vue';

const store = useCounterStore()

</script>

<template>
   <NavBar />
   <RouterView />
</template>

<style scoped>
</style>
