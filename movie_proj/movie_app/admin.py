from locale import currency
from django.contrib import admin
from django.db.models import QuerySet

from .models import Movie
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'currency', 'rating_status']
    list_editable = ['rating', 'year', 'budget', 'currency']
    ordering =['-rating', 'name']
    list_per_page = 3
    actions = ['set_dollars']
    search_fields = ['name', 'rating']
    
    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Даже не трать время!'
        if mov.rating < 70:
            return 'Разок можно глянуть!'
        if mov.rating <= 85:
            return 'Зачет!'

        return 'Топчик!'
    
    @admin.action(description='Установить валюту в доллар.')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)
        
        
    
# admin.site.register(Movie, MovieAdmin) # заменили на декоратор @admin.register(Movie)

    