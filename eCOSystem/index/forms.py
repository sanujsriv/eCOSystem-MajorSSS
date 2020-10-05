from django import forms

from .models import Posts, Comment


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('text',)
        widgets={
            'text':forms.TextInput(attrs={'placeholder':'Comment here.....'}),
        }
    def __init__(self,*args,**kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        self.fields['text'].label = ''
