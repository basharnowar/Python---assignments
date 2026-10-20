from django.shortcuts import render, redirect
from .models import Author, Book
# Create your views here.
def books(request):
    context = {
        "all_books": Book.objects.all()
    }
 
    # if request.method == 'POST':
    #     Book.objects.create(
    #         title = request.POST['title'],
    #         desc = request.POST['desc']
    #     )
    #     return redirect('/books')
    return render(request, 'books.html', context)

    
def show_books(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        author_id = request.POST['author_id']
        author = Author.objects.get(id=author_id)
        book.authors.add(author)
        return redirect(f'/books/{book_id}')
    context = {
        'book': book,
        'all_authors': Author.objects.all()
    }
    return render(request, 'show_book.html', context)

def home(request):
    return render(request, "books.html")

# def testing_func(request):
#     Book.objects.create(
#         title = request.POST['title'],
#         desc = request.POST['desc']
#     )
#     return redirect('/books')

def create_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')





# Create your views here.
def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
 
    # if request.method == 'POST':
    #     Book.objects.create(
    #         title = request.POST['title'],
    #         desc = request.POST['desc']
    #     )
    #     return redirect('/books')
    return render(request, 'authors.html', context)

    
def show_authors(request, author_id):
    author = Author.objects.get(id=author_id)

    if request.method == 'POST':
        book = Book.objects.get(id=request.POST['book_id'])
        author.books.add(book)
        return redirect(f'/authors{author_id}')
    
    context = {
            'book': author,
            'all_books': Book.objects.all()
    }
    return render(request, 'show_author.html', context)

def home(request):
    return render(request, "authors.html")

# def testing_func(request):
#     Book.objects.create(
#         title = request.POST['title'],
#         desc = request.POST['desc']
#     )
#     return redirect('/books')

# def create_author(request):
#     Author.objects.create(
#         first_name = request.POST.get('first_name',''),
#         last_name = request.POST.get('last_name','')
#     )
#     print(request.POST['first_name'],request.POST['last_name'])
#     return redirect('/author')

def create_author(request):
    if request.method == "POST":
        Author.objects.create(
            first_name = request.POST.get('first_name', ''),
            last_name = request.POST.get('last_name', ''),
            notes = request.POST.get('notes', '')
        )
        return redirect('/authors')
    
    # If it's a GET request, just go back to the authors page
    return redirect('/authors')

