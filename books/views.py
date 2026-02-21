from django.shortcuts import render, redirect
from django.http import HttpResponse

from books.forms import BookForm
from books.models import Book
from django.http.request import HttpRequest

# Create your views here.

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


def hello_world(request: HttpRequest):
    return render(request, "books/home.html")

def simple_endpoint(request: HttpRequest):
    return HttpResponse("{ 'content': 'Hello this is my response to your request'}", status=202)
