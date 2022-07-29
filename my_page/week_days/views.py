from django.shortcuts import render
from django.http import HttpResponse


def get_day_name(request, day_name):
    day_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    if day_name.lower() in day_list:
        return HttpResponse(f"{day_name.capitalize()}")
    else:
        return HttpResponse(f"I don't know such a day of the week.")
