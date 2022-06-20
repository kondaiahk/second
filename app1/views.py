from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hai(request):
    return HttpResponse('this is hai function of app1 views')
