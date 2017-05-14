from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from .models import Article

# Create your views here.

def start_page(request):
    #t = get_template('blog.html')
    #html = t.render()
    articles = Article.objects.all();
    html = render(request, 'blog.html', {"articles": articles})
    return HttpResponse(html)
    