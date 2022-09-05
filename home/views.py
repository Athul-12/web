from django.shortcuts import render


# Create your views here.
def customer_login(request):
    return render (request,'hom/login.html')

def customer_intro(request):
    return render (request,'hom/intro.html')