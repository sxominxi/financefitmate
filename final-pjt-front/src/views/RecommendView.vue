<template>
    <div id="wrap">
       <div class="check">
          <div class="inner">
             
             <div class="title-box">
                <div class="title">
                   <div class="border border-3 border-bottom-0 border-success rounded-top">
                      <h1><strong>금융 상품 추천</strong></h1>
                   </div>
                </div>
                <div class="title-etc">
                   <div class="border-3 border-bottom border-success"></div>
                </div>
             </div>
 
             <div class="sideview">
                 <div class="sideview1">
                 <div class="reco-title">
                     <h2>예금 상품 추천</h2>
                 </div>
 
                 <div class="card-list" v-for="product in store2.depositproducts">
                     <div v-for="recommends in store.customProduct">
                         <div class="card border-success mb-3 col-12" v-if="product.fin_prdt_cd == recommends"  @click="goDetailDeposit(product.id)">
                             <div class="card-header">{{ product.kor_co_nm }}</div>
                             <div class="card-body" >
                                 <h5 class="card-title fs-3 fw-bold text-success">{{ product.fin_prdt_nm }}</h5>
                                 <div class="card-function">
            
                                 </div>
                             </div>
                         </div>
                     </div>
                 </div>
                 </div>
 
                 <div class="sideview2">
                 <div class="reco-title">
                     <h2>적금 상품 추천</h2>
                 </div>
 
                 <div class="card-list" v-for="product in store2.installmentproducts">
                     <div v-for="recommends in store.customProduct">
                         <div class="card border-success mb-3 col-12" v-if="product.fin_prdt_cd == recommends" @click="goDetailInstallment(product.id)">
                             <div class="card-header">{{ product.kor_co_nm }}</div>
                             <div class="card-body">
                                 <h5 class="card-title fs-3 fw-bold text-success">{{ product.fin_prdt_nm }}</h5>
                                 <div class="card-function">
                                     
                                 </div>
                             </div>
                         </div>
                     </div>
                 </div>
             </div>
             </div>
          </div>
       </div>
    </div>
 </template>
 
 <script setup>
 import { onMounted, ref } from 'vue';
 import { useCounterStore } from '../stores/modules/counter';
 import { useServiceStore } from '@/stores/modules/service';
 import { useRouter } from 'vue-router';
 
 const router = useRouter()
 const store = useCounterStore()
 const store2 = useServiceStore()
 const goDetailDeposit = function(deposit_id) {
     router.push({
         name: 'DepositDetailView',
         params: { id: deposit_id}
     })
 }
 
 const goDetailInstallment = function(installment_id) {
     router.push({
         name: 'installmentDetailView',
         params: { id: installment_id }
     })
 }  
 
 const DepositProduct = ref([])
 const recommendDepoist = function() {
     for (const item of store2.depositproducts) {
         for (const recommenditem of store.customProduct) {
             if ( item.fin_prdt_cd === recommenditem) {
                 DepositProduct.value.push(item)
             }
         }
     }
 }
 
 const InstallmentProduct = ref([])
 const recommendInstallment = function() {
     for (const item2 of store2.installmentproducts) {
         for (const recommenditem of store.customProduct) {
             if ( item2.fin_prdt_cd === recommenditem) {
                 InstallmentProduct.value.push(item2)
             }
         }
     }
 }

 onMounted(() => {
     store.recommendProducts()
     store.userFind()
     store2.getDepositProducts()
     store2.getInstallmentProducts()
     recommendDepoist()
     recommendInstallment()
 })
 
 
 onMounted(() => {
     store.recommendProducts()
     store.userFind()
     store2.getDepositProducts()
     store2.getInstallmentProducts()
 })
 
 </script>
 
 <style scoped>
 .reco-title {
     padding: 10px;
     margin-top: 30px;
     font-size: 15px;
 }
 .reco-title > h2 {
     font-size: 23px;
 }
 .select-list {
    display: flex;
    flex-direction: row;
    justify-content: left;
    align-items: center; 
    padding-left: 20px;
    padding-right: 20px;
  }
 
  .select-list select {
    width: 200px;
    height: 50px;
    margin: 30px 10px;
  }
 
  .select-list > button {
    width: 80px;
    height: 48px; 
    margin: 30px 10px;
  }
 
  .card {
     width: 99%;
  }
  .card-list{
     display: flex;
     flex-direction: column;
     align-items: left;
     padding-right: 5px;
     padding-left: 5px;
  }
 
  .card-body > h5 {
     height: 5px;
  }
 
  .not {
    padding-inline-start: 30px;
  }
 
  .card-main {
     display: flex;
     justify-content: space-between;
  }
 
  .card-text {
     margin: 0 0;
  }
  .intr {
     display: flex;
     flex-direction: column;
     align-items: end;
  }
 
  .card-function {
     display: flex;
     justify-content: space-between;
     margin-top: 50px;
  }
 
 .sideview{
     display: flex;
     flex-direction: row; 
 }
 
 .sideview1{
     flex: 1; 
 }
 .sideview2{
     flex: 1;
 }

  .card:hover {
    cursor: pointer;
  } 
 </style>