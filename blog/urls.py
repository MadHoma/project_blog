from django.conf.urls import url, include
from blog.views import Blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     url(r'', Blog.as_view()),
     url(r'^search/$', Blog.as_view()),
]