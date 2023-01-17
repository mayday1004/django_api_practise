from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.CreateUser.as_view(), name="create_user"),
]
