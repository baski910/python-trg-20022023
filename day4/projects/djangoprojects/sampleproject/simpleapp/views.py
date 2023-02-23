from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return  HttpResponse("<H2>HEY! Welcome to Django! </H2>")

def welcome(request):
    #return HttpResponse("<H2>HEY! Another function from django! </H2>")
    return render(request,"simpleapp/welcome.html")

