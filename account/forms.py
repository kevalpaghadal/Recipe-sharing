from typing import Any
from django import forms
from . models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
            'confirm_password' : forms.PasswordInput(attrs={'class' : 'form-control'}),
        }

    def clean(self):
        cleaned_data = super(UserForm , self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("password does not match!")


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_fields'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_fields'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_fields'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'input_fields'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_fields'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_fields'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_fields'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_fields'}))
    pin_code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_fields'}))
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'input_fields', 'id': 'input-file'}))


    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'username' ,'email', 'address', 'country', 'state' , 'city' , 'pin_code' , 'profile_picture']

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         widgets = {
#             'first_name' : forms.TextInput(attrs={'class' : 'input_fields'}),
#             'last_name' : forms.TextInput(attrs={'class' : 'input_fields'}),
#             'username' : forms.TextInput(attrs={'class' : 'input_fields'}),
#             'email' : forms.EmailInput(attrs={'class' : 'input_fields'}),
#             # 'profile_picture': forms.ClearableFileInput(attrs={'class': 'input_field', 'id': 'input-file'}),
#             'address': forms.TextInput(attrs={'class': 'input_fields'}),
#             'country': forms.TextInput(attrs={'class': 'input_fields'}),
#             'state': forms.TextInput(attrs={'class': 'input_fields'}),
#             'city': forms.TextInput(attrs={'class': 'input_fields'}),
#             'pin_code': forms.NumberInput(attrs={'class': 'input_fields'}),
#         }

    