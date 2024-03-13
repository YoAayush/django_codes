from django import forms
class form2(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':'10', 'cols':'30'}))
    
class form1(forms.Form):
    email = forms.EmailField(label="Enter your email",max_length=50)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
