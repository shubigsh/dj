from django.contrib import admin
from django.urls import include,path
from .models import Task

# Register your models here.
urlpatterns=[
    path("admin/",admin.site.urls),
    path("",include('base.urls')),
    admin.site.register(Task)
]