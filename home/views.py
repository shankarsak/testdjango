from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("working")