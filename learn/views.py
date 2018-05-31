from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello1(request):
    return render(request, 'hello.html')


def hello(requst):
    return HttpResponse('你好，世界！')
