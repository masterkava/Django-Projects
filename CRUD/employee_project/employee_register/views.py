from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

# showing the list of employee
def employee_list(request):
    context = {'employee_list' : Employee.objects.all()} #inside Employee all the records are save those are inserted we are saving them into the variable
    return render(request, 'employee_register/employee_list.html', context)


# insert and update operation
def employee_form(request, id=0):
    if request.method == "GET":
        # identify insert or update operation
        if id==0: #means update form
            form = EmployeeForm()
        else: #here insert form is there
            employee = Employee.objects.get(pk=id) #pk=primary key
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html', {'form':form})
    else: #post req handled
        if id==0: #insert operation
            form = EmployeeForm(request.POST)
        else: #update operation
            employee = Employee.objects.get(pk=id) #pk=primary key this line gets data acc to id
            form = EmployeeForm(request.POST, instance=employee) #this line updates the data
        if form.is_valid():
            form.save() #this saves all the data inside the database
        return redirect(request, '/employee/list/')
        

# delete operation
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id) #pk=primary key this line gets data acc to id
    employee.delete()
    return redirect('/employee/list/')


