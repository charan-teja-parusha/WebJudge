from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.main,name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<str:brandname>', views.details, name='details'),
    # path('testing/', views.testing, name='testing'),
    path('compare/', views.compare, name='compare'),
    path('search/', views.search, name='search'),
]