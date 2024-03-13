from django.shortcuts import render
from django.http import HttpResponse
# from django.utils import timezone
from datetime import datetime,timedelta
from .forms import form1,form2

temp = '''
<h1>Tags</h1><br>
<a href='https://github.com'>GITHUB</a><br><br>
<a href='https://geeksforgeeks.com'>GEEKSFORGEEKS</a><br><br>
<a href='https://divanshusoni.cin'>PORTFOLIO</a><br><br>
<a href='https://stackoverflow.com'>STACKOVERFLOW</a><br><br>
<a href='https://microsoft.com'>MICROSOFT</a><br><br>
'''

def index(request):
    return HttpResponse("hello world")

def links(request):
    return HttpResponse(temp)

def time_offset(request, operator, offset):
    current_time = datetime.now()
    if operator == 'plus':
        new_time = current_time + timedelta(hours=int(offset))
    elif operator == 'minus':
        new_time = current_time - timedelta(hours=int(offset))
    else:
        new_time = current_time
    
    context = {
        'current_time': current_time,
        'new_time': new_time,
        'offset': offset,
        'operator': operator
    }
    return render(request, 'app1/current_time.html', context)

Students = [
    {'name': 'vishal jain' , 'subject': 'Literature'},
    {'name': 'Jasmine' , 'subject' : 'Music'},
    {'name': 'Lalit kumar' , 'subject' : 'Philosophy'},
    {'name': 'Piyush Chopra' , 'subject' : 'Music'},
    {'name': 'Yamini Malhotra' , 'subject' : 'Literature'},
]

def student_list(request):
    return render(request, 'app1/students.html', {'students':Students})

def templates_tags_filters(request):
    current_time = datetime.now()
    context = {
        'title': 'Teplates_tags_filters',
        'numbers': [1, 2, 3, 4, 5],
        'user': {
            'name': 'john',
            'age': 25,
            'is_registered': True
        },
        'current_time': current_time,
        'temp': 'HELLO THIS IS A RAINY DAY'
    }
    return render(request, 'app1/templates_tags_filters.html', context)

def child2(request):
    return render(request, 'app1/child2.html')

def f1(request):
    if request.method == 'POST':
        form = form1(request.POST)
        Req_Email = "abc123@gmail.com"
        Req_Password = "abc123"
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if email == Req_Email and password == Req_Password:
                return render(request,'app1/NewForm.html',{'email':email,'password':password})
            else:
                return HttpResponse("Invalid Credentials")
    else:
        form = form1()
    return render(request,'app1/submit.html',{'form':form})

def f2(request):
    if request.method == 'POST':
        form = form2(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            return render(request,'app1/FormData.html',{'name':name,'email':email,'subject':subject,'message':message})
    else:
        form = form2()
    return render(request,'app1/submit.html',{'form':form})