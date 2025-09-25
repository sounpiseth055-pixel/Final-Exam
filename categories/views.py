from django.shortcuts import render,redirect
from . models import Category
from .forms import CategoryEditForm,CategoryAddForm

def category_list(request):
    categories = Category.objects.all()
    return render(request,"category/category_list.html",{"categories":categories})

def category_add(request):
    form = CategoryAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request,"category/category_add.html",{"form":form})

def category_edit(request, pk):
    category = Category.objects.filter(pk = pk).first()
    form = CategoryEditForm(request.POST or None,instance=category)
    if form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request,"category/category_edit.html",{"form":form})

def category_deleted(request,pk):
    category = category_deleted.objects.filter(pk = pk).first()
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    return render(request,"category/category_delete.html",{"category":category})