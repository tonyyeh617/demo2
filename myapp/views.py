from django.shortcuts import render
from django.http import HttpResponse

def testweb1(request):
    return HttpResponse("This is another test web page.")

