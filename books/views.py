from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book


class Home(TemplateView):
    template_name = 'home.html'


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'


@csrf_exempt
def test_file_process(request):
    if not request.method == 'POST':
        return HttpResponseBadRequest('Разрешены только POST запросы!')
    req_file: InMemoryUploadedFile = request.FILES.get('form')
    result_str = req_file.read()
    print(result_str)
    return HttpResponse(result_str)
    # with open('/destination/path/%s' % file.name, 'wb+') as dest:
    #     for chunk in file.chunks():
    #         dest.write(chunk)
    # return HttpResponse('File uploaded')
