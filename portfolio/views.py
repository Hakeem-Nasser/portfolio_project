from django.shortcuts import render, get_object_or_404
from .models import Project

def portfolio_list(request):
    projects = Project.objects.all().order_by('-date_completed')
    return render(request, 'portfolio/portfolio_list.html', {'projects': projects})

def portfolio_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'portfolio/portfolio_detail.html', {'project': project})