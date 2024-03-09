from django.urls import path
from . import views

urlpatterns=[
    path("checksignup",views.checksignup,name="checksignup"),
    path("checklogin", views.checklogin, name="checklogin"),
    path("checkchangepassword",views.checkchangepassword,name="checkchangepassword"),
]