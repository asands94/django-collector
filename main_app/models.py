from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    year_published = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.name}"
