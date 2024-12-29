from django.shortcuts import render
from django.http import HttpResponse
from django.http import  JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.conf import settings



# Create your views here.
def index(request):

    return render(request, 'IDGenie/index.html')


def blogpost_view(request):
    
    return render(request, 'IDGenie/blogpost_view.html')