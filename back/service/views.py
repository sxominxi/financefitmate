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
    print(response)
    return JsonResponse(response, safe=False)

