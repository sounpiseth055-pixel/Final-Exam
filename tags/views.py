from django.shortcuts import render,redirect
from . models import Tag
from .forms import TagEditForm,TagAddForm

def tag_list(request):
    tags = Tag.objects.all()
    return render(request,"tag/tag_list.html",{"tags":tags})

def tag_add(request):
    form = TagAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("tag_list")
    return render(request,"tag/tag_add.html",{"form":form})

def tag_edit(request, pk):
    tag = Tag.objects.filter(pk = pk).first()
    form = TagEditForm(request.POST or None,instance=tag)
    if form.is_valid():
        form.save()
        return redirect("tag_list")
    return render(request,"tag/tag_edit.html",{"form":form})

def tag_deleted(request,pk):
    tag = Tag.objects.filter(pk = pk).first()
    if request.method == "POST":
        tag.delete()
        return redirect("tag_list")
    return render(request,"tag/tag_delete.html",{"tag":tag})