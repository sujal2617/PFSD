"""
URL configuration for PetParadise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('home', views.homepage, name="home"),
    path("loginabout", views.loginaboutpage, name="loginabout"),
    path("contact", views.contactpage, name="contact"),
    path("logincontact", views.logincontactpage, name="logincontact"),
    path("cart", views.cartpage, name="cart"),
    path("login/", views.loginpage, name="login"),
    path("loginhome", views.loginhomepage, name="loginhome"),
    path("signup", views.signuppage, name="signup"),
    path("loginfail", views.loginfailpage, name="loginfail"),
    path("logout", views.logoutpage, name="logout"),
    path("inventory", views.inventorypage, name="inventory"),
    path("pets", views.petspage, name="pets"),
    path("accessories", views.accessoriespage, name="accessories"),
    path("feedback", views.feedbackpage, name="feedback"),
    path("", include("adminapp.urls")),


]