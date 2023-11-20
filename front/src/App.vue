<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <RouterLink :to="{ name: 'HomeView' }">Home |</RouterLink>
  <RouterLink :to="{ name: 'ExchangeView' }">Exchange |</RouterLink>
  <RouterLink :to="{ name: 'DepositProductsView' }">DepositProducts |</RouterLink>
  <RouterLink :to="{ name: 'InstallmentProductsView' }">InstallmentProducts |</RouterLink>
  <RouterLink :to="{ name: 'MapView' }">Map |</RouterLink>

  <RouterView />
</template>

<style scoped>
</style>
