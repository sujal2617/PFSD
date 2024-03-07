from django.shortcuts import render
from django.contrib import messages
from .models import signup


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
        # flag = Admin.objects.filter(username=adminuname, password=adminpwd).values()
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
