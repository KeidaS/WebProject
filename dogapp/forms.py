from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from models import Dog, Refuge, Adoption


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class RefugeForm(ModelForm):
    class Meta:
        model = Refuge
        exclude = ('user', 'date',)


class DogForm(ModelForm):
    class Meta:
        model = Dog
        exclude = ('user', 'date', 'refuge',)


class AdoptionForm(ModelForm):
    class Meta:
        model = Adoption
        exclude = ('user', 'date', 'refuge', 'dog')
