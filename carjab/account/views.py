from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def login(request):
    return HttpResponse("로그인")


@api_view(['POST'])
def signup(request):
    data = {
        'message':"회원가입완료"
    }

    return Response(data=data)