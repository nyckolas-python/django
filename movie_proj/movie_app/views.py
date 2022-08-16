from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Avg, Count, Value

# Create your views here.
from .models import Movie, Director, Actor


def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors,
        })

def show_one_actor(request, id_actor: int):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor
    })


def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors,
        })

def show_one_director(request, id_director: int):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })
    

def show_all_movies(request):
    # movies = Movie.objects.order_by(F('year').desc(nulls_last=True), '-rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('Hello Django'),
        int_field=Value(1234567890),
        new_budget=F('budget')+100999,     
        
    ).annotate(rating_plus_year=F('rating')+F('year'),)

    agg = movies.aggregate(Avg('budget'), Max(
        'rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
      		'agg': agg,
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })
