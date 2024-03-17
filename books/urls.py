from django.urls import path
from .views import books_home, index, profile,landing, create_book

urlpatterns = [
    path('home', books_home, name='books_home'),
    path('', index, name='bookstore_index'),
    path('<int:id>', profile, name='bookstore_profile'),
    path('land/',landing,name="bookstore_land"),
    path('create', create_book, name='book.create'),
]