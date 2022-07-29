from django.urls import path
from . import views as views_horoscope


urlpatterns = [
    path('<int:sign_zodiac>/', views_horoscope.get_zodiac_by_number),
    path('<str:sign_zodiac>/', views_horoscope.get_zodiac),
]