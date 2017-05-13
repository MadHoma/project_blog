from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def start_page(request):
    view = 'base_one'
    html = "<html><body>This is %s view</body> </html>" % view
    return HttpResponse(html)