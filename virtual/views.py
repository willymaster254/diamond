from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import reverse
# Create your views here.
def home(request):
     return render (request,'virtual.html')
