from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<str:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('directors/', views.show_all_directors),
    path('directors/<int:id_director>',
         views.show_one_director, name='director_detail'),
    path('actors/', views.show_all_actors),
    path('actors/<int:id_actor>', views.show_one_actor, name='actor_detail'),

]
