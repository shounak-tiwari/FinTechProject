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
        # create a dict which you want to send 
        value = {"FirstName":"Naina", "LastName" : "Jaiswal", "Contact":"Nakul122@gmail.com"}        
        #send the dict to the frontend in form of keys and value 
        return render(request,'index.html',{"key":value})

class AboutViews(views.View):
    def get(self,request):
        value = ["Akash","Naina","Nakul"]
        
        return render(request,'about.html',{"key2":value})

# Reponse : 
# httpresponse
# Apis  