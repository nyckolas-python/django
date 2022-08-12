from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()


    def __str__(self) -> str:
        return f"{self.title} - {self.rating}% - bestSeller - {self.is_best_selling}"