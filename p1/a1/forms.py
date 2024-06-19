from django import forms
class form1(forms.Form):
    first_name = forms.CharField(label="Enter your first name",max_length=50)
    last_name = forms.CharField(label="Enter your last name",max_length=50)
    email = forms.EmailField(label="Enter your email",max_length=50)
    age = forms.IntegerField(label="Enter your age")
    # file = forms.MultipleChoiceField(choices=[('1','one'),('2','two'),('3','three')],widget=forms.CheckboxSelectMultiple)
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)
    
class ModelForm(forms.Form):
    empno = forms.IntegerField()
    ename = forms.CharField(max_length=10)
    job = forms.CharField(max_length=9)
    mgr = forms.IntegerField()
    # hiredate = forms.DateField()
    sal = forms.IntegerField()
    comm = forms.IntegerField()
    deptno = forms.IntegerField()