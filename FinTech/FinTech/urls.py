from django.contrib import admin
from django.urls import path
from UserApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # enter or create empty path on urls 
    path('',views.HomeViews.as_view())
]
