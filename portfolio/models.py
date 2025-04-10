from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_completed = models.DateField()
    project_url = models.URLField(blank=True, null=True)
    project_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    
    def __str__(self):
        return self.title