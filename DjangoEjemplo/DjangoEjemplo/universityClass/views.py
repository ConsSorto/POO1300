from django.shortcuts import render, redirect
from .models import UniversityClass

# Create your views here.
def index(request):
    universityClass = UniversityClass.objects.all()

    return render(request, 'index.html', {'universityClass': universityClass})

def retrieve(request, id):
    singleClass = UniversityClass.objects.get(pk=id)
    return render(request, 'singleClass.html', {"singleClass": singleClass})

def create(request):

    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        department = request.POST['department']

        singleClass = UniversityClass(name=name, code=code, department=department)
        singleClass.save()

        return redirect('index')

    return render(request, 'create.html')

def edit(request, id):
    singleClass = UniversityClass.objects.get(pk=id)

    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        department = request.POST['department']

        singleClass.name = name
        singleClass.code = code
        singleClass.department = department
        singleClass.save()
        return redirect('index')

    return render(request, 'edit.html', {"singleClass": singleClass})


def delete(request, id):
    if request.method == 'POST':
        singleClass = UniversityClass.objects.get(pk=id)
        singleClass.delete()
        return redirect('index')