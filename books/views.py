from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.
#def hello_jasmine (request):
    #return "Hello Jasmine!"
    #return HttpResponse ("Hello Jasmine!")

def books_home(request):
    return render(request, template_name="books_home.html", context={"books": books})

books = [
    {"id": 1, "name": "Caraval", "price": 250, "author": "Stephanie Garber", "pages": 407, "image": "pic1.jpg"},
    {"id": 2, "name": "Legendary", "price": 250, "author": "Stephanie Garber", "pages": 451, "image": "pic2.jpg"},
    {"id": 3, "name": "Finale", "price": 250, "author": "Stephanie Garber", "pages": 468, "image": "pic3.jpg"},
]


def index(request):
    return render(request, template_name="index.html", context={"books": books})

def profile(request, id):
    filtered_books = filter(lambda book: book['id'] == id, books)
    filtered_books = list(filtered_books)
    if filtered_books:
        return render(request, template_name='book_profile.html', context={"book": filtered_books[0]})
    return HttpResponse("Book not found. Please try again.")

def landing(request):
    return render(request, template_name="landing.html", context={"books": books})

def book_show(request, id):
    books = Book.objects.get(id=id)
    return render (request, 'books/show.html', context={"books":books}),

def create_book(request):
    return render(request,'books/create.html'),