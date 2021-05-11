from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import EmployeeForm
from.models import Employee


# Create your views here.

def welcome(request):
    return HttpResponse('<h1> Hii.......!!!!!!!!!!!</h1>')

# Function Based views----------------------------------------------------

def create_view(request):
    form=EmployeeForm()
    print('----data filled----')
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        print('DATA SAVED IN DATABASE')
        if form.is_valid():
            form.save()
            return redirect('/fcvApp/list')
    return render(request,'testApp/form.html',{'form':form})

def list_view(request):
    data=Employee.objects.all()
    return render(request,'testApp/list.html',{'data':data})

def Detail_view(request,id):
    record=Employee.objects.get(id=id)
    return render(request,'testApp/detail.html',{'record':record})

def update_view(request,id):
    list=Employee.objects.get(id=id)
    if request.method=='POST':
        ulist=EmployeeForm(request.POST,instance=list)
        if ulist.is_valid():
            ulist.save()
            return redirect('/fcvApp/list')
    return render(request,'testApp/update.html',{'list':list})

def delete_view(request,id):
    data=Employee.objects.get(id=id)
    data.delete()
    return redirect('/fcvApp/list')


# Class based views ----------------------------------------------------

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.urls import reverse

class List_view(ListView):
    model = Employee
    template_name = 'testApp/employee_list.html'

class Detail_views(DetailView):
    model = Employee
    template_name = 'testApp/employee_detail.html'

class Create_view(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'testApp/employee_form.html'
    success_url = '/fcvApp/listC/'

class Update_view(UpdateView):
    model = Employee
    fields = ('name','add')
    template_name = 'testApp/employee_form.html'
    #success_url = '/fcvApp/listC/'

class Delete_view(DeleteView):
    model = Employee
    template_name = 'testApp/employee_confirm_delete.html'
    success_url = '/fcvApp,listC'
