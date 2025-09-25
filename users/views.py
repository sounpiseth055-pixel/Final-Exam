from django.shortcuts import render,redirect
from . models import User
from .forms import UserEditForm,UserAddForm

def user_list(request):
    users = User.objects.all()
    return render(request,"user/user_list.html",{"users":users})

def user_add(request):
    form = UserAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("user_list")
    return render(request,"user/user_add.html",{"form":form})

def user_edit(request, pk):
    user = User.objects.filter(pk = pk).first()
    form = UserEditForm(request.POST or None,instance=user)
    if form.is_valid():
        form.save()
        return redirect("user_list")
    return render(request,"user/user_edit.html",{"form":form})

def user_deleted(request,pk):
    user = User.objects.filter(pk = pk).first()
    if request.method == "POST":
        user.delete()
        return redirect("user_list")
    return render(request,"user/user_delete.html",{"user":user})