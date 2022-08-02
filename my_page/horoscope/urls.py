from django.urls import path
from . import views as views_horoscope


urlpatterns = [
    path('', views_horoscope.index),
    path('type/', views_horoscope.get_type, name='type/'),
    path('type/<str:type_name>', views_horoscope.get_type_names, name='type-name'),
    path('<int:sign_zodiac>/', views_horoscope.get_zodiac_by_number),
    path('<str:sign_zodiac>/', views_horoscope.get_zodiac, name='horoscope-name'),
]