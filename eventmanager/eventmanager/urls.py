
from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='mainapp')),
    path('', include('django.contrib.auth.urls'))
]
