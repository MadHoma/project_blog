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
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super(Blog, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(Q(title__icontains=q)|
                                   Q(text__icontains=q)|
                                   Q(text_preview__icontains=q))
        return queryset
    
    
class BlogSearch(ListView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
            result = super(BlogSearch, self).get_queryset()

            query = self.request.GET.get('q')
            print(query)
            if query:
                query_list = query.split()
                result = result.filter(
                    reduce(operator.and_,
                        (Q(title__icontains=q) for q in query_list)) |
                    reduce(operator.and_,
                        (Q(content__icontains=q) for q in query_list))
                )
            print(query)
            return result
   