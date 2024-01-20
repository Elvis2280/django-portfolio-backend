from django.db import models

# Create your models here.

class Tags(models.Model): 
    name: models.CharField(max_length=50)
    id: models.IntegerField(primary_key=True)

class Projects(models.Model):
    title: models.CharField(max_length=200)
    description: models.TextField(max_length=500)
    id: models.UUIDField(primary_key=True)
    tags: models.ManyToManyField(Tags)
    image: models.ImageField(upload_to='images/')
    projectLink: models.URLField(max_length=200)
    content: models.TextField(max_length=5000)
    owner: models.CharField(max_length=50)
    createdAt: models.DateTimeField(auto_now_add=True)