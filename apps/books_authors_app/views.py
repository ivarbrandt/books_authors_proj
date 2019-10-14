from django.shortcuts import render, HttpResponse, redirect
from . models import Book, Author

# Create your views here.

def index(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

def addbook(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['des'])
    return redirect('/')

def booksmain(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': Book.objects.get(id=id),
        'bookauthors': book.authors.all(),
        'authors': Author.objects.all()
    }
    return render(request, 'books_authors_app/bookdes.html', context)

def addauthortobook(request, id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(id=request.POST["authors"])
    book.authors.add(author)
    return redirect('/')

def authormain(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books_authors_app/author.html', context)

def addauthor(request):
    Author.objects.create(first_name=request.POST['fir_name'], last_name=request.POST['las_name'], notes=request.POST['notes'])
    return redirect('/authors')

def authordes(request, id):
    author = Author.objects.get(id=id)
    context = {
        'author': Author.objects.get(id=id),
        'authorbooks': author.books.all(),
        'allbooks': Book.objects.all()
    }
    return render(request, 'books_authors_app/authordes.html', context)

def addbooktoauthor(request, id):
    author = Author.objects.get(id=id)
    book = Book.objects.get(id=request.POST["books"])
    author.books.add(book)
    return redirect('/authors')