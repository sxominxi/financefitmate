from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
   user = request.user  # 현재 인증된 사용자
   data = request.data  # 업데이트할 사용자 정보

   # 요청된 데이터로 사용자 정보 업데이트
   if 'username' in data:
      user.username = data['username']
   if 'email' in data:
      user.email = data['email']
   if 'first_name' in data:
      user.first_name = data['first_name']
   if 'last_name' in data:
      user.last_name = data['last_name']

   if 'nickname' in data:
      user.nickname = data['nickname']
   if 'age' in data:
      user.age = data['age']
   if 'money' in data:
      user.money = data['money']
   if 'salary' in data:
      user.salary = data['salary']

   user.save()  # 변경 사항 저장

   return Response({'message': '사용자 정보가 업데이트 되었습니다.'}, status=status.HTTP_200_OK)
