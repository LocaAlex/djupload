from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserFile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file', 'user_file_name']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.user_file_name:
            instance.user_file_name = instance.file.name
        if commit:
            instance.save()
        return instance


class FileRenameForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['user_file_name']
    
    def __init__(self, *args, **kwargs):
        super(FileRenameForm, self).__init__(*args, **kwargs)
        print("Initializing FileRenameForm")  # Debug statement
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})
