from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Article, Category
# Register your models here.

admin.site.register(Article)

class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    
admin.site.register(Category, CategoryAdmin)