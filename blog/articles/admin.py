from django.contrib import admin

# Register your models here.

from .models import Article
from .models import Category

admin.site.register(Category)
admin.site.register(Article)

