from django.shortcuts import redirect, render
from .models import Item
from django.contrib import messages
import os
# Create your views here.


def home(request):
    return render(request, 'home.html')

def index(request):
    products = Item.objects.all()
    context = {'products':products}
    return render(request, 'index.html', context)

def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')

        if len(request.FILES) != 0:
            abcd = request.FILES['image']
            prod.image = request.FILES['image']
            print(type(abcd))
        prod.save()

        messages.success(request, "Product Added Successfully")
        return redirect('/')
    return render(request, 'add.html')

def editProduct(request, pk):
    prod = Item.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']

        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')
        prod.save()

        messages.success(request, "Product Updated Successfully")
        return redirect('/')

    context = {'prod':prod}
    return render(request, 'edit.html', context)

def deleteProduct(request, pk):
    prod = Item.objects.get(id=pk)
    if len(prod.image) > 0:
        os.remove(prod.image.path)
    prod.delete()
    messages.success(request,"Product Deleted Successfuly")
    return redirect('/')


def Contact(request):
    return render(request,'contact.html')
    