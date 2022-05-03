from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
        

class UserChangeForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        
   
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}), 
            'body': forms.Textarea(attrs={'class': 'form-control'}),  
            
        }
        
        
           
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'image': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),  
            
        }
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body',)
        
        widgets = {
            # 'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user'}), 
            # 'author': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', }),
            'body': forms.Textarea(attrs={'class': 'form-control'}),  
            
        }
        
        
        
# class ProfilePageForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('bio',)
#     	# fields = ('bio')
#         widgets = {
#             'bio': forms.TextInput(attrs={'class': 'form-control'}),
             
            
#         }
	   