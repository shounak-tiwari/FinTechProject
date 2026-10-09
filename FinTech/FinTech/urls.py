from django.contrib import admin
from django.urls import path
from UserApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home)
]
