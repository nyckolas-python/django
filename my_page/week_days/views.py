from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_day_by_number(request, day: int):
    if 1 <= day <= len(day_list):
        day_name = day_list[day-1]
        redirect_urls = reverse('todo_week', args=(day_name, ))
        return HttpResponseRedirect(redirect_urls)
    else:
        return HttpResponseNotFound(f"I don't know such a day of the week number - {day}")


def get_day_name(request, day: str):
    if day.lower() in day_list:
        # return (f"Today is a beautiful day - {day.capitalize()}")
        return render(request, 'week_days/greeting.html')
    else:
        return HttpResponseNotFound(f"I don't know such a day of the week.")