from django.urls import path
from app_pages import views

urlpatterns = [
    path("", views.home, name="app_pages__home"),
    path("about/", views.about, name="app_pages__about"),
    path("services/", views.services, name="app_pages__services"),
    path("contact/", views.contact, name="app_pages__contact"),
    path("cars/", views.cars, name="app_pages__cars"),
]
