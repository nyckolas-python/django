from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Director(models.Model):
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    email = models.CharField(max_length=256, null=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDERS = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    ]
    first_name = models.CharField(max_length=128, null=False)
    last_name = models.CharField(max_length=128, null=False)
    gender = models.CharField(default=MALE, max_length=1, choices=GENDERS)

    def __str__(self) -> str:
        if self.gender == 'M':
            return f"Actor {self.first_name} {self.last_name}"
        else:
            return f"Actress {self.first_name} {self.last_name}"


class Movie(models.Model):

    EUR = 'EUR'
    USD = 'USD'
    UAH = 'UAH'

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (UAH, 'Hryvna'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    year = models.IntegerField(null=True)
    currency = models.CharField(
        default=USD, max_length=3, choices=CURRENCY_CHOICES)
    budget = models.IntegerField(
        default=1000000, validators=[MinValueValidator(1)])
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)

    # метод для заполнения поля при сохранении, например можно пройти цыклом все записи.
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} ({self.year})"

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])
