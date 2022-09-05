from django.shortcuts import render

# Create your views here.
def custom_contact(request):
    return render (request,'hom/contact.html')