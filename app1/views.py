from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request,"one.html")

def three(request):
    return render(request,"home.html")

def five(request):
    return render(request,"five.html")

def seven(request):
    return render(request,"seven.html")