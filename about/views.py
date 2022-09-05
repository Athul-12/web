from urllib import request
from django.shortcuts import render

# Create your views here.
def customer_service(request):
    return render (request,'hom/service.html')

def customer_review(request):
    return render (request,'hom/review.html')