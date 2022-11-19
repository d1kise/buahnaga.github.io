from django.shortcuts import render, redirect
from crud.forms import CarsForm
from crud.models import TableCars

# Create your views here.  
def index(request):

    context={
        'page_title':'Nama Kelompok',
    }

    return render(request, 'home/index.html',context)

def input(request):  
    if request.method == "POST":  
        form = CarsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CarsForm()  
    return render(request,'crud/input.html',{'form':form})  

def show(request):  
    cars = TableCars.objects.all()  
    return render(request,"crud/show.html",{'cars':cars})  

def edit(request, id):  
    cars = TableCars.objects.get(id=id)  
    return render(request,'crud/edit.html', {'cars':cars})  

def update(request, id):  
    cars = TableCars.objects.get(id=id)  
    form = CarsForm(request.POST, instance = cars)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'crud/edit.html', {'cars': cars})  

def destroy(request, id):  
    cars = TableCars.objects.get(id=id)  
    cars.delete()  
    return redirect("/show")