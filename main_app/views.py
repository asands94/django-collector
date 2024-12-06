from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .forms import CommentForm, RatingForm
from django.contrib.auth.views import LoginView


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    comment_form = CommentForm()
    rating_form = RatingForm()
    return render(request, 'books/detail.html', {
        'book': book, 'comment_form': comment_form, 'rating_form': rating_form
        })

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'image', 'author', 'description', 'year_published']

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

def add_note(request, book_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.book_id = book_id
        new_review.save()
    return redirect('book-detail', book_id=book_id)

def add_rating(request, book_id):
    form = RatingForm(request.POST)
    if form.is_valid():
        new_rating = form.save(commit=False)
        new_rating.book_id = book_id
        new_rating.save()
    return redirect('book-detail', book_id=book_id)