from django.db import models
from django.contrib.auth.models import User

class Filepdf(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=150,default = "")
    file = models.FileField(upload_to='filePDF/',default = "")
    disc = models.CharField(max_length=600,default = "")
    category = models.CharField(max_length=100,default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class User_Admin(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length=200,default="")
    
    def __str__(self):
        return self.user.username