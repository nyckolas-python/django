from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<str:slug_movie>', views.show_one_movie, name='movie_detail'),

]
