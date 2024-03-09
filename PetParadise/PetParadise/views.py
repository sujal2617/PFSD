from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")

def loginaboutpage(request):
    return render(request, "loginabout.html")

def contactpage(request):
    return render(request, "contact.html")

def logincontactpage(request):
    return render(request, "logincontact.html")

def loginpage(request):
    return render(request, "login.html")

def loginhomepage(request):
    return render(request, "loginhome.html")

def cartpage(request):
    return render(request, "cart.html")

def signuppage(request):
    return render(request, "signup.html")

def loginfailpage(request):
    return render(request, "loginfail.html")

def logoutpage(request):
    return render(request, "login.html")

def inventorypage(request):
    return render(request, "inventory.html")

def petspage(request):
    return render(request, "pets.html")

def accessoriespage(request):
    return render(request, "accessories.html")