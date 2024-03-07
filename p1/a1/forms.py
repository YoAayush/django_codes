from django import forms
class form1(forms.Form):
    first_name = forms.CharField(label="Enter your first name",max_length=50)
    last_name = forms.CharField(label="Enter your last name",max_length=50)
    email = forms.EmailField(label="Enter your email",max_length=50)
    age = forms.IntegerField(label="Enter your age")
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)