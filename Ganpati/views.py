from django.shortcuts import render
from prediction import mappingsss
def home(request):
    if request.method=="POST":
        l=mappingsss()
        return render(request,"nearby.html",{'listt':l})
    return render(request,"home.html")