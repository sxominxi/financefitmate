<template>
    <div id="wrap">
       <div class="check">
          <div class="inner">
 
             <h1>가입한 정기 적금 상품</h1> 
             <hr>
             <div v-if="installments.length > 0">
                   <div v-for="product in installments">
                      <h4>가입 상품: {{ product[0].fin_prdt_nm }}</h4>
                      <p>금융회사 명: {{ product[0].kor_co_nm }}</p>
                      <div v-for="option in product[0].option_set">
                         <div v-if="option.save_trm === product[1]">
                               <p>기간: {{ option.save_trm }} 개월</p>
                               <p>저축 금리 유형: {{ option.intr_rate_type_nm }}</p>
                               <p>저축 금리: {{ option.intr_rate }}</p>
                               <p>최대 우대 금리: {{ option.intr_rate2 }}</p>
                         </div>
                      </div>
                      <hr>
                   </div>
             </div>
             <hr>
                   <h2>가입한 상품 금리</h2>
             <div>
                   <button @click="createChart">내 상품 금리 정보 비교하기</button>
                   <div v-if="IsChart">
                      <Bar :data="chartData" :options="chartOptions"/>
                   </div>
             
             </div>
          </div>
       </div>
    </div>
 </template>
 
 
 
 <script setup>
 import { Bar } from 'vue-chartjs'
 import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
 import { ref, onMounted } from 'vue'
 import { useCounterStore } from '../stores/modules/counter';
 ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
 
 const store = useCounterStore()
 const installments = ref([])
 installments.value = JSON.parse(localStorage.getItem('become_installment')) || []
 
 const graph_x = ['평균 금리']
 const graph_y1 = [3.99]
 const graph_y2 = [3.99]
 
 
 const getX2 = function() {
     for (const x2_nm of installments.value) {
         if (x2_nm[2].pk == store.userInfo.pk) {
             graph_x.push(x2_nm[0].fin_prdt_nm.replace('\n',''))
             for(const y2_nm of x2_nm[0].option_set) {
                 if (y2_nm.save_trm === x2_nm[1]){
                     graph_y1.push(y2_nm.intr_rate)
                     graph_y2.push(y2_nm.intr_rate2)
                 }   
             }
         }
     }
 }
 
 const IsChart = ref(false)
 const chartData = ref({})
 const chartOptions = ref({})
 
 const createChart = function() {
     IsChart.value = true
     chartData.value = {
     active: true,
     labels:  graph_x,
     datasets: [
         {
         label: '저축 금리',
         backgroundColor: '#f87979',
         data: graph_y1
         },
         {
         label: '최대 우대 금리',
         backgroundColor: '#f15851',
         data: graph_y2
         }
     ]
     }
     chartOptions.value = {
     responsive: true,
     // maintainAspectRatio: true,
     scales: {
         y: {
             suggestedMin: 0,
             suggestedMax: 5,
             beginAtZero: true
         }}
     }
 }
 
 onMounted(() => {
     getX2(),
     store.userFind()
 })
 
 </script>
 
 <style scoped>
 
 </style>