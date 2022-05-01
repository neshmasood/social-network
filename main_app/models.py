from django.db import models
from django.contrib.auth.models import User
from django .urls import reverse
from datetime import datetime, date


# Create your models here.


class Post (models.Model):
    title = models.CharField(max_length=255)
    # image = models.ImageField(null = True, blank = True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='posts')
    
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    
    
class Comment(models.Model):
        post = models.ForeignKey(Post, blank=True, related_name="comments", on_delete=models.CASCADE)
        # name = models.CharField(max_length=255)
        author = models.ForeignKey(User, on_delete = models.CASCADE)
        body = models.TextField()
        date_added = models.DateTimeField(auto_now_add=True)
        
        
        class Meta: 
            ordering = ('-date_added',) 
        
        def __str__(self):
            return '%s  - %s' % (self.post.title, self.author)
        
        
        # def __str__(self):
        #     return 'Comment by {}'.format(self.body)

# class Post (models.Model):
#     title = models.CharField(max_length=255)
#     image = models.ImageField(null = True, blank = True, upload_to="images/")
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = models.TextField()
#     post_date = models.DateField(auto_now_add=True)
#     likes = models.ManyToManyField(User, related_name='posts')
    
    
#     def total_likes(self):
#         return self.likes.count()
    
#     def __str__(self):
#         return self.title + '|' + str(self.author)
    
#     def get_absolute_url(self):
#         return reverse('home')
    
    
# class Comment(models.Model):
#         post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
#         # name = models.CharField(max_length=255)
#         author = models.ForeignKey(User, on_delete = models.CASCADE)
#         body = models.TextField()
#         date_added = models.DateTimeField(auto_now_add=True)
        
        
#         class Meta: 
#             ordering = ('date_added',) 
        
#         def __str__(self):
#             return '%s  - %s' % (self.post.title, self.author)
        
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    stripe_product_id = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Price (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=250)
    price = models.IntegerField(default=0) 
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # stripe_id = models.CharField(max_length=250)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    
    def __str__(self):
        return str (self.user)