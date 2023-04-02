from django.contrib import admin
from django.urls import path, include
from registration import views as v
from members import views as v1

urlpatterns = [
    path('',v1.main,name='main'),
    path("register/", v.register, name="register"),
    path('testing/', v1.testing, name='testing'),    # <-- added
]