from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),  # Using blogpost app for blog URLs
    path('resume/', include('resume.urls')),
]

# Add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)