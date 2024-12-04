from django.shortcuts import render

class Book:
    def __init__(self, name, image, author, description, year_published):
        self.name = name
        self.image = image
        self.author = author
        self.description = description
        self.year_published = year_published

books = [
    Book('A Dowry of Blood', 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1663707732l/60521937.jpg', 'S.T. Gibson', 'A dark and delicious story of Dracula and his first bride, Constanta, spread across centuries.', 2001),
    Book('House of Hunger', 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1649092164l/60052118.jpg', 'Alexis Henderson', 'A sapphic gothic horror novel that follows Marion Shaw who has spent her life in the slums.', 2022 ),
    Book('The Marionettes', 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1625148276i/57235694.jpg', 'Katie Wismer', 'Valerie Darkmore\'s entire life has been building up to this moment-her initiation into the Marionettes, the prestigious league of witches sworn to serve the vampires.' , 2021),
    Book('Twilight', 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1700522826i/41865.jpg' , 'Stephenie Meyer', 'Seventeen-year-old Isabella "Bella" Swam moves from Phoenix, Arizona to Forks, Washington.',2005)
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def book_index(request):
    return render(request, 'books/index.html', {'books': books})

