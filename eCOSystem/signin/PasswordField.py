
from djongo import models
from django import forms

class PasswordField(forms.CharField):
    widget = forms.PasswordInput

class PasswordModelField(models.CharField):
    def formfield(self, **kwargs):
        defaults={'form_class':PasswordField}
        defaults.update(kwargs)
        return super(PasswordModelField,self).formfield(**defaults)
