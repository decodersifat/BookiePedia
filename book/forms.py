from django import forms
from .models import Books,Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cloudinary.forms import CloudinaryFileField
class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        
        fields = ['title' ,'text', 'photo']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    second_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=11)
    profile_picture = CloudinaryFileField()  # Cloudinary field for photo upload

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'second_name', 'phone', 'profile_picture', 'password1', 'password2')