from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.cv, name='cv'),
    path('certifications/', views.certifications, name='certifications'),
    path('experience/', views.experience, name='experience'),
]