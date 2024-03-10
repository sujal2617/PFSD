from django.shortcuts import render, redirect
from django.contrib import messages
from .models import signup,cartitem


def checksignup(request):
    if request.method == "POST":
        name = request.POST["name"]
        phno = request.POST["phno"]
        email = request.POST["email"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if signup.objects.filter(username=uname).exists():
                messages.info(request, "username already exists......")
                return render(request, "signup.html")
            elif signup.objects.filter(email=email).exists():
                messages.info(request, "email already exists.....")
                return render(request, "signup.html")
            else:
                user = signup.objects.create(name=name, phno=phno, email=email, username=uname,
                                             password=pwd)
                user.save()
                messages.info(request, "user created successfully....")
                return render(request, "login.html")
        else:
            messages.info(request, "Password not matching......")
            return render(request, "signup.html")

def checklogin(request):
    if request.method == "POST":
        name = request.POST["uname"]  # gets user name
        pwdd = request.POST["pwd"]
        flag = signup.objects.filter(username=name, password=pwdd).values()
        if flag:  # flag is not empty
            if name == "sujal2624":  # here "sujal2624" is admin
                messages.info(request,
                              "This is Admin's page")  # to send message to the next page
                return render(request, "adminhome.html")
        if flag:
            messages.info(request, "This is User's page")
            return render(request, "userhome.html")
        else:
            messages.info(request, "Your credentials are not correct")
            return render(request, "loginfail.html")


def checkchangepassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = signup.objects.filter(username=uname, password=opwd).values()
        if flag:
            signup.objects.filter(username=uname, password=opwd).update(password=npwd)
            messages.info(request, "Password updated successfully")
            return render(request, "login.html")
        else:
            return render(request, "changepassword.html")
    else:
        return render(request, "changepassword.html")

def logincheckchangepassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = signup.objects.filter(username=uname, password=opwd).values()
        if flag:
            signup.objects.filter(username=uname, password=opwd).update(password=npwd)
            messages.info(request, "Password updated successfully")
            return render(request, "login.html")
        else:
            return render(request, "loginchangepassword.html")
    else:
        return render(request, "loginchangepassword.html")


def loginadmincheckchangepassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = signup.objects.filter(username=uname, password=opwd).values()
        if flag:
            signup.objects.filter(username=uname, password=opwd).update(password=npwd)
            messages.info(request, "Password updated successfully")
            return render(request, "login.html")
        else:
            return render(request, "loginadminchangepassword.html")
    else:
        return render(request, "loginadminchangepassword.html")

def addtocart(request, item_name, item_cost):
    cart_item = cartitem(name=item_name, cost=item_cost)
    cart_item.save()
    return redirect('cart')  # Redirect to the cart page after adding to cart