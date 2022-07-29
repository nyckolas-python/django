from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def leo(request):
    return HttpResponse("Zodiac sign - Leo")

def scorpio(request):
    return HttpResponse("Zodiac sign - Scorpio")

def aquarius(request):
    return HttpResponse("Zodiac sign - Aquarius")
