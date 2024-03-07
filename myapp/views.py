from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import createNewTask, createNewProject


# Create your views here.
def index(request):
    return render(request, 'index.html')

def projects(request):
    list_projects = list(Project.objects.all())
    return render(request, 'projects.html',{
        'proyectos': list_projects
    })

def task(request):
    list_tasks = list(Task.objects.all())
    return render(request, 'tasks.html', {
        'tareas': list_tasks
    })

def hello(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("about")

def create_task(request):

    if(request.method == 'GET'):
        return render(request, 'create_task.html', {
            'form': createNewTask
        })
    else:
            project_instance = Project.objects.get(id=2)
            Task.objects.create(title=request.POST['title'], descripcion=request.POST
                                ['descripcion'], project=project_instance)
    return redirect ('tasks')
            
    
def create_project(request):

    if(request.method == 'GET'):
        return render(request, 'create_project.html', {
            'form': createNewProject
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect ('projects')
    

def project_detalle(request, id):
    proyecto= Project.objects.get(id=id)
    tareas= Task.objects.filter(project_id=id)
    return render(request, 'detalle.html',{
        'project': proyecto,
        'tasks': tareas
    })
