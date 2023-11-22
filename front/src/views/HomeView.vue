<template>
   <div id="wrap">
      <div id="header" class="direct_hi_header">
         <div id="container" class="container">
            <div id="content" class="content">
               <div class="main_top_inner">
                  <div class="top_quick_list">
                     <div class="comp_quick_list">
                        <div class="top_quick_title">
                           <h2>"고객님,"
                              <br>
                              "어떤 상품을 찾으시나요?"
                           </h2>
                           <img class="investment" src="@/assets/investment.png" alt="기본인사">
                        </div>

                     
                        <div class="card-wrapper">
                           <div class="card">
                              <a href="#" class="card-content">
                              <strong>예금</strong>
                              <span class="card-image">
                                 <img src="#" alt="">
                              </span>
                              </a>
                           </div>

                           <div class="card">
                              <a href="#" class="card-content">
                              <strong>적금</strong>
                              <span class="card-image">
                                 <img src="#" alt="">
                              </span>
                              </a>
                           </div>
                        </div> 
                     </div>

                     <div class="comp_login_out">
                        <div class="comp_login_area">
                           <h2>내가 가입한 금융 상품</h2>
                           <a href="">예금 |</a>
                           <a href="">적금</a>
                        </div>
                     </div>
                        
                        <div class="comps">
                           <ul>
                              <li>
                              <a href="">
                                 <strong>은행찾기</strong>
                                 <span class="">
                                    <img src="" alt="">
                                 </span>
                              </a>
                              </li>
                              <li>
                              <a href="">
                                 <strong>환율계산기</strong>
                                 <span class="">
                                    <img src="" alt="">
                                 </span>
                              </a>
                              </li>
                              <li>
                              <a href="">
                                 <strong>커뮤니티</strong>
                                 <span class="">
                                    <img src="" alt="">
                                 </span>
                              </a>
                              </li>
                              <li>
                              <a href="">
                                 <strong>마이페이지</strong>
                                 <span class="">
                                    <img src="" alt="">
                                 </span>
                              </a>
                              </li>
                           </ul>
                        </div>
                     
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

/* 전체 페이지를 감싸는 컨테이너 */
#wrap {
  display: flex;
  justify-content: center;
  padding: 0px 100px; /* 기본값은 50px */
}

/* 페이지 내 컨텐츠를 감싸는 컨테이너 */
.content {
  max-width: 100%;
  width: 100%;
}

/* Header */
.direct_hi_header {
  background-color: #fff;
  padding: 20px 0;
  width: 80%;
  position: relative;
  overflow: hidden; /* 부모 요소의 내용이 넘칠 때 숨김 처리 */
}

/* 미디어 쿼리를 이용한 반응형 조정 */
@media screen and (max-width: 1000px) {
  /* 현재 창 크기가 1000px 이하인 경우 */
  #wrap {
    padding: 0; /* 좁은 화면에서는 양 옆 공백을 줄입니다. */
  }

  .direct_hi_header {
    padding: 20px 0; /* 상하 여백은 필요에 따라 조절하세요 */
    width: 100%;
  }
}

/* Top Menu */
.top_menu {
  margin-bottom: 20px;
}

.top_menu_container {
  position: absolute;
  top: 0;
  right: 0;
  margin: 20px;
}

.top_menu_inner ul {
  list-style: none;
  padding: 0;
}

.top_menu_inner ul li {
  display: inline-block;
  margin-right: 10px;
}

/* Header Inner */
.header_inner {
  display: flex;
  align-items: center;
  margin: 20px;
}

.blind{
   margin-right: 20px;
}

/* GNB */
.gnb ul {
  list-style: none;
  padding: 0;
  display: flex;
}

.gnb ul li {
  margin-right: 15px;
}

/* Main Content */
.main_top_inner {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background-color: #fff;
}

.logout-form {
  display: inline-block; /* 폼을 인라인 레벨로 변경하여 다른 컨텐츠와 나란히 위치하도록 설정합니다. */
  margin-left: 0px; /* 버튼과의 간격 설정 */
}

/* 로그아웃 버튼 스타일 */
.logout-btn {
  padding: 6px 10px;
  font-size: 16px;
  border: none;
  background-color: #fff;
  color: #333;
  border-radius: 4px;
  cursor: pointer;
}

.top_quick_title {
  font-size: 12px; /* 텍스트의 글꼴 크기 설정 */
  border: 1px solid transparent; /* 기존 보더 초기화 */
  position: relative; /* 상대 위치 설정 */
  display: flex; /* Flexbox 사용 */
  align-items: center; /* 수직 가운데 정렬 */
}

.top_quick_title::after {
  position: absolute;
  content: ''; /* 가상 요소를 생성하여 보더를 만듭니다. */
  bottom: 0;
  left: 0;
  width: calc(100% - 100px); /* 텍스트 너비 계산 (이미지 너비 100px 감안) */
}

.top_quick_title h2 {
  flex: 1; /* 텍스트가 남은 공간을 모두 차지하도록 설정 */
  margin-right: 20px; /* 이미지와의 간격 설정 */
}

.top_quick_title img.investment {
  max-width: 50px; /* 이미지의 최대 너비 설정 */
  order: -1; /* 이미지를 텍스트 앞에 배치합니다. */
  margin-right: 20px;
  margin-left: 10px;
}

.comp_login_out {
   border: 1px solid #ddd;
   border-radius: 8px;
}

.comps{
   border: 1px solid #ddd;
   border-radius: 8px;
}

/* 고객님 어떤상품 */
.comp_quick_list{
   border: 1px solid #ddd;
   border-radius: 8px;
}
/* 예적금 카드 */
.card-wrapper {
  display: flex;
  padding: 10px;
}

.card {
  width: 150px; /* 카드 너비 조정 */
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  box-sizing: border-box;
  position: relative;
  margin-bottom: 20px;
  text-align: center;
  margin-right: 20px;
}

.card-content {
  text-decoration: none;
  color: #333;
}

.card-content:hover {
  background-color: #f9f9f9;
}

</style>