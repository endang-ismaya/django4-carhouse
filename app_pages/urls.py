from django.urls import path
from app_pages import views

urlpatterns = [
    path("", views.home, name="app_pages__home"),
]
