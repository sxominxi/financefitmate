<template>
    <div>
        <h1>마이 페이지</h1>
        <h2>가입한 정기 예금 상품</h2>
        <div v-if="deposits.length > 0">
            <div v-for="product in deposits">
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
        <div v-else>
            <strong>가입한 정기 예금 상품이 없습니다.</strong>
        </div>
        <hr>
        <h2>가입한 정기 적금 상품</h2>
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
        <div v-else>
            <strong>가입한 정기 적금 상품이 없습니다.</strong>
        </div>
        <hr>
            <h2>가입한 상품 금리</h2>
        <div>
            <Bar :data="chartData" :options="chartOptions" />
        </div>
    </div>
</template>



<script setup>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import { useServiceStore } from '../stores/modules/service';
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const store = useServiceStore()

const deposits = ref([])
deposits.value = JSON.parse(localStorage.getItem('become_deposit')) || []


const installments = ref([])
installments.value = JSON.parse(localStorage.getItem('become_installment')) || []

const graph_x = []
const getX = function() {
    for (const x_nm of deposits.value) {
        graph_x.push(x_nm[0].fin_prdt_nm.replace('\n',''))
    }
}

console.log(graph_x)

const chartData = ref({
    labels:  graph_x,
    datasets: [
      {
        label: '저축 금리',
        backgroundColor: '#f87979',
        data: [40, 20, 40]
      },
      {
        label: '최대 우대 금리',
        backgroundColor: '#f15851',
        data: [40, 20, 40]
      }
    ]
  })
  const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: false
  })


  onMounted(() => {
    getX()
  })
</script>

<style scoped>

</style>