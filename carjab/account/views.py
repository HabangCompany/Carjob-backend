from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# 직렬화 API
from rest_framework import viewsets ,status
from .serializers import LoginSerializer, UserSerializers, StoreRegister
from .models import User
import json


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def signup(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def store_register(request):
    print(request)
    print(request.data)



@api_view(['GET'])
def idCheck(request):
    username = request.GET.get('username')
    if username is not None:
        user = User.objects.filter(username=username)
        if user.exists():
            return Response({"message": "이미 존재하는 아이디입니다."}, status=400)
        else:
            return Response({"message": "사용 가능한 아이디입니다."}, status=200)
    else:
        return Response({"message": "아이디를 입력해주세요."}, status=400)
    
@api_view(['GET'])
def nicknameCheck(request):
    nickname = request.GET.get('nickname')
    if nickname is not None:
        user = User.objects.filter(nickname=nickname)
        if user.exists():
            return Response({"message": "이미 존재하는 닉네임 입니다."}, status=400)
        else:
            return Response({"message": "사용 가능한 닉네임 입니다."}, status=200)
    else:
        return Response({"message": "닉네임을 입력해주세요."}, status=400)
#업체등록
@api_view(['POST'])
def store_register(request):
    res = request.data
    print(res)
    serializer = StoreRegister(data =res ,  context ={'request' : request})
    if serializer.is_valid() :
        return Response("됬음")
    else:
        return Response("ㄴㄴ" , status=400)
    # serializer = StoreRegister(data = request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.validated_data, status=status.HTTP_200_OK)
    # else:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)