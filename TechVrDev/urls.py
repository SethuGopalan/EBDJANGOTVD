from django.urls import path
from TechVrDev import views

urlpatterns = [
    path("", views.TechVrDev, name="TechVrDev"),
    path("<int:pk>/", views.TechVrDev_detail, name="TechVrDev_detail"),
]