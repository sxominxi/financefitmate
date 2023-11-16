<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <RouterLink :to="{ name: 'HomeView'}">Home |</RouterLink>
  <RouterLink :to="{ name: 'ExchangeView'}">Exchange |</RouterLink>

  <RouterView />
</template>

<style scoped>
</style>
