from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="Forum-Home"),
    path('about/',views.About,name="Forum-About"),
    path('signin/',views.signin,name='Sign-IN')
]