from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True,
                                on_delete=models.CASCADE)
    status = models.TextField(max_length=300,default='Hey! I am here')
    location = models.TextField(max_length=100,blank=True)
    photo = models.ImageField(upload_to='pics',default='default.jpg')

    def __str__(self):
        return self.user.username + ' ' + 'profile'

class UserPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' : '+ self.content
