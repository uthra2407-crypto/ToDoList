from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def home(request):
    t=Task.objects.filter(is_completed=False)
    c_t=Task.objects.filter(is_completed=True)
    print(c_t)
    context ={
        't':t,
        'c_t':c_t,
    }
    return render(request,'home.html',context)

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('/')
    # return HttpResponse("The task was updated......")

def completed(request, pk):
    t=get_object_or_404(Task,pk=pk)
    t.is_completed=True
    t.save()
    return redirect('/')
    # return HttpResponse(pk)
    
def undone(request,pk):
    t=get_object_or_404(Task,pk=pk)
    t.is_completed =False
    t.save()
    return redirect('/')

def delete(request,pk):
    d_t=get_object_or_404(Task,pk=pk)
    d_t.delete()
    return redirect('/')

def edit(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task= request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('/')
    else:
        context = {
            'get_task': get_task,
        }
    return render(request, 'edit.html', context)
    