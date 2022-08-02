from django.urls import path
from . import views as calulate_views


urlpatterns = [
    path('rectangle/<int:width>/<int:height>', calulate_views.rectangle, name='rectangle'),
    path('square/<int:width>', calulate_views.square, name='square'),
    path('circle/<int:radius>', calulate_views.circle, name='circle'),
    path('get_rectangle_area/<int:width>/<int:height>', calulate_views.get_rectangle_area),
    path('get_square_area/<int:width>', calulate_views.get_square_area),
    path('get_circle_area/<int:radius>', calulate_views.get_circle_area),
]