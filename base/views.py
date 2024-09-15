from django.shortcuts import render



def home(request):
    return render(request, 'base/home.html')


def book(request):
    return render(request, 'base/book.html')
    