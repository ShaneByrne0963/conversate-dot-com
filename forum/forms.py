from django import forms
from django.contrib.auth.models import User
from .models import Post
from django_summernote.widgets import SummernoteWidget


class PostContentForm(forms.Form):
    body = forms.CharField(
        required=True,
        widget=SummernoteWidget()
    )

    def __init__(self, *args, **kwargs):
        """
        Removes the suffix ":" from the form label
        """
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={ 'class': 'form-control' })
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={ 'class': 'form-control' })
    )

    class Meta:
        model = User
        fields = ['username', 'email']
