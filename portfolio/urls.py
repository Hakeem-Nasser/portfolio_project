from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('<int:project_id>/', views.portfolio_detail, name='portfolio_detail'),
]