from django.shortcuts import render
from django.urls import reverse
from library.models import User, Book
from library.serializers import UserSerializer, BookSerializer
from .forms import NewUserForm, AddBookForm
from django.http import HttpResponseRedirect
#rest
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


class ListAddUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'test/readers.html'

    def get(self, request):
        readers = User.objects.all()
        form = NewUserForm()
        return Response({'readers': readers, 'form': form})

    def post(self, request):
        readers = User.objects.all()
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form, 'readers': readers}
        return render (request, 'test/readers.html', context)


class UserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'test/reader.html'

    def get(self, request, reader_id):
        reader = User.objects.get(id=reader_id)
        books = reader.book_set.all()
        form = AddBookForm()
        return Response({'reader': reader, 'books': books, 'form': form})

    def post(self, request, reader_id):
        reader = User.objects.get(id=reader_id)
        books = reader.book_set.all()
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form, 'books': books, 'reader': reader}
        return render (request, 'test/reader.html', context)


class EditBookDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'test/edit_book.html'

    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        reader = book.owner
        form = AddBookForm(instance=book)
        return Response({'form': form, 'book': book})

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        form = AddBookForm(instance=book, data=request.POST)
        reader = book.owner
        #reader = Reader.objects.get(id=reader_id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reader', args=[reader.id]))
        context = {'book': book, 'form': form, 'reader': reader}
        return render(request, 'test/edit_book.html', context)


# rest API views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
