from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

user = get_user_model()

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation',widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ('email','first_name','last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords doesn't match")
        return password2

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password  = ReadOnlyPasswordHashField()

    class Meta:
        model = user
        fields = ('email','first_name','last_name' ,'is_active','is_staff', 'is_admin')

    def clean_password(self):
        return self.initial['password']
            