from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
# 직렬화 API
from rest_framework import viewsets ,status
from .serializers import UserSerializers
from .models import User

@api_view(['GET'])
def login(request):
    return HttpResponse("로그인")


@api_view(['POST'])
def signup(request):
    print("회원가입요청이들어왔습니다")
    print(request.data)
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

