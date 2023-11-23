<template>
   <div id="wrap">
      <div id="header" class="direct_hi_header">
         <!-- 회원가입 | 로그인  -->
         <div class="top_menu">
            <div class="top_menu_container">
               <div class="top_menu_inner">
                  <ul>
                     <li>
                        <RouterLink :to="{ name: 'MyPageView' }" class="menu-link1">마이페이지 |</RouterLink>
                        <template v-if="store.isLogin">
                           <form @submit.prevent="store.logOut" class="logout-form">
                              <button type="submit" class="logout-btn">로그아웃</button> 
                           </form>
                        </template>
                        <template v-else>
                           <RouterLink :to="{ name: 'SignUpView' }" class="menu-link1"> 회원가입 |</RouterLink>
                           <RouterLink :to="{ name: 'LogInView' }" class="menu-link1"> 로그인</RouterLink>
                        </template>
                     </li>
                  </ul>
               </div>
            </div>
         </div>
         <!-- 로고와 nav bar -->
         <div class="header_inner">
            <RouterLink :to="{ name: 'HomeView' }" class="blind">
               <img src="@/assets/logo.png" alt="" class="blind-img">
            </RouterLink>
            <div id="gnb" class="gnb">
               <ul>
                  <li class="is-on">
                     <!-- <a href="" title="금융상품조회">예금조회</a> -->
                     <RouterLink :to="{ name: 'DepositProductsView' }" class="menu-link"><strong>예금조회</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="금융상품조회">적금조회</a> -->
                     <RouterLink :to="{ name: 'InstallmentProductsView' }" class="menu-link"><strong>적금조회</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="은행찾기">은행찾기</a> -->
                     <RouterLink :to="{ name: 'MapView' }" class="menu-link"><strong>은행찾기</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="환율계산기"></a> -->
                     <RouterLink :to="{ name: 'ExchangeView' }" class="menu-link"><strong>환율계산기</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="커뮤니티">커뮤니티</a> -->
                     <RouterLink :to="{ name: 'PostView' }" class="menu-link"><strong>금융꿀팁</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="마이페이지">마이페이지</a> -->
                     <RouterLink :to="{ name: 'MyPageView' }" class="menu-link"><strong>마이페이지</strong></RouterLink>
                  </li>
               </ul>
            </div>
         </div>
      </div>
   </div>
   <RouterLink :to="{ name: 'RecommendView' }">RecommendProducts</RouterLink>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/modules/counter'

const store = useCounterStore()

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap');

.direct_hi_header {
  background-color: #fff;
  padding: 20px 0;
  width: 100%;
  position: relative;
  overflow: hidden; /* 부모 요소의 내용이 넘칠 때 숨김 처리 */
}

/* 미디어 쿼리를 이용한 반응형 조정 */
@media screen and (max-width: 1260px) {
  /* 현재 창 크기가 1000px 이하인 경우 */
  .direct_hi_header {
    padding: 20px 0; /* 상하 여백은 필요에 따라 조절하세요 */
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
  margin-bottom: 50px;
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
  padding-top: 20px;
}

.blind{
   margin-right: 20px;
   text-decoration: none; /* 밑줄 제거 */
}

.blind > img {
   width: 220px;
   margin-bottom: 7px;
}

/* GNB */
.gnb ul {
  list-style: none;
  padding: 0;
  margin-bottom: 8px;
  display: flex;
}

.gnb ul li {
  margin-right: 15px;
}

.logout-form {
  display: inline-block; /* 폼을 인라인 레벨로 변경하여 다른 컨텐츠와 나란히 위치하도록 설정합니다. */
  margin-left: 0px; /* 버튼과의 간격 설정 */
}

/* 로그아웃 버튼 스타일 */
.logout-btn {
  font-size: 15px;
  border: none;
  background-color: #fff;
  color: #333;
  border-radius: 4px;
  cursor: pointer;
}

.menu-link1 {
  color: #333; /* 글자 색상 통일 */
  text-decoration: none; /* 밑줄 제거 */
  font-size: 15px;
}

.menu-link {
  color: #333; /* 글자 색상 통일 */
  text-decoration: none; /* 밑줄 제거 */
  font-size: 17px;
}

</style>