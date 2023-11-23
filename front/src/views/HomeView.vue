<template>
   <div id="wrap">
      <div id="header" class="check">
         <div id="container" class="inner">
            <div id="content" class="content">
               <div class="main_top_inner">
                  <div class="top_quick_list">
                     <div class="comp_quick_list">
                        <div class="top_quick_title">
                           <h2><strong>고객님,
                              <br>
                              어떤 상품을 찾으시나요?
                           </strong>
                           </h2>
                           <img class="investment" src="@/assets/investment.png" alt="기본인사">
                        </div>

                     
                        <div class="card-wrapper">
                           <div class="card">
                              <RouterLink :to="{ name: 'DepositProductsView' }" class="card-content"><strong>예금</strong></RouterLink>
                              <span class="card-hover">
                                 <img src="@/assets/bauble.png" alt="" class="card-img">
                              </span>
                           </div>

                           <div class="card">
                              <RouterLink :to="{ name: 'InstallmentProductsView' }" class="card-content"><strong>적금</strong></RouterLink>
                              <span class="card-hover">
                                 <img src="@/assets/reindeer.png" alt="" class="card-img">
                              </span>
                           </div>
                        </div> 
                     </div>

                     <div class="my_finance">
                        <div class="comp_quick_list2">
                           <div class="divbox"> <!-- 얘는 안보이는 박스임 -->
                              <h2>내가 가입한 금융 상품</h2>
                              <img class="investment" src="@/assets/target.png" alt="기본인사">
                           </div>
                              <div class="card3">
                                 <div class="comp_quick_title">
                                    <h2><strong>내가 가입한 금융 상품</strong></h2>
                                    <div class="investment_div">d</div>
                                 </div>

                                 <div class="card-wrapper">
                                    <div class="card2">
                                       <RouterLink :to="{ name: 'MydepositView' }" class="card-content"><strong>예금</strong></RouterLink>
                                       <span class="card-hover">
                                          <img src="@/assets/snow-globe.png" alt="" class="card-img1">
                                       </span>
                                    </div>

                                    <div class="card2">
                                       <RouterLink :to="{ name: 'MyinstallmentView' }" class="card-content"><strong>적금</strong></RouterLink>
                                       <span class="card-hover">
                                          <img src="@/assets/mitten.png" alt="" class="card-img1">
                                       </span>
                                    </div>
                                 </div>
                              </div>

                        </div>
                     </div>
                  </div>
                        
                        <div class="comps">
                           <ul>
                              <li class="menu-item">
                                 <RouterLink :to="{ name: 'MapView' }" class="menu-link">
                                    <span class="menu-img">
                                       <img src="@/assets/3d-map.png" alt="">
                                    </span>
                                    <strong class="comps_text">은행찾기</strong>
                                 </RouterLink>
                              </li>
                              <li class="menu-item">
                                 <RouterLink :to="{ name: 'ExchangeView' }" class="menu-link">
                                    <span class="menu-img">
                                       <img src="@/assets/calculator.png" alt="">
                                    </span>
                                    <strong class="comps_text">환율계산기</strong>
                                 </RouterLink>
                              </li>
                              <li class="menu-item">
                                 <RouterLink :to="{ name: 'PostView' }" class="menu-link">
                                    <span class="menu-img">
                                       <img src="@/assets/newspaper.png" alt="">
                                    </span>
                                    <strong class="comps_text">금융꿀팁</strong>
                                 </RouterLink>
                              </li>
                              <li class="menu-item">
                                 <RouterLink :to="{ name: 'MyPageView' }" class="menu-link">
                                    <span class="menu-img">
                                       <img src="@/assets/google.png" alt="">
                                    </span>
                                    <strong class="comps_text">마이페이지</strong>
                                 </RouterLink>
                              </li>
                           </ul>
                        </div>
                     
                  
               </div>
            </div>
         </div>
      </div>
   </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/modules/counter'

const store = useCounterStore()


</script>

<style scoped>
/* 고객님과 가입금융상품 div */
.top_quick_list {
   display: flex;
}
/* 고객님, 어떤 상품을 찾으시나요 ? */
.comp_quick_list{
   border-radius: 30px;
   width: 50%;
}

.top_quick_title {
  /* border: 3px solid transparent; 기존 보더 초기화 */
  position: relative; /* 상대 위치 설정 */
  display: flex; /* Flexbox 사용 */
  align-items: center; /* 수직 가운데 정렬 */
  padding-bottom: 20px;
}

.top_quick_title h2 {
  font-size: 20px; /* 텍스트의 글꼴 크기 설정 */
  margin: 0;
  line-height: 30px;
}

.top_quick_title::after {
  position: absolute;
  content: ''; /* 가상 요소를 생성하여 보더를 만듭니다. */
  bottom: 0;
  left: 0;
  /* width: calc(100% - 100px); 텍스트 너비 계산 (이미지 너비 100px 감안) */
}

.top_quick_title img.investment {
  max-width: 70px; /* 이미지의 최대 너비 설정 */
  order: -1; /* 이미지를 텍스트 앞에 배치합니다. */
  margin-right: 10px;
  margin-left: 10px;
  padding-inline-start: 15px;
}

/* 예적금 카드 */
.card-wrapper {
  display: flex;
  justify-content: space-around;
}

.card {
  width: 45%; /* 카드 너비 조정 */
  height: 150px;
  border: 3px solid #198754;
  border-radius: 30px;
  box-sizing: border-box;
  position: relative;
}

.card-content {
   text-decoration: none;
   color: #333;
   width: 100%;
   height: 100%;
   position: relative;
   display: inline-block;
   z-index: 2; /* card-hover 위로 올려주기 위한 z-index 설정 */
}

.card-content > strong{
   font-size: 20px;
   padding: 25px;
}
.card-hover {
  display: none;
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: 1;
  transform: translate(-50%, -50%);
}

.card-content:hover + .card-hover {
  display: block;
}

.card-content:hover {
  border: none ; /* border 없애기 */
}

/* 내가 가입한 금융상품 */
.my_finance {
   width: 50%;
}
.my_finance h2 {
   font-size: 20px; /* 텍스트의 글꼴 크기 설정 */
   margin: 0;
}
.my_finance img.investment {
  max-width: 70px; /* 이미지의 최대 너비 설정 */
  margin-right: 10px;
  margin-left: 10px;
}
.investment_div{
   height: 60px;
   visibility: hidden;
}

.comp_quick_title {
  /* border: 3px solid transparent; 기존 보더 초기화 */
  position: relative; /* 상대 위치 설정 */
  display: flex; /* Flexbox 사용 */
  align-items: center; /* 수직 가운데 정렬 */
  margin-inline-start: 10px;
}
.comp_quick_title > h2 {
  padding-inline-start: 10px;
}
.card2 {
   width: 45%; /* 카드 너비 조정 */
   height: 75px;
   border: 3px solid #198754;
  border-radius: 30px;
  box-sizing: border-box;
  position: relative;
  margin-bottom: 10px;
}
.card3 {
   border: 3px solid #198754;
   border-radius: 30px;
   width: 102%;
}
.card-img {
   width: 100px;
   justify-content: center;
}
.card-img1 {
   width: 60px;
   justify-content: center;
}

.divbox {
  /* border: 3px solid transparent; 기존 보더 초기화 */
  position: relative; /* 상대 위치 설정 */
  display: flex; /* Flexbox 사용 */
  align-items: center; /* 수직 가운데 정렬 */
  visibility: hidden;
  padding-bottom: 14.2px;
}

@media screen and (max-width: 1260px) {
  .my_finance,
  .comp_quick_list {
    width: 100%; /* 모바일 화면일 때 가득 채우도록 설정 */
    box-sizing: border-box; /* 내부 여백과 테두리를 포함한 전체 너비로 설정 */

    margin-bottom: 50px; /* 아래 여백 추가 */
  }
  .top_quick_list {
   display: inline;
  }
  .divbox{
   display: none;
  }
  .card2 {
   width: 45%; /* 카드 너비 조정 */
  height: 150px;
  border: 3px solid #198754;
  border-radius: 30px;
  box-sizing: border-box;
  position: relative;
}
.my_finance img.investment {
  max-width: 70px; /* 이미지의 최대 너비 설정 */
  order: -1; /* 이미지를 텍스트 앞에 배치합니다. */
  margin-right: 10px;
  margin-left: 10px;
}
.comp_quick_title {
  /* border: 3px solid transparent; 기존 보더 초기화 */
  position: relative; /* 상대 위치 설정 */
  display: flex; /* Flexbox 사용 */
  align-items: center; /* 수직 가운데 정렬 */
}
.comps ul {
  list-style-type: none; /* 점 표시 없애기 */
  padding: 20px;
  margin-top: 20px;
  display: flex;
  flex-wrap: wrap; /* 요소들이 가로로 정렬되면서 넘치면 다음 줄로 이동 */
  justify-content: center;
}
.card3 {
   border-radius: 30px;
   border: 3px solid white;
}
.card-img1 {
   width: 100px;
   justify-content: center;
}
}

/* comp */

.comps{
   border-radius: 30px;
}

.comps ul {
  list-style-type: none; /* 점 표시 없애기 */
  padding: 20px;
  margin-top: 50px;
  display: flex;
  flex-wrap: wrap; /* 요소들이 가로로 정렬되면서 넘치면 다음 줄로 이동 */
  justify-content: center;
}

.comps ul li {
  margin-bottom: 10px;
  margin-right: 10px; /* 각 리스트 아이템 간의 간격 조정 */
}

.menu-link {
  text-decoration: none; /* 링크 밑줄 제거 */
  color: inherit; /* 기본 링크 색상 사용 */
  font-weight: bold;
  padding: 10px;
}

.comps img {
   max-width: 70px; /* 이미지의 최대 너비 설정 */
   order: -1; /* 이미지를 텍스트 앞에 배치합니다. */
   margin-right: 10px;
   margin-left: 10px;
}

.menu-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.menu-img {
  max-width: 70px;
}

.comps_text {
   text-align: center;
   margin-bottom: 0;
   display: block;
   margin-top: 15px;
}

.card-content strong {
   margin-left: 20px;
   margin-top: 10px;
   display: block;
}

</style>