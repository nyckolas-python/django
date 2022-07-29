from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


zodiac_dict = {
    'aries': 'Zodiac sign - Aries is the first sign of the zodiac, the planet Mars (March 21 to April 20).',
    'taurus': 'Zodiac sign - Taurus is the second sign of the zodiac, the planet Venus (from April 21 to May 21).',
    'gemini': 'Zodiac sign - Gemini is the third sign of the zodiac, the planet Mercury (May 22 to June 21).',
    'cancer': 'Zodiac sign - Cancer is the fourth sign of the zodiac, the Moon (June 22 to July 22).',
    'leo': 'Zodiac sign - Leo is the fifth sign of the zodiac, the Sun (July 23 to August 21).',
    'virgio': 'Zodiac sign - Virgo is the sixth sign of the zodiac, the planet Mercury (August 22 to September 23).',
    'libra': 'Zodiac sign - Libra is the seventh sign of the zodiac, the planet Venus (September 24 to October 23).',
    'scorpio': 'Zodiac sign - Scorpio is the eighth sign of the zodiac, the planet Mars (October 24 to November 22).',
    'sagittarius': 'Zodiac sign - Sagittarius is the ninth sign of the zodiac, the planet Jupiter (November 23 to December 22).',
    'capricorn': 'Zodiac sign - Capricorn is the tenth sign of the zodiac, the planet Saturn (December 23 to January 20).',
    'aquarius': 'Zodiac sign - Aquarius is the eleventh sign of the zodiac, the planets Uranus and Saturn (January 21 to February 19).',
    'pisces': 'Zodiac sign - Pisces is the twelfth sign of the zodiac, the planet Jupiter (February 20 to March 20).',
}


def get_zodiac_by_number(request, sign_zodiac: int):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"It is not zodiac sign - {sign_zodiac}")
   
 
def get_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"It is not zodiac sign - {sign_zodiac}")