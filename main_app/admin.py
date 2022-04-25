from django.contrib import admin
from .models import Post, Comment, Product, Price

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Price)
