from django.urls import path
from TechVrDev import views

urlpatterns = [
    path("", views.TechVrDev, name="TechVrDev"),
]