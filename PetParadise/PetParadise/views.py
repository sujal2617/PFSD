from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contact_us.html")

