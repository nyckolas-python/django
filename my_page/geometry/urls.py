from django.urls import path
from . import views as calulate_views


urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', calulate_views.get_rectangle_area),
    path('square/<int:width>/', calulate_views.get_square_area),
    path('circle/<int:radius>/', calulate_views.get_circle_area),

]