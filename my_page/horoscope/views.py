from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass


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

types_dict = {
    'fire': ['aries', 'taurus', 'gemini'],
    'earth': ['cancer', 'leo', 'virgio'],
    'air': ['libra', 'scorpio', 'sagittarius'],
    'water': ['capricorn', 'aquarius', 'pisces']
}


def index(request):
    zodiac_list = list(zodiac_dict)
    context = {
        'zodiac_list': zodiac_list,
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'horoscope/index.html', context=context)


def get_type(request):
    types_list = list(types_dict)
    li_elements = ''
    for type_name in types_list:
        redirect_path = reverse('horoscope-type-name', args=(type_name, ))
        li_elements += f"<li> <a href='{redirect_path}'>{type_name.title()}</a> </li>"

    response = f"<ul> {li_elements} </ul>"
    return HttpResponse(response)


def get_type_names(request, type_name: str):
    zodiac_list = types_dict.get(type_name, None)
    if zodiac_list:
        li_elements = ''
        for sign in zodiac_list:
            redirect_path = reverse('horoscope-name', args=(sign, ))
            li_elements += f"<li> <a href='{redirect_path}'>{sign.title()}</a> </li>"

        response = f"<ul> {li_elements} </ul>"
        return HttpResponse(response)
    else:
        redirect_url = reverse('horoscope-type')
        return HttpResponseRedirect(f"{redirect_url}")


def get_zodiac_by_number(request, sign_zodiac: int):
    zodiac_list = list(zodiac_dict)
    if sign_zodiac < len(zodiac_list):
        name_zodiac = zodiac_list[sign_zodiac-1]
        redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
        return HttpResponseRedirect(f"{redirect_url}")
    else:
        return HttpResponseNotFound(f"There is no such zodiac sign number - {sign_zodiac}")

@dataclass
class Person():
    name: str
    age: int
    def __str__(self) -> str:
        return f"This is {self.name}"

def get_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    data = {
        'description_data': description,
        'sign': sign_zodiac.title(),
        'zodiac_list': list(zodiac_dict)
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)
