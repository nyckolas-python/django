from locale import currency
from django.contrib import admin
from django.db.models import QuerySet

from .models import Movie, Director, Actor, DressingRoom
# Register your models here.

class RatingFilter(admin.SimpleListFilter):
    title = 'Свой фильтр рейтинга'
    parameter_name = 'rating'
    
    def lookups(self, request, model_admin):
        return [
            ('>40', 'Низкий'),
            ('от 40 до 69', 'Средний'),
            ('от 70 до 79', 'Высокий'),
            ('от 80 и выше', 'Высочайший'),            
        ]
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '>40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 69':
            return queryset.filter(rating__gte=40).filter(rating__lt=70)
        if self.value() =='от 70 до 79':
            return queryset.filter(rating__gte=70).filter(rating__lt=80)
        if self.value() == 'от 80 и выше':
            return queryset.filter(rating__gte=80)
        return queryset


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'room', 'actor']

@admin.register(Director)
class DirectorsAdmin(admin.ModelAdmin):
    pass

@admin.register(Actor)
class ActorsAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating', 'year', 'budget', 'currency'] # поля отображаются в карточке
    # exclude = ['slug'] # поля которые не отображаются в карточке Модели.
    # readonly_fields = ['rating'] # поля, которые нельзя изменить.
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'year', 'budget', 'director', 'rating_status']
    list_editable = ['rating', 'year', 'budget', 'director']
    ordering =['-rating', 'name']
    list_per_page = 3
    actions = ['set_dollars']
    search_fields = ['name', 'rating']
    list_filter = ['name', RatingFilter, 'director']
    filter_horizontal = ['actors']
    
    
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

    