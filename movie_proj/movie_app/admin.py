from django.contrib import admin
from .models import Movie
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'currency', 'rating_status']
    list_editable = ['rating', 'year', 'budget', 'currency']
    ordering =['-rating', 'name']
    list_per_page = 3
    
    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Даже не трать время!'
        if mov.rating < 70:
            return 'Разок можно глянуть!'
        if mov.rating <= 85:
            return 'Зачет!'

        return 'Топчик!'
    
# admin.site.register(Movie, MovieAdmin) # заменили на декоратор

    