<template>
  <div id="wrap">
     <div class="check">
        <div class="inner">
          <div class="box">
            <div class="title-box">
               <div class="title">
                  <div class="border border-3 border-bottom-0 border-success rounded-top">
                     <h1 class="fs-3 fw-bold"><strong>은행 찾기</strong></h1>
                  </div>
               </div>
               <div class="title-etc">
                  <div class="border-3 border-bottom border-success"></div>
               </div>
            </div>
            <div class="select-list">
              <title>주소로 장소 표시하기</title>
              <select id="sido" v-model="select_area" @input="selected" class="form-select" aria-label="Default select example">
                  <option :value=null>도/시를 선택하세요</option>
                  <option v-for="sido in Object.keys(area)">{{ sido }}</option>
              </select>

              <select id="sigugun" v-model="select_sido" class="form-select">
                  <option :value=null>구/군을 선택하세요</option>
                  <option v-for="sigugun in list_city">{{ sigugun }}</option>
              </select>

              <select class="bank form-select" v-model="bank">
                    <option value="bank" selected disable3d hidden>은행을 선택하세요</option>
                    <option value="하나은행">하나은행</option>
                    <option value="국민은행">국민은행</option>
                    <option value="SC제일은행">SC제일은행</option>
                    <option value="신한은행">신한은행</option>
                    <option value="우리은행">우리은행</option>
                    <option value="외환은행">외환은행</option>
                    <option value="한국시티은행">한국시티은행</option>
                    <option value="기업은행">기업은행</option>
                    <option value="농협">농협</option>
              </select>
              <button type="button" class="btn btn-success" @click="search">검색</button>
            </div>
            <div class="wrapper">
                <div ref="container" class="first">
                </div>
            </div>
          </div>
        </div>
     </div>
  </div>
 </template>
  
  <script setup>
  import { onMounted,ref } from 'vue'
  // -------------------
  const list_city = ref([])
  const select_area = ref(null)
  const select_sido = ref(null)
  const infowindow = ref(null)
  
  const area = ref({
          "서울특별시": [ "강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구" ],
          "경기도" : [ "수원시 장안구", "수원시 권선구", "수원시 팔달구", "수원시 영통구", "성남시 수정구", "성남시 중원구", "성남시 분당구", "의정부시", "안양시 만안구", "안양시 동안구", "부천시", "광명시", "평택시", "동두천시", "안산시 상록구", "안산시 단원구", "고양시 덕양구", "고양시 일산동구", "고양시 일산서구", "과천시", "구리시", "남양주시", "오산시", "시흥시", "군포시", "의왕시", "하남시", "용인시 처인구", "용인시 기흥구", "용인시 수지구", "파주시", "이천시", "안성시", "김포시", "화성시", "광주시", "양주시", "포천시", "여주시", "연천군", "가평군","양평군" ],
          "인천광역시" : [ "계양구", "미추홀구", "남동구", "동구", "부평구", "서구", "연수구", "중구", "강화군", "옹진군" ],
          "강원도" : [ "춘천시", "원주시", "강릉시", "동해시", "태백시", "속초시", "삼척시", "홍천군", "횡성군", "영월군", "평창군", "정선군", "철원군", "화천군", "양구군", "인제군", "고성군", "양양군" ],            
          "충청북도" : [ "청주시 상당구", "청주시 서원구", "청주시 흥덕구", "청주시 청원구", "충주시", "제천시", "보은군", "옥천군", "영동군", "증평군", "진천군", "괴산군", "음성군", "단양군" ],
          "충청남도" : [ "천안시 동남구", "천안시 서북구", "공주시", "보령시", "아산시", "서산시", "논산시", "계룡시", "당진시", "금산군", "부여군", "서천군", "청양군", "홍성군", "예산군", "태안군" ],
          "대전광역시" : [ "대덕구", "동구", "서구", "유성구", "중구" ],
          "세종특별자치시" : [ "세종특별자치시" ],    
          "전라북도" : [ "전주시 완산구", "전주시 덕진구", "군산시", "익산시", "정읍시", "남원시", "김제시", "완주군", "진안군", "무주군", "장수군", "임실군", "순창군", "고창군", "부안군" ],
          "전라남도" : [ "목포시", "여수시", "순천시", "나주시", "광양시", "담양군", "곡성군", "구례군", "고흥군", "보성군", "화순군", "장흥군", "강진군", "해남군", "영암군", "무안군", "함평군", "영광군", "장성군", "완도군", "진도군", "신안군" ],
          "광주광역시" : [ "광산구", "남구", "동구", "북구", "서구" ],
          "경상북도" : [ "포항시 남구", "포항시 북구", "경주시", "김천시", "안동시", "구미시", "영주시", "영천시", "상주시", "문경시", "경산시", "군위군", "의성군", "청송군", "영양군", "영덕군", "청도군", "고령군", "성주군", "칠곡군", "예천군", "봉화군", "울진군", "울릉군" ],
          "경상남도" : [ "창원시 의창구", "창원시 성산구", "창원시 마산합포구", "창원시 마산회원구", "창원시 진해구", "진주시", "통영시", "사천시", "김해시", "밀양시", "거제시", "양산시", "의령군", "함안군", "창녕군", "고성군", "남해군", "하동군", "산청군", "함양군", "거창군", "합천군" ],
          "부산광역시" : [ "강서구", "금정구", "남구", "동구", "동래구", "부산진구", "북구", "사상구", "사하구", "서구", "수영구", "연제구", "영도구", "중구", "해운대구", "기장군" ],
          "대구광역시" : [ "남구", "달서구", "동구", "북구", "서구", "수성구", "중구", "달성군" ],
          "울산광역시" : [ "남구", "동구", "북구", "중구", "울주군" ],
          "제주특별자치도" : [ "서귀포시", "제주시" ],
  });

  const selected = function(event) {
    select_area.value = event.target.value
    list_city.value = area.value[event.target.value]
  }
  
  
  /* global kakao */
  
  const location =ref('')
  const bank = ref('bank')
  const loadScript =function() {
    const script = document.createElement('script')
    // 동적 로딩을 위해서 autoload=false 추가
    script.src = `https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=8d2a6579e21785248893d93db12118c8&libraries=services,clusterer,drawing`
    // kakaomap script loading 후 initMap 실행
    script.onload = () => kakao.maps.load(initMap)
    document.head.appendChild(script)
  }
  
  let map = null
  const container = ref(null)
  const initMap = () => {
    const options = {
      center: new kakao.maps.LatLng(36.3504119, 127.3845475), // 대전
      level: 6
    }
    map = new kakao.maps.Map(container.value, options)
    infowindow.value = new kakao.maps.InfoWindow({ zIndex: 1 })
  }
  
  onMounted(() => {
    if (window.kakao?.maps) {
      initMap()
    } else {
      loadScript()
    }
  })
  
  const search = function() {
      let places = new kakao.maps.services.Places(map)
      places.keywordSearch(`${select_sido.value}${bank.value}${select_area.value}`, placesSearchCB) 
      location.value = ''
      bank.value = ''
  }
  
  
  // 키워드 검색 완료 시 호출되는 콜백함수 입니다
  function placesSearchCB (data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
          // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
          // LatLngBounds 객체에 좌표를 추가합니다
          var bounds = new kakao.maps.LatLngBounds();
          for (var i=0; i<data.length; i++) {
              displayMarker(data[i]);    
              bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
          }       
          // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
          map.setBounds(bounds);
      } 
  }
  
  // const  infowindow = ref(kakao.maps.InfoWindow({zIndex:1}))
  // 지도에 마커를 표시하는 함수입니다
  function displayMarker(place) {
      // 마커를 생성하고 지도에 표시합니다
      var marker = new kakao.maps.Marker({
          map: map,
          position: new kakao.maps.LatLng(place.y, place.x) 
      });
      // 마커에 클릭이벤트를 등록합니다
      kakao.maps.event.addListener(marker, 'click', function() {
          // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
          infowindow.value.setContent('<div style="font-size: 12px; padding: 4px;">' + place.place_name + '</div>'); 
          infowindow.value.open(map, marker);
          console.log(infowindow.value.a.innerText)
      })
  }
</script>


 <style scoped >
 .box{
     
 }
 .wrapper {
     margin-left: auto;
     margin-right: auto;
     width: 80%;
     height: 500px;    
 }
 .first{
     margin-top: 5px;
     width: 78%;
     height: 480px;
     margin-left: auto;
     margin-right: auto;
   }
 
 .tag{
   font-size: 10px;
   display: inline-block;
   margin-left: 20px;
 }
 .bank {
   margin-left: 20px;
 }

 .select-list {
   display: flex;
   flex-direction: row;
   justify-content: center;
   align-items: center; /* 중앙 정렬을 위해 추가 */
 }

 .select-list select {
   width: 200px;
   height: 50px;
   margin: 30px 10px;
 }

 .select-list button {
   width: 80px;
   height: 50px; /* 선택한 높이에 맞게 조절 */
   margin: 30px 10px; /* 간격 조절 */
 }
 </style>