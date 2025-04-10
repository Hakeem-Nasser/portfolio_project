from django.db import models

# Create your models here.

class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} ({self.submitted_at.strftime('%Y-%m-%d')})"
