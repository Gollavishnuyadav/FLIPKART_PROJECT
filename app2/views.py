from django.shortcuts import render

# Create your views here.
def two(request):
    return render(request,"two.html")

def four(request):
    return render(request,"four.html")

def six(request):
    return render(request,"six.html")
