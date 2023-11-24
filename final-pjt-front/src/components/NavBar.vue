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
                     <RouterLink :to="{ name: 'DepositProductsView' }" class="menu-link"><strong>예금조회</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <RouterLink :to="{ name: 'InstallmentProductsView' }" class="menu-link"><strong>적금조회</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <RouterLink :to="{ name: 'RecommendView' }" class="menu-link"><strong>금융상품추천</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <RouterLink :to="{ name: 'MapView' }" class="menu-link"><strong>은행찾기</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <RouterLink :to="{ name: 'ExchangeView' }" class="menu-link"><strong>환율계산기</strong></RouterLink>
                  </li>
                  <li class="is-on">
                     <RouterLink :to="{ name: 'PostView' }" class="menu-link"><strong>커뮤니티</strong></RouterLink>
                  </li>
               </ul>
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
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap');


.direct_hi_header {
  background-color: #fff;
  padding: 20px 0;
  width: 100%;
  position: relative;
  overflow: hidden;
}

@media screen and (max-width: 1260px) {
  .direct_hi_header {
    padding: 20px 0;
  }
}

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

.header_inner {
  display: flex;
  align-items: center;
  margin: 20px;
  padding-top: 20px;
}

.blind{
   margin-right: 20px;
   text-decoration: none;
}

.blind > img {
   width: 220px;
   margin-bottom: 7px;
}

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
  display: inline-block;
  margin-left: 0px;
}

.logout-btn {
  font-size: 15px;
  border: none;
  background-color: #fff;
  color: #333;
  border-radius: 4px;
  cursor: pointer;
}

.menu-link1 {
  color: #333;
  text-decoration: none;
  font-size: 15px;
}

.menu-link {
  color: #333;
  text-decoration: none;
  font-size: 17px;
}

</style>