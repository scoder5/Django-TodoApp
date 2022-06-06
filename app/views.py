from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    context = {'success':False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success':True}

    return render(request, 'index.html', context)

def todo(request):
    allTask = Task.objects.all()
    for item in allTask:
        print(item.taskTitle)

    context = {'tasks': allTask}    
    return render(request, 'todo.html', context)
