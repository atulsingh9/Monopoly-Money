from django.urls import path
from . import views

app_name = "monopoly_money"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard")
]