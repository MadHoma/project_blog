from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def start_page(request):
    
    html = "<html><body><h1>Где мой шоколад</h1></body> </html>"
    return HttpResponse(html)