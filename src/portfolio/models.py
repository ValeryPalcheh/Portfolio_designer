# portfolio/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects', null=True)

    def __str__(self):
        return self.title

# portfolio/models.py
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Изображение {self.id} проекта {self.project.title}"

