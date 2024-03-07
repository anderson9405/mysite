from django import forms

class createNewTask(forms.Form):
    title= forms.CharField(label = "Titulo de la tarea", max_length=200)
    descripcion= forms.CharField(label = "Descripción de la tarea", widget=forms.Textarea)


class createNewProject(forms.Form):
    name= forms.CharField(label = "Nombre del proyecto", max_length=200)