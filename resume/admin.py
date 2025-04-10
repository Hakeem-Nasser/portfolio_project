from django.contrib import admin

# Register your models here.
from .models import Certification, Experience

admin.site.register(Certification)
admin.site.register(Experience)