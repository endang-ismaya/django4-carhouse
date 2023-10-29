from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "app_pages/home.html", context)


def about(request):
    context = {}
    return render(request, "app_pages/about.html", context)


def services(request):
    context = {}
    return render(request, "app_pages/services.html", context)


def contact(request):
    context = {}
    return render(request, "app_pages/contact.html", context)


def cars(request):
    context = {}
    return render(request, "app_pages/cars.html", context)
