from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, InstallmentOptionsSerializer, InstallmentProductsSerializer
from .models import DepositProducts, InstallmentProducts
import requests
import json
from django.http import JsonResponse
from accounts.models import User
from accounts.serializers import CustomReadSerializer

api_key = 'f09a043ec54a3da97ecf32c4027e41b8'

@api_view(['GET'])
def index(request):
    # url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    return Response(response)


@api_view(['GET'])
def save_deposit_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    for li in response.get("result").get("baseList"):
        save_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'etc_note': li.get('etc_note'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'join_way': li.get('join_way'),
            'spcl_cnd': li.get('spcl_cnd'),
        }

        # 저장하기 위해 데이터를 포장
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # options ---------------------------------------------------------

    for option in response.get("result").get("optionList"):
        option_data = {
            'fin_prdt_cd': option.get('fin_prdt_cd'),    
            'intr_rate_type_nm': option.get('intr_rate_type_nm'),  
            'intr_rate': option.get('intr_rate'),                           
            'intr_rate2': option.get('intr_rate2'),                       
            'save_trm': option.get('save_trm'),   
        }

        product = get_object_or_404(DepositProducts, fin_prdt_cd=option.get('fin_prdt_cd'))
        serializer = DepositOptionsSerializer(data=option_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            
    # 저장완료 메세지
    return Response({ 'message': 'okay'})

# 정기예금 상품 목록 출력 & 데이터 삽입
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        data = {
            'message': '이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.'
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


# 정기 예금 상품 디테일
@api_view(['GET'])
def deposit_detail(request, deposit_pk):
    product = get_object_or_404(DepositProducts, pk=deposit_pk)
    serializer = DepositProductsSerializer(product)
    return Response(serializer.data)

# -----------------------------------------------------------------------------------------

# 정기 적금 데이터 저장
@api_view(['GET'])
def save_installment_savings_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    for li in response.get("result").get("baseList"):
        save_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'etc_note': li.get('etc_note'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'join_way': li.get('join_way'),
            'spcl_cnd': li.get('spcl_cnd'),
        }

        # 저장하기 위해 데이터를 포장
        serializer = InstallmentProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # options ---------------------------------------------------------

    for option in response.get("result").get("optionList"):
        option_data = {
            'fin_prdt_cd': option.get('fin_prdt_cd'),    
            'intr_rate_type_nm': option.get('intr_rate_type_nm'),  
            'intr_rate': option.get('intr_rate'),                           
            'intr_rate2': option.get('intr_rate2'),                       
            'save_trm': option.get('save_trm'),
            'rsrv_type_nm': option.get('rsrv_type_nm'),   
        }

        product = get_object_or_404(InstallmentProducts, fin_prdt_cd=option.get('fin_prdt_cd'))
        serializer = InstallmentOptionsSerializer(data=option_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            
    # 저장완료 메세지
    return Response({ 'message': 'okay'})


# 적금 상품 목록 출력 & 데이터 삽입
@api_view(['GET', 'POST'])
def installment_savings_products(request):
    if request.method == 'GET':
        products = InstallmentProducts.objects.all()
        serializer = InstallmentProductsSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstallmentProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        data = {
            'message': '이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.'
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
# 정기 적금 상품 디테일
@api_view(['GET'])
def installment_detail(request, installment_pk):
    product = get_object_or_404(InstallmentProducts, pk=installment_pk)
    serializer = InstallmentProductsSerializer(product)
    return Response(serializer.data)

# ---------------------------------------------------------------------------------------------

# 환율 계산기
def exchange(request):
    API_KEY = 'DBAH4dbneY14sHfaMcBHfx0eJ7AM8lkN'
    URL = f' https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&searchdate=20180102&data=AP01'
    response = requests.get(URL).json()
    return JsonResponse(response, safe=False)

# ---------------------------------------------------------------------------------------------

# 상품 추천 서비스
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from collections import Counter

@api_view(['GET'])
def recommend(request):
    user_data = User.objects.exclude(pk=request.user.pk).values('id', 'age', 'money', 'salary')
    user_info = User.objects.get(pk=request.user.pk)

    # 각 유저 간의 유사성 측정 (나이, 보유 자산, 연봉 기준) -> 3차원 그래프 형태로 변경 후 거리 계산 
    user_similarity = {}
    for data in user_data:
        user_vector = np.array([data['age'], data['money'], data['salary']])
        new_user_vector = np.array([user_info.age, user_info.money, user_info.salary])
        distance = euclidean_distances([user_vector], [new_user_vector])[0][0]
        user_similarity[data['id']] = distance

    # 유사도를 기준으로 오름차순 정렬
    sorted_users = sorted(user_similarity.items(), key=lambda x: x[1])

    # 상위 10명의 유저를 선택
    top_users = sorted_users[:10]

    # 선택된 유저들의 상품 조회
    recommended_products = []
    for user_id, distance in top_users:
        # 상품 리스트가 , 형태로 저장되어 있어서 split 을 통해 분해
        user_products = User.objects.get(pk=user_id).financial_products.split(',')
        recommended_products.extend(user_products)

   # 각 상품의 등장 횟수를 계산
    product_counter = Counter(recommended_products)

    # 중복 상품을 제거하고 등장 횟수를 기준으로 내림차순으로 정렬
    sorted_products = sorted(product_counter.items(), key=lambda x: x[1], reverse=True)

    # 공백이 아닌 상품만 선택하여 추천 리스트로 만듦
    recommended_products = [product for product, _ in sorted_products if product.strip()]

    return Response(recommended_products)