from django.conf.urls import url, include
from blog import views

urlpatterns = [
     url(r'', views.start_page),
]