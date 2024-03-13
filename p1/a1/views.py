from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import form1
from django.core.mail import send_mail

def index(request):
    return HttpResponse("this is default page")

def home(request):
    return render(request,'a1/index1.html')

def new_func(request):
    dictionary = {'first_name':'Aayush','last_name':'Chopra'}
    return render(request,'a1/newTemp.html',dictionary)

def f1(request):
    if request.method == 'POST':
        form = form1(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            print(first_name,last_name,email,age)
            return render(request,'a1/NewForm.html',{'first_name':first_name,'last_name':last_name,'email':email,'age':age})

        # if form.is_valid():
        #     subject = form.cleaned_data["subject"]
        #     message = form.cleaned_data["message"]
        #     sender = form.cleaned_data["sender"]
        #     cc_myself = form.cleaned_data["cc_myself"]
        #     recipients = ["ayushchopra1977@gmail.com"]
        #     if cc_myself:
        #         recipients.append(sender)
        #     send_mail(subject, message, sender, recipients)
        #     return HttpResponseRedirect("/form2/")
    else:
        form = form1()
    return render(request,'a1/submit.html',{'form':form})

def f2(request):
    return render(request,'a1/NewForm.html')

def main(request):
    d = {}
    try:
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        n3 = n1 + n2
        d = {'value1':n1,'value2':n2,'output':n3}
        if request.method == 'POST':
            return HttpResponseRedirect(f'/thanks/?output={n3}')
    except:
        pass
    return render(request,'a1/main.html',d)

def t1(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request,'a1/thanks.html',{'output':output})