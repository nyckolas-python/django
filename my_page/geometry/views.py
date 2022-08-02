from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi
from django.urls import reverse

def get_rectangle_area(request, width: int, height: int):
    redirect_url = reverse('rectangle', args=(width, height))
    return HttpResponseRedirect(redirect_url)

def get_square_area(request, width: int):
    redirect_url = reverse('square', args=(width, ))
    return HttpResponseRedirect(redirect_url)

def get_circle_area(request, radius: int):
    redirect_url = reverse('circle', args=(radius, ))
    return HttpResponseRedirect(redirect_url)

def rectangle(request, width: int, height: int):
    return HttpResponse(f"The area of the rectangle {width}x{height} is equal - {width*height}")

def square(request, width: int):
    return HttpResponse(f"The area of the square {width}x{width} is equal - {width**2}")

def circle(request, radius: int):
    return HttpResponse(f"The area of the circle with radius {radius} is equal - {pi*radius**2}")