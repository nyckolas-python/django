from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from math import pi

def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f"The area of the rectangle {width}x{height} is equal - {width*height}")

def get_square_area(request, width: int):
    return HttpResponse(f"The area of the square {width}x{width} is equal - {width**2}")

def get_circle_area(request, radius: int):
    return HttpResponse(f"The area of the circle with radius {radius} is equal - {pi*radius**2}")