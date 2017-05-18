from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Article
from django.db.models import Q

# Create your views here.

class Blog(ListView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-created_date')

    def get_queryset(self):
        queryset = super(Blog, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(Q(title__icontains=q)|
                                   Q(text__icontains=q)|
                                   Q(text_preview__icontains=q))
        return queryset