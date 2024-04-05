from django.shortcuts import render

# Create your views here.
def mazza(request):
    return render(request,'drinks.html')