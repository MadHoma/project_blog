import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = 'category'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    class Meta:
        db_table = 'article'
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text_preview = models.TextField()
    text = models.TextField()
    category = models.ManyToManyField(Category, verbose_name="list of categoryes")
    created_date = models.DateTimeField(
            default=timezone.now)
    change_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.change_date = datetime.datetime.now()
        super(Article, self).save(*args, **kwargs)
