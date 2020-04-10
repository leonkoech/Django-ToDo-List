from django.urls import path
from . import views

urlpatterns = [
path("", views.view, name="index"),
path("view/", views.view, name="index"),
path("create/", views.get_name, name="index"),
path("<int:id>", views.index, name="index"),
]
