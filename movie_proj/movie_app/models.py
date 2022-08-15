from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


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
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    currency = models.CharField(
        default=USD, max_length=3, choices=CURRENCY_CHOICES)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.rating}%"

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])
