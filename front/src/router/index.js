import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import DepositProductsView from '@/views/DepositProductsView.vue'
import MapView from '@/views/MapView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/service/exchange/',
      name: 'ExchangeView',
      component: ExchangeView
    },
    {
      path: '/service/deposit-products/',
      name: 'DepositProductsView',
      component: DepositProductsView
    },
    {
      path: '/service/map/',
      name: 'MapView',
      component: MapView
    },
  ]
})

export default router
