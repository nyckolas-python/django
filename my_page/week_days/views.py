from django.shortcuts import render
from django.http import HttpResponse


def monday(request):
    return HttpResponse("Monday")

def tuesday(request):
    return HttpResponse("Tuesday")
