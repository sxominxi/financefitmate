import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ExchangeView from '@/views/ExchangeView.vue'

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
  ]
})

export default router
