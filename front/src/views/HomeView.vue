<template>
   <div id="wrap">
      <div id="header" class="direct_hi_header">
         <div id="container" class="container">
            <div id="content" class="content">
               <div class="main_top_inner">
                  <div class="top_quick_list">
                     <div class="top_quick_title">
                        <h2>"고객님,"
                           <br>
                           "어떤 상품을 찾으시나요?"
                        </h2>
                        <img src="" alt="기본인사">
                     </div>

                     <div class="comp_quick_list">
                        <ul>
                           <li>
                              <a href="">
                                 <strong>예금</strong>
                                 <em>
                                    "어쩌구"
                                    <br>
                                    "저쩌구"
                                 </em>
                                 <span class="">
                                    <img src="" alt="">
                                 </span>
                              </a>
                           </li>
                           <li>
                              <a href="">
                                 <strong>적금</strong>
                                 <em>
                                    "어쩌구"
                                    <br>
                                    "저쩌구"
                                 </em>
                                 <span class="">
                                    <img src="" alt="">
                                 </span>
                              </a>
                           </li>
                        </ul>
                        <div class="comp_login_out">
                           <div class="comp_login_area">
                              <h2>내가 가입한 금융 상품</h2>
                              <a href="">예금 |</a>
                              <a href="">적금</a>
                           </div>
                        </div>
                        <div>
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
  background-color: #f0f0f0;
  padding: 0px 50px; /* 기본값은 50px */
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
  width: 100%;
  position: relative;
  overflow: hidden; /* 부모 요소의 내용이 넘칠 때 숨김 처리 */
}

/* 미디어 쿼리를 이용한 반응형 조정 */
@media screen and (max-width: 600px) {
  /* 현재 창 크기가 600px 이하인 경우 */
  #wrap {
    padding: 0 10px; /* 좁은 화면에서는 양 옆 공백을 줄입니다. */
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

/* 그 외의 내용에 필요한 스타일링을 진행해주세요. */

</style>