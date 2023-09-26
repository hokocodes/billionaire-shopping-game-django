from django.shortcuts import render
from .forms import URLForm
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.
def index(request):
   return render(request,'home.html', {"form": form})