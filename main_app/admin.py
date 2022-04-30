from django.contrib import admin
from .models import Post, Comment, Product, Price, Profile

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Price)
admin.site.register(Profile)



# class PriceInlineAdmin(admin.TabularInline):
#     model = Price
#     extra = 0


# class ProductAdmin(admin.ModelAdmin):
#     inlines = [PriceInlineAdmin]


