from django.shortcuts import render, HttpResponse

# Create your views here.
def about_us(request):
    return HttpResponse("About Us")