from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("links/",views.links, name="links"),
    path('time/<str:operator>/<int:offset>/', views.time_offset, name='time_offset'),
    path('students/', views.student_list, name='student_list'),
    path('templates_tags_filters/', views.templates_tags_filters, name='templates_tags_filters'),
    path('child2/', views.child2, name='child2'),
    path("form1/",views.f1,name="form1"),
    path("form2/",views.f2,name="form2"),
    path("signupForm/",views.signupForm,name="signupForm"),
    path("create/",views.employee_Create,name="create"),
    path("read/",views.employee_read,name="read"),
    path("update/",views.employee_update,name="update"),
    path("delete/",views.employee_delete,name="delete"),
    path("filter/",views.filter,name="filter"),
    path("chaining/",views.chaining,name="chaining"),
    path("slice/",views.slice,name="slice"),
    path("upload/",views.upload,name="upload"),
    path("success/",views.success,name="success"),
    path("employeeAdd/",views.employeeAdd,name="employeeAdd"),
]
