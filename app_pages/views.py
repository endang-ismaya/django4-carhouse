from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "app_pages/home.html", context)
