from django.urls import path
from TechVrDev import views

urlpatterns = [
    path(" ", views.TechVrDev, name="TechVrDev"),

    path("", views.TechVrDev_intex, name="TechVrDev_intex"),
    path("<int:pk>/", views.TechVrDev_detail, name="TechVrDev_detail"),
]