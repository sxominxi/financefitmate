import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import DepositProductsView from '@/views/DepositProductsView.vue'
import DepositDetailView from  '@/views/DepositDetailView.vue'

import InstallmentProductsView from '@/views/InstallmentProductsView.vue'
import installmentDetailView from '@/views/installmentDetailView.vue'

import MyPageView from '@/views/MyPageView.vue'
import MapView from '@/views/MapView.vue'

import PostView from '@/views/PostView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import UpdateView from '@/views/UpdateView.vue'
import UpdateUserView from '@/views/UpdateUserView.vue'


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

    {
      path: '/posts',
      name: 'PostView',
      component: PostView
    },
    {
      path: '/posts/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/post/:id',
      name: 'UpdateView',
      component: UpdateView
    },

    {
      path: '/account/update-profile/',
      name: 'UpdateUserView',
      component: UpdateUserView
    },
  ]
})

import { useCounterStore } from '@/stores/modules/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'CreateView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'PostView' }
  }
})

export default router
