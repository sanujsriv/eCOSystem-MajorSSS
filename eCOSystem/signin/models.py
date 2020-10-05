from djongo import models
from signin.PasswordField import PasswordModelField
from django.contrib import auth


class signup_model(models.Model):
    full_name= models.CharField(max_length=128,null=False)
    phone = models.CharField(max_length=10, null=False)
    email=models.EmailField(max_length=50,null=False)
    password = PasswordModelField(max_length=16, null=False)
    repeat_password = PasswordModelField(max_length=16, null=False)

    def __str__(self):
        return self.full_name





