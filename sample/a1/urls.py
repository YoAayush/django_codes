from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in, name="sign_in"),
    path('dynamic/<str:name>/', views.dynamic, name='dynamic'),
    path('template/', views.template, name='template'),
    path('form/', views.form, name='form')
]