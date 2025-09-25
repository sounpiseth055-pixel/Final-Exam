from django.shortcuts import render,redirect
from . models import Enrollment
from .forms import EnrollmentEditForm,EnrollmentAddForm

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request,"enrollment/enrollment_list.html",{"enrollments":enrollments})

def enrollment_add(request):
    form = EnrollmentAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("enrollment_list")
    return render(request,"enrollment/enrollment_add.html",{"form":form})

def enrollment_edit(request, pk):
    enrollment = Enrollment.objects.filter(pk = pk).first()
    form = EnrollmentEditForm(request.POST or None,instance=enrollment)
    if form.is_valid():
        form.save()
        return redirect("enrollment_list")
    return render(request,"enrollment/enrollment_edit.html",{"form":form})

def enrollment_deleted(request,pk):
    enrollment = Enrollment.objects.filter(pk = pk).first()
    if request.method == "POST":
        enrollment.delete()
        return redirect("enrollment_list")
    return render(request,"enrollment/enrollment_delete.html",{"enrollment":enrollment})