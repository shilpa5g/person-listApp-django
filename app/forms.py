from django import forms

from .models import Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'phone_number', 'address')


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 70,
        widget = forms.EmailInput()
    )
    date_of_birth = forms.DateField(
        required = True,
        label = 'Date Of Birth',
        widget = forms.DateInput()
    )
    age = forms.IntegerField(
        required = True,
        label = 'Age',
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class PasswordResetForm(forms.Form):
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 70,
        widget = forms.EmailInput()
        )