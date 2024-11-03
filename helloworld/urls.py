from django.urls import path

from . import views

urlpatterns = [
        path("", views.index_adal, name="index"),
        path("<user>", views.user, name="user"),
        ]

