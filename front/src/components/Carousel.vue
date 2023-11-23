<template>
    <div id="carouselExampleCaptions" class="carousel slide">
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <div class="box1">
                </div>
                <div class="carousel-caption d-none d-md-block">
                    <h5>First slide label</h5>
                    <p>Some representative placeholder content for the first slide.</p>
                </div>
            </div>
            <div class="carousel-item">
                <div class="box2">
                </div>
            <div class="carousel-caption d-none d-md-block">
                <h5>Second slide label</h5>
                <p>Some representative placeholder content for the second slide.</p>
            </div>
            </div>
            <div class="carousel-item">
                <div class="box3">
                </div>
            <div class="carousel-caption d-none d-md-block">
                <h5>Third slide label</h5>
                <p>Some representative placeholder content for the third slide.</p>
            </div>
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
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


onMounted(() => {
    store.recommendProducts()
    store.userFind()
    store2.getDepositProducts()
    store2.getInstallmentProducts()
})
</script>

<style scoped>
.carousel-inner {
    width: 100%;
    height: 100%; /* Make the carousel-inner fill the available height */
}
.carousel-item {
    width: 100%;
    height: 100%;
}

img {
    object-fit: cover; /* Maintain aspect ratio while covering the entire container */
    width: 100%; /* Make the image fill the container width */
    height: 100%; /* Make the image fill the container height */
}

.box1 {
    border: 1px solid blue;
    background-color: blue;
    width: 100%;
    height: 100%
}
.box2 {
    border: 1px solid red;
    background-color: red;
    width: 100%;
    height: 100%
}
.box3 {
    border: 1px solid yellow;
    background-color:yellow;
    width: 100%;
    height: 100%
}
.carousel {
    margin-top: 20px;
    width: 90%;
    height: 50%;
}
</style>