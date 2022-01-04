from django import forms
from django.contrib.auth.models import User
from .models import Biodata


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')
        widgets = {
            "first_name" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'placeholder' : 'nama depan',
                    'required' : True
                }
            ),
            "last_name" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'cols' : '30',
                    'rows' : '10',
                    'required' : True
                }
             ),
             "email" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'placeholder' : 'email anda',
                    'required' : True
                }
            ),
        }

class BiodataForms(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = ('alamat','telp')
        widgets = {
            "alamat" : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'placeholder' : 'silahkan masukkan email',
                    'required' : True
                }),
            "telp" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'cols' : '30',
                    'rows' : '10',
                    'required' : True
                }),
        }