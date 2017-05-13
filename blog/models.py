from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = 'category'
    name = models.CharField(max_length=100)

class Article(models.Model):
    class Meta:
        db_table = 'article'
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text_preview = models.TextField()
    text = models.TextField()
    category = models.ForeignKey(Category)
    created_date = models.DateTimeField(
            default=timezone.now)
    change_date = models.DateTimeField(
            blank=True, null=True)


