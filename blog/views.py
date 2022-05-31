from django.shortcuts import render

# Create your views here.

def new(request):
    return render(request, 'new.html')

def category(request):
    return render(request, 'category.html')