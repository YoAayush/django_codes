from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="defaultpage"),
    path("home/",views.home,name="homepage"),
    path("newTemp/",views.new_func,name="newTemp"),
    path("form1/",views.f1,name="form1"),
    path("form2/",views.f2,name="form2"),
    path("form-main/",views.main,name="main"),
    path("thanks/",views.t1,name="thanks"),
    path("modelForm/",views.home1,name="modelForm"),
]