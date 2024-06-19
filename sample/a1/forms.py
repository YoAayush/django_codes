from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=200, initial="Enter Your Email")
    password = forms.CharField(widget=forms.PasswordInput())
    
class NewForm(forms.Form):
    email = forms.EmailField(initial="Enter Your Email")
    password = forms.CharField(widget=forms.PasswordInput())