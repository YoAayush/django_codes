from django.shortcuts import render, redirect
from django.http import HttpResponse
from.forms import SignInForm, NewForm

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})

def dynamic(request,name):
    return HttpResponse(f"Hello {name}")

def template(request):
    return render(request , 'a1/sample.html', {'name':'Aayush', 'college':'VIPS'})

def form(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
           email = form.cleaned_data['email']
           password = form.cleaned_data['password']
           return render(request, 'a1/FormData.html', {'email':email, 'password':password})
    else:
        form = NewForm()
    return render(request, 'a1/submit.html', {'form':form})