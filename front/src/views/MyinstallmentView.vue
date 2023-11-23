<template>
    <div id="wrap">
       <div class="check">
          <div class="inner">
 
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1><strong>가입한 적금</strong></h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div> 
             
            <div class="title-top" v-if="installments.length > 0">
                <div v-for="product in installments">
                    <div v-if="product[2].pk === store.userInfo.pk">
                        <h3><strong>{{ product[0].fin_prdt_nm }}</strong></h3>
                        <p class="product-name fs-6">금융회사 명: {{ product[0].kor_co_nm }}</p>
                        <div v-for="option in product[0].option_set">
                            <div v-if="option.save_trm === product[1]">
                                <p>기간: {{ option.save_trm }} 개월</p>
                                <p>저축 금리 유형: {{ option.intr_rate_type_nm }}</p>
                                <p>저축 금리: {{ option.intr_rate }}</p>
                                <p class="text-danger">적립 유형명: {{ option.rsrv_type_nm }}</p>
                                <p class="text-danger">최대 우대 금리: {{ option.intr_rate2 }}</p>
                            </div>
                        </div>
                        <hr>
                    </div>
                </div>
            </div>

            <div class="chart">
                 <h2>가입한 상품 금리 정보 한 눈에 보기</h2>
                <button class="btn btn-success" @click="createChart">내 상품 금리 정보 비교하기</button>
            </div>
            <div v-if="IsChart">
               <Bar :data="chartData" :options="chartOptions"/>
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
         backgroundColor: '#5bc0de',
         data: graph_y1
         },
         {
         label: '최대 우대 금리',
         backgroundColor: '#0275d8',
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
 .title-top {
    margin-top: 40px;
 }

 .product-name{
   margin-top: 30px;
}
hr {
  color: green; 
}

.info-main {
   margin: 40px 0;
}

.togle-ment {
   margin-top: 30px;
}

.chart {
    margin-top: 40px;
    display: flex;
    justify-content: space-between;
}
 </style>