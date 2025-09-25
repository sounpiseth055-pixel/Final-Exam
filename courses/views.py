from django.shortcuts import render,redirect
from . models import Course
from .forms import CourseEditForm,CourseAddForm

def course_list(request):
    courses = Course.objects.all()
    return render(request,"course/course_list.html",{"courses":courses})

def course_add(request):
    form = CourseAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("course_list")
    return render(request,"course/course_add.html",{"form":form})

def course_edit(request, pk):
    course = Course.objects.filter(pk = pk).first()
    form = CourseEditForm(request.POST or None,instance=course)
    if form.is_valid():
        form.save()
        return redirect("course_list")
    return render(request,"course/course_edit.html",{"form":form})

def course_deleted(request,pk):
    course = Course.objects.filter(pk = pk).first()
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(request,"course/course_delete.html",{"course":course})