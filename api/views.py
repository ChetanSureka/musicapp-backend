from django.http import HttpResponse
from django.shortcuts import render

def HomeView(request):
    return HttpResponse("<h3>This is a front page...</h3>")