from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi

def get_rectangle_area(request, width: int, height: int):
    return HttpResponseRedirect(f"/calculate_geometry/rectangle/{width}/{height}")

def get_square_area(request, width: int):
    return HttpResponseRedirect(f"/calculate_geometry/square/{width}/{width}")

def get_circle_area(request, radius: int):
    return HttpResponseRedirect(f"/calculate_geometry/circle/{radius}")

def rectangle(request, width: int, height: int):
    return HttpResponse(f"The area of the rectangle {width}x{height} is equal - {width*height}")

def square(request, width: int):
    return HttpResponse(f"The area of the square {width}x{width} is equal - {width**2}")

def circle(request, radius: int):
    return HttpResponse(f"The area of the circle with radius {radius} is equal - {pi*radius**2}")