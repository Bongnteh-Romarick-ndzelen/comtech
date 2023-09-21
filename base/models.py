from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(default=1)
    bio = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='default.jpg')

    def __str__(self):
        return self.user.username

#creating Homepage model
class HomePage(models.Model):
    about = models.TextField(null=True)
    topics = models.CharField(max_length=200)
    def __str__(self):
        return  self.topics
    
class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    message = models.TextField()
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.firstname

#creating livechat model
class Live_Chat(models.Model):
    name = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    date_send = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
