from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
#def hello_jasmine (request):
    #return "Hello Jasmine!"
    #return HttpResponse ("Hello Jasmine!")

def books_home (request):
        return render(request,
                     template_name= "books_home.html",)

books = [
    {"id": 1, "name": "Caraval", "price":250,"author":"Stephanie Garber","pages":407, "image": "pic1.png"},
    {"id": 2, "name": "Legendary", "price":250,"author":"Stephanie Garber","pages":451, "image": "pic2.png"},
    {"id": 3, "name": "Finale", "price":250,"author":"Stephanie Garber","pages":468, "image": "pic3.png"},
]

def index(request):
    return HttpResponse(books)

def profile(request, id):
        filtered_books=filter(lambda book:book['id']==id,books)
        filtered_books=list(filtered_books)
        if filtered_books:
                 return render(request, 
                            template_name='bookStoreHome.html',
                            context={"book":filtered_books[0]})
        
        return HttpResponse("book not found, try again")
    
def landing(request):
        return render (request,
                     template_name ="landing.html",
                     context={"books":books})