from django.db import models

# Create your models here.

class Certification(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.role} at {self.company_name}"
