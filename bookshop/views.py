from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Book
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AuthorSerializer, BookSerializer


# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    return HttpResponse(loader.get_template("pages/home.html").render(context={"pageName": "BOOKSHOP"}))

def all(request):
    return HttpResponse(loader.get_template('pages/all_books.html').render(context={"pageName": "All Books", "books": Book.objects.all()}, request=request))
