from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250, blank=True)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year_published = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.name}"
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'book_id': self.id})
