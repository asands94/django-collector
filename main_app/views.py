from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .forms import NoteForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    note_form = NoteForm()
    return render(request, 'books/detail.html', {
        'book': book, 'note_form': note_form
        })

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

def add_review(request, book_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.book_id = book_id
        new_review.save()
    return redirect('book-detail', book_id=book_id)