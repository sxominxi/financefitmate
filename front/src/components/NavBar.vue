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
                              <!-- 이 못생긴 로그아웃 버튼 어캐 해야됨 -->
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
            <h1>
               <a href="">
                  <RouterLink :to="{ name: 'HomeView' }" class="blind">FinanceFitMate</RouterLink>
               </a>
            </h1>
            <div id="gnb" class="gnb">
               <ul>
                  <li class="is-on">
                     <!-- <a href="" title="금융상품조회">예금조회</a> -->
                     <RouterLink :to="{ name: 'DepositProductsView' }" class="menu-link">예금조회</RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="금융상품조회">적금조회</a> -->
                     <RouterLink :to="{ name: 'InstallmentProductsView' }" class="menu-link">적금조회</RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="은행찾기">은행찾기</a> -->
                     <RouterLink :to="{ name: 'MapView' }" class="menu-link">은행찾기</RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="환율계산기"></a> -->
                     <RouterLink :to="{ name: 'ExchangeView' }" class="menu-link">환율계산기</RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="커뮤니티">커뮤니티</a> -->
                     <RouterLink :to="{ name: 'PostView' }" class="menu-link">금융꿀팁</RouterLink>
                  </li>
                  <li class="is-on">
                     <!-- <a href="" title="마이페이지">마이페이지</a> -->
                     <RouterLink :to="{ name: 'MyPageView' }" class="menu-link">마이페이지</RouterLink>
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
#wrap {
  display: flex;
  justify-content: center;
  padding: 0px 100px; /* 기본값은 50px */
}

/* Header */
.direct_hi_header {
  background-color: #fff;
  padding: 20px 0;
  width: 100%;
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
   font-size: 25px;
   color: #333;
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