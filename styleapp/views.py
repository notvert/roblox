from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
# from .models import Champions, PlayerRecord, MatchData
from rest_framework import status
from rest_framework.response import Response
import requests
import json

def index(request):
    return render(request, 'styleapp/index.html')

# def myview(request):
#     return HttpResponse('hello world!')