from django.shortcuts import render, redirect
from django.http import HttpResponse

# from django.utils import timezone
from datetime import datetime, timedelta
from .forms import form1, form2, form3, EmplyeeForm, FileImageForm
from .models import Employee, FileImage

temp = """
<h1>Tags</h1><br>
<a href='https://github.com'>GITHUB</a><br><br>
<a href='https://geeksforgeeks.com'>GEEKSFORGEEKS</a><br><br>
<a href='https://divanshusoni.cin'>PORTFOLIO</a><br><br>
<a href='https://stackoverflow.com'>STACKOVERFLOW</a><br><br>
<a href='https://microsoft.com'>MICROSOFT</a><br><br>
"""


def index(request):
    return HttpResponse("home page")


def links(request):
    return HttpResponse(temp)


def time_offset(request, operator, offset):
    current_time = datetime.now()
    if operator == "plus":
        new_time = current_time + timedelta(hours=int(offset))
    elif operator == "minus":
        new_time = current_time - timedelta(hours=int(offset))
    else:
        new_time = current_time

    context = {
        "current_time": current_time,
        "new_time": new_time,
        "offset": offset,
        "operator": operator,
    }
    return render(request, "app1/current_time.html", context)


Students = [
    {"name": "vishal jain", "subject": "Literature"},
    {"name": "Jasmine", "subject": "Music"},
    {"name": "Lalit kumar", "subject": "Philosophy"},
    {"name": "Piyush Chopra", "subject": "Music"},
    {"name": "Yamini Malhotra", "subject": "Literature"},
]


def student_list(request):
    return render(request, "app1/students.html", {"students": Students})


def templates_tags_filters(request):
    current_time = datetime.now()
    context = {
        "title": "Teplates_tags_filters",
        "numbers": [1, 2, 3, 4, 5],
        "user": {"name": "john", "age": 25, "is_registered": True},
        "current_time": current_time,
        "temp": "HELLO THIS IS A RAINY DAY",
    }
    return render(request, "app1/templates_tags_filters.html", context)


def child2(request):
    return render(request, "app1/child2.html")


def f1(request):
    if request.method == "POST":
        form = form1(request.POST)
        Req_Email = "abc123@gmail.com"
        Req_Password = "abc123"
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            if email == Req_Email and password == Req_Password:
                return render(
                    request, "app1/NewForm.html", {"email": email, "password": password}
                )
            else:
                return HttpResponse("Invalid Credentials")
    else:
        form = form1()
    return render(request, "app1/submit.html", {"form": form})


def f2(request):
    if request.method == "POST":
        form = form2(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            return render(
                request,
                "app1/FormData.html",
                {"name": name, "email": email, "subject": subject, "message": message},
            )
    else:
        form = form2()
    return render(request, "app1/submit.html", {"form": form})


def signupForm(request):
    if request.method == "POST":
        form = form3(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            dateofbirth = form.cleaned_data["dateofbirth"]
            country = form.cleaned_data["country"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            return render(
                request,
                "app1/Thanks.html",
                {
                    "firstname": firstname,
                    "lastname": lastname,
                    "dateofbirth": dateofbirth,
                    "country": country,
                    "email": email,
                    "phone": phone,
                },
            )
    else:
        form = form3()
    return render(request, "app1/index.html", {"form": form})


def employee_Create(request):
    for i in range(1, 11):
        department_id = 1 if i % 2 == 0 else 2  # alternate between department IDs 1 and 2
        Employee.objects.create(
            empName=f"Employee_{i}",
            age=22 + i,
            department_id=department_id,
            desgination="Software Developer",
            qualification="B.Tech",
            dateOfJoining="2021-09-01",
        )
    return HttpResponse("Employee Created")


def employee_read(request):
    a = Employee.objects.get(id=13)
    return HttpResponse(f"Employee id={a.id} <br /> Employee Name={a.empName}")


def employee_update(request):
    a = Employee.objects.get(id=12)
    a.empName = "John"
    a.save()
    return HttpResponse(f"Employee Updated")


def employee_delete(request):
    a = Employee.objects.get(id=14)
    a.delete()
    return HttpResponse("Employee Deleted")


def filter(request):
    a = Employee.objects.filter(qualification="B.Tech")
    return render(request,'app1/index2.html',{'a':a})


def chaining(request):
    a = Employee.objects.filter(empName="John").filter(age=23)
    return render(request,'app1/index2.html',{'a':a})


def slice(request):
    a = Employee.objects.all()[:3]
    return render(request,'app1/index2.html',{'a':a})


def upload(request):
    if request.method == "POST":
        form = FileImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("File Uploaded")
    else:
        form = FileImageForm()
    return render(request, "app1/upload.html", {"form": form})


def success(request):
    return render(request, "app1/success.html")


def employeeAdd(request):
    if request.method == "POST":
        form = EmplyeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
        else:
            if "age" in form.errors:
                error_message = form.errors["age"] = form.errors["age"].as_text()
                return render(
                    request,
                    "app1/employee.html",
                    {"form": form, "error_message": error_message},
                )
    else:
        form = EmplyeeForm()
    return render(request, "app1/employee.html", {"form": form})
