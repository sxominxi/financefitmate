import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import DepositProductsView from '@/views/DepositProductsView.vue'
import DepositDetailView from  '@/views/DepositDetailView.vue'

import InstallmentProductsView from '@/views/InstallmentProductsView.vue'
import installmentDetailView from '@/views/installmentDetailView.vue'

import MyPageView from '@/views/MyPageView.vue'
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
      path: '/service/deposit-products/:id',
      name: 'DepositDetailView',
      component: DepositDetailView
    },
    {
      path: '/service/installment-savings-products/',
      name: 'InstallmentProductsView',
      component: InstallmentProductsView
    },
    {
      path: '/service/installment-savings-products/:id',
      name: 'installmentDetailView',
      component: installmentDetailView
    },
    {
      path: '/service/map/',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/mypage',
      name: 'MyPageView',
      component: MyPageView
    },
  ]
})

export default router
