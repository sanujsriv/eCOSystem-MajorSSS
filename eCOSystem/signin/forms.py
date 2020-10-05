from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from signin.models import signup_model


class MyForm(forms.ModelForm):

    class Meta:
        model = signup_model
        fields = ('full_name','phone','email','password','repeat_password')
        widgets={
       'full_name':forms.TextInput(attrs={'placeholder':'Name'}),
       'phone':forms.TextInput(attrs={'placeholder':'Phone'}),
       'email': forms.TextInput(attrs={'placeholder': 'Email'}),
       'password':forms.PasswordInput(attrs={'placeholder':'Password'}),
       'repeat_password':forms.PasswordInput(attrs={'placeholder':'Repeat Password'}),
                 }

    def __init__(self,*args,**kwargs):
        super(MyForm, self).__init__(*args,**kwargs)
        self.fields['full_name'].label = ''
        self.fields['phone'].label = ''
        self.fields['email'].label = ''
        self.fields['password'].label = ''
        self.fields['repeat_password'].label = ''
