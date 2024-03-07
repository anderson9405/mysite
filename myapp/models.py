from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title= models.CharField(max_length=200)
    descripcion= models.TextField()
    isDone = models.BooleanField(default=False)

    #Relation with project table
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + '-' + self.project.name