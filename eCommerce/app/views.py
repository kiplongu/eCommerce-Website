from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views import View

# Create your views here.

#render a page using a function
def home(request):
    return render(request, "app/home.html")


#render a page using a class
class CategoryView(View):
    def get(self, request, val):
        return render(request, 'app/category.html', locals())