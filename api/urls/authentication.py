from django.urls import path
from api.views.authentication import login, register

urlpatterns = [
    path("login/", login),
    path("register/", register),
]
