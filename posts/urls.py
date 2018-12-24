from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("top/", views.top, name="top"),
    re_path(r"details/(?P<id>\d+)/$", views.details, name="details"),
]
