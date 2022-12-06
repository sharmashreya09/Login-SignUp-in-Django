from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('',Home,name="home"),
    path('signup/',SignUp.as_view(),name="Signup"),
    path('login/',Login.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='/login/'),name="logout")
]