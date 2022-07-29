from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('leo/', views_horoscope.leo),
    path('scorpio/', views_horoscope.scorpio),
    path('aquarius/', views_horoscope.aquarius),
    path('taurus/', views_horoscope.taurus),
    path('aries/', views_horoscope.aries),
    
]