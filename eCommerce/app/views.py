from django.db.models import Count
from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views import View
from . models import Product
from . forms import CustomerRegistrationForm
from django.contrib import messages

#Django Views are python functions that takes http request and returns http response, like HTML documents.

#render a page using a function
def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")



#render a page using a class-method based
class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())


class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'app/category.html', locals())


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! User Register Successfully')
        else:
            messages.warning(request, 'Invalid Input Data')
        return render(request, 'app/customerregistration.html', locals())



class ProfileView(View):
    def get(self, request):
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        return render(request, 'app/profile.html', locals())
