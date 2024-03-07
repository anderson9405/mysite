from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('about/', views.about),
    path('projects/', views.projects ,name= 'proyects'),
    path('tasks/', views.task, name='tasks'),
    path('create_task/', views.create_task, name= 'create_task'),
    path('create_project/', views.create_project, name= 'create_project'),
    path('project_detalle/<int:id>', views.project_detalle, name= 'project_detalle'),

]