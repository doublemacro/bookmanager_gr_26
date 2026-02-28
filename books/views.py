from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from books.forms import BookForm
from books.models import Book
from django.http.request import HttpRequest

# Create your views here.
# CRUD Actions
# Create, Read, Update, Delete.

def book_list(request: HttpRequest):
    # accesam baza de date, extragem cartile, si le afisam pe pagina html.
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "books/home.html", context)

def create_book(request: HttpRequest):
    if request.method == "POST":
        # primim HTTP POST request cand se apasa pe butonul Save la create book.
        form = BookForm(request.POST)
        if form.is_valid():
            # aici se intampla salvarea in baza de date
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    context = {
        'form': form
    }
    return render(request, "books/book_form.html", context)

def delete_book(request: HttpRequest, pk: int):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    else:
        return render(request, "books/book_confirm_delete.html", { "book": book })

def update_book(request: HttpRequest, pk: int):
    # cartea care exista deja din baza de date
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        # request.POST = { "title": "Harry Potter1", "author": "Rowling" }
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(request, "books/book_form.html", {"form": form})

def check_book_count(request: HttpRequest):
    count = Book.objects.count()
    return HttpResponse(count, status=200)



def hello_world(request: HttpRequest):
    return render(request, "books/home.html")

def simple_endpoint(request: HttpRequest):
    return HttpResponse("{ 'content': 'Hello this is my response to your request'}", status=202)
