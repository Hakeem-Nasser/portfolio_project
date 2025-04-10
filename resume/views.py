from django.shortcuts import render
from .models import Certification, Experience

def cv(request):
    experiences = Experience.objects.all().order_by('-start_date')
    certifications = Certification.objects.all().order_by('-issue_date')
    return render(request, 'resume/cv.html', {
        'experiences': experiences,
        'certifications': certifications
    })

def certifications(request):
    certifications = Certification.objects.all().order_by('-issue_date')
    return render(request, 'resume/certifications.html', {'certifications': certifications})

def experience(request):
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'resume/experience.html', {'experiences': experiences})