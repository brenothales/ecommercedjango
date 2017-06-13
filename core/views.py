from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    lorem = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quo dolor assumenda.', 'eligendi quasi quod dignissimos esse eum tempore reprehenderit totam. Fugiat esse a dolores unde temporibus vitae tenetur quas? Non' ]
    context = {
    'title': 'Django E-commerce',
    'texts': lorem
    }
    return render(request, "index.html", context)


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')


def product_list(request):
    return render(request, 'product_list.html')