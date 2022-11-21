from django.contrib import admin
from django.urls import path

from mainapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.hello_world),
    path("<str:word>/", views.check_kwargs),
]
