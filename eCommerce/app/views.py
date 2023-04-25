from django.db.models import Count
from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views import View
from . models import Product
# Create your views here.

#render a page using a function
def home(request):
    return render(request, "app/home.html")


#render a page using a class
class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', locals())