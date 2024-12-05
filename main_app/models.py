from django.db import models
from django.urls import reverse

# Create your models here.
RATINGS = (
    ('5', '★★★★★'),
    ('4', '★★★★'),
    ('3', '★★★'),
    ('2', '★★'),
    ('1', '★'),
)



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
    
class Rating(models.Model):
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0]
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.name} is a {self.get_rating_display()}"

class Note(models.Model):
    date = models.DateField()
    comment = models.TextField(max_length=250)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment #{self.id} for {self.book.name}"