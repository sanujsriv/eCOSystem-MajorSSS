from django import forms
from .models import Experience, Address, Skill, Interest, Education_details, Certifications,user_profile

class ExperienceForm(forms.ModelForm):
    class Meta():
        model = Experience
        fields = "__all__"
        widgets = {
            'descriptionExp': forms.Textarea(attrs={'placeholder': 'Share your experience'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company'}),
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'work_field': forms.TextInput(attrs={'placeholder': 'Work Field'}),
            'from_date': forms.TextInput(attrs={'placeholder': 'From', 'class': 'datepicker'}),
            'to_date': forms.TextInput(attrs={'placeholder': 'To', 'class': 'datepicker'}),

        }

    def __init__(self, *args, **kwargs):
            super(ExperienceForm,self).__init__(*args, **kwargs)
            self.fields['company'].label = ''
            self.fields['title'].label = ''
            self.fields['location'].label = ''
            self.fields['work_field'].label = ''
            self.fields['from_date'].label = ''
            self.fields['to_date'].label = ''
            self.fields['descriptionExp'].label = ''

class AddressForm(forms.ModelForm):
    class Meta():
        model = Address
        fields = "__all__"

        widgets = {
            # 'state': forms.CheckboxInput(),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'locality': forms.TextInput(attrs={'placeholder': 'Locality'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'zip': forms.TextInput(attrs={'placeholder': 'Zip'}),

        }

    def __init__(self, *args, **kwargs):
            super(AddressForm, self).__init__(*args, **kwargs)
            self.fields['country'].label = ''
            self.fields['state'].label = ''
            self.fields['locality'].label = ''
            self.fields['city'].label = ''
            self.fields['zip'].label = ''


class SkillForm(forms.ModelForm):
    class Meta():
        model = Skill
        fields = "__all__"
        widgets = {
            'skill': forms.TextInput(attrs={'placeholder': 'My Skill Set..'}),

        }

        def __init__(self, *args, **kwargs):
            super(SkillForm,self).__init__(*args, **kwargs)
            self.fields['skill'].label = ''


class InterestForm(forms.ModelForm):
    class Meta():
        model = Interest
        fields = "__all__"
        widgets = {
            'interest': forms.TextInput(attrs={'placeholder': 'My Interests...'}),

        }

        def __init__(self, *args, **kwargs):
            super(InterestForm,self).__init__(*args, **kwargs)
            self.fields['interest'].label = ''

class Education_detailsForm(forms.ModelForm):
    class Meta():
        model = Education_details
        fields = "__all__"
        widgets = {
            'school': forms.TextInput(attrs={'placeholder': 'School Name'}),
            'school_from': forms.TextInput(attrs={'placeholder': 'From', 'class': 'datepicker'}),
            'school_to': forms.TextInput(attrs={'placeholder': 'To', 'class': 'datepicker'}),
            'degree': forms.TextInput(attrs={'placeholder': 'Degree'}),
            'study_field': forms.TextInput(attrs={'placeholder': 'Study Field'}),
            'descriptionEdu': forms.Textarea(attrs={'placeholder': 'Description', }),
        }

    def __init__(self, *args, **kwargs):
            super(Education_detailsForm,self).__init__(*args, **kwargs)
            self.fields['school'].label = ''
            self.fields['school_from'].label = ''
            self.fields['school_to'].label = ''
            self.fields['degree'].label = ''
            self.fields['study_field'].label = ''
            self.fields['descriptionEdu'].label = ''

class CertificationsForm(forms.ModelForm):
    class Meta():
        model = Certifications
        fields = "__all__"
        widgets = {
            'certification_name': forms.TextInput(attrs={'placeholder': 'Certification In..'}),
            'authority': forms.TextInput(attrs={'placeholder': 'Certification Authority'}),
            'cert_from': forms.TextInput(attrs={'placeholder': 'From', 'class': 'datepicker'}),
            'cert_to': forms.TextInput(attrs={'placeholder': 'To', 'class': 'datepicker'}),
            'cert_pic': forms.FileInput(attrs={'placeholder': 'Upload Certificate', 'class': ''}),

        }

    def __init__(self, *args, **kwargs):
         super(CertificationsForm,self).__init__(*args, **kwargs)
         self.fields['certification_name'].label = ''
         self.fields['authority'].label = ''
         self.fields['cert_from'].label = ''
         self.fields['cert_to'].label = ''
         self.fields['cert_pic'].label = ''


class ProfilepicForm(forms.ModelForm):
    class Meta:
        model= user_profile
        fields=('user_image',)


    def __init__(self, *args, **kwargs):
        super(ProfilepicForm, self).__init__(*args, **kwargs)
        self.fields['user_image'].widget.attrs.update({'id':'profilepic-form','class':'profilepic-class','label':''})

