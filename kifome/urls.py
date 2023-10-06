
from django.urls import path

from kifome import views

urlpatterns = [
    path("", views.index, name="index"),

]