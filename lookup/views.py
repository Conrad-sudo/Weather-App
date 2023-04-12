from django.shortcuts import render

# Create your views here.

#This is the views file

#Points a request to the webpage that we made
def home(request):
    return render(request,'home.html',{})


def about(request):
    return render(request,'about.html',{})