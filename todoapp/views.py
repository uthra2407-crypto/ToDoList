from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def home(request):
    t=Task.objects.filter(is_completed=False)
    context ={
        't':t,
    }
    return render(request,'home.html',context)

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('/')
    # return HttpResponse("The task was updated......")