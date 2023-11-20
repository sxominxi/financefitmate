<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/modules/counter'

const store = useCounterStore()

</script>

<template>
  <RouterLink :to="{ name: 'HomeView' }">Home |</RouterLink>
  <RouterLink :to="{ name: 'ExchangeView' }">Exchange |</RouterLink>
  <RouterLink :to="{ name: 'DepositProductsView' }">DepositProducts |</RouterLink>
  <RouterLink :to="{ name: 'InstallmentProductsView' }">InstallmentProducts |</RouterLink>
  <RouterLink :to="{ name: 'MapView' }">Map |</RouterLink>
  <RouterLink :to="{ name: 'MyPageView' }">MyPage |</RouterLink>

  <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> |
  <nav v-if="store.isLogin">
    <form @submit.prevent="store.logOut">
      <input type="submit" value="logOut">
    </form>
  </nav>
  <nav v-else>
    <RouterLink :to="{ name: 'SignUpView' }">SignUp</RouterLink> |
    <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink>
  </nav>

  <RouterView />
</template>

<style scoped>
</style>
