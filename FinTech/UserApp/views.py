from django.shortcuts import render
from django.http import HttpResponse

from django import views

#  views 
# 1. function based views 
# 2. class based views 

# def homeViews(request):
#     return HttpResponse("Hey! wellcome in django")

# send dict,list,any thing  as response 

class HomeViews(views.View):
    def get(self,request):
        dic = {
            "first name":"Akash",
            "last name":"Tiwari",
            "email":"akashtiwari1014@gmail.com"
        }        
        return render(request,'index.html',{"dic":dic})

# Reponse : 
# httpresponse
# Apis  