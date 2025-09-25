from django.shortcuts import render,redirect
from . models import Instructor
from .forms import InstructorEditForm,InstructorAddForm
from users.decorators import user_login_required
@user_login_required
def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request,"instructor/instructor_list.html",{"instructors":instructors})
@user_login_required
def instructor_add(request):
    form = InstructorAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("instructor_list")
    return render(request,"instructor/instructor_add.html",{"form":form})
@user_login_required
def instructor_edit(request, pk):
    instructor = Instructor.objects.filter(pk = pk).first()
    form = InstructorEditForm(request.POST or None,instance=instructor)
    if form.is_valid():
        form.save()
        return redirect("instructor_list")
    return render(request,"instructor/instructor_edit.html",{"form":form})
@user_login_required
def instructor_deleted(request,pk):
    instructor = Instructor.objects.filter(pk = pk).first()
    if request.method == "POST":
        instructor.delete()
        return redirect("instructor_list")
    return render(request,"instructor/instructor_delete.html",{"instructor":instructor})