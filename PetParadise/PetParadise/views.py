from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contact.html")

def loginpage(request):
    return render(request, "login.html")

def cartpage(request):
    return render(request, "cart.html")

def signuppage(request):
    return render(request, "signup.html")

def loginfailpage(request):
    return render(request, "loginfail.html")

