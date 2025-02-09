from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=10000)
    photo = CloudinaryField('photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} -- {self.text[:10]}'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    profile_picture = CloudinaryField('profile_picture/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional for non-registered users
    email = models.EmailField()  # Keep only if non-users can submit
    subject = models.CharField(max_length=150)
    message = models.TextField()  # No need for max_length in TextField

    def __str__(self):
        return f"Message from {self.email} - {self.subject}"
