from django.contrib import admin
from django.urls import path
from UserApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # enter or create empty path on urls 
    path('',views.HomeViews.as_view()),
    # path of aboutus views path on urls 
    path('about/',views.AboutViews.as_view())
]
