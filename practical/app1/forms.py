from django import forms
from .models import Employee, FileImage


class form2(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"name": "body", "rows": "10", "cols": "30"})
    )


class form1(forms.Form):
    email = forms.EmailField(label="Enter your email", max_length=50)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


def validate_email(value):
    if "@gmail.com" not in value:
        raise forms.ValidationError("Email should be gmail.com")
    else:
        return value


class form3(forms.Form):
    firstname = forms.CharField(max_length=50, label="first name")
    lastname = forms.CharField(max_length=50, label="last name")
    dateofbirth = forms.DateField(
        label="date of birth", widget=forms.NumberInput(attrs={"type": "date"})
    )
    gender = forms.ChoiceField(
        label="gender",
        choices=[("male", "Male"), ("female", "Female")],
        widget=forms.RadioSelect,
    )
    country = forms.ChoiceField(
        label="country",
        choices=[("India", "India"), ("USA", "USA"), ("UK", "UK")],
        widget=forms.Select,
    )
    email = forms.EmailField(max_length=50, validators=[validate_email])
    phone = forms.IntegerField(label="phone number")
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class EmplyeeForm(forms.Form):
    class Meta:
        model = Employee
        fields = "__all__"


class FileImageForm(forms.Form):
    class Meta:
        model = FileImage
        fields = ("image", "file")
