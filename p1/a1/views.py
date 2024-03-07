from django.shortcuts import render
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
            return HttpResponseRedirect('/form2/')
      
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
    return HttpResponse("Thank You for submitting the form. We will get back to you soon.")