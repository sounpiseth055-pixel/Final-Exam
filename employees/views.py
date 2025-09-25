from django.shortcuts import render,redirect
from . models import Employee
from .forms import EmployeeEditForm,EmployeeAddForm
from users.decorators import user_login_required

@user_login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request,"employee/employee_list.html",{"employees":employees})
@user_login_required
def employee_add(request):
    form = EmployeeAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request,"employee/employee_add.html",{"form":form})
@user_login_required
def employee_edit(request, pk):
    employees= Employee.objects.filter(pk = pk).first()
    form = EmployeeEditForm(request.POST or None,instance=employees)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request,"employee/employee_edit.html",{"form":form})
@user_login_required
def employee_deleted(request,pk):
    employee = Employee.objects.filter(pk = pk).first()
    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")
    return render(request,"employee/employee_delete.html",{"employee":employee})