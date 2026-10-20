from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('books', views.books),
    path('books/<int:book_id>', views.show_books),
    # path('yousef', views.testing_func)
    path('emil', views.create_book),
    path('authors', views.authors),
    path('authors/<int:author_id>', views.show_authors),
    path('author', views.create_author),
    
]