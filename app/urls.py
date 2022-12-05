from django.urls import path
from .views import *

urlpatterns = [

    path('',Home,name="home"),
    path('signup/',SignUp.as_view(),name="Signup"),
    path('login/',Login.as_view(),name="login")
]