from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onlinecourse/', include('onlinecourse.urls')),
    # Add a root URL pattern that redirects to onlinecourse
    path('', lambda request: redirect('onlinecourse/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
