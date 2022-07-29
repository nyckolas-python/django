from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def leo(request):
    return HttpResponse("""Zodiac sign - Leo.</br>
                        Leo is the fifth sign of the zodiac, the Sun (July 23 to August 21).
                        """)

def scorpio(request):
    return HttpResponse("""Zodiac sign - Scorpio.</br>
                        Scorpio is the eighth sign of the zodiac, the planet Mars (October 24 to November 22).
                        """)

def aquarius(request):
    return HttpResponse("""Zodiac sign - Aquarius.</br>
                        Aquarius is the eleventh sign of the zodiac, the planets Uranus and Saturn (January 21 to February 19).
                        """)
def aries(request):
    return HttpResponse("""Zodiac sign - Aries.</br>
                        Aries is the first sign of the zodiac, the planet Mars (March 21 to April 20).
                        """)
def taurus(request):
    return HttpResponse("""Zodiac sign - Taurus.</br>
                        Taurus is the second sign of the zodiac, the planet Venus (from April 21 to May 21).
                        """)
