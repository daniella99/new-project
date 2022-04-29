from difflib import context_diff
from django.shortcuts import render

from django.http import HttpResponse 

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcacke!'}
    #return HttpResponse("Rango say hey there!")
    return render(request, 'rango/index.html', context = context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page.")
