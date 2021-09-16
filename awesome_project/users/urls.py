# users/urls.py

from django import contrib
from django.conf.urls import url, include
from users.views import dashboard

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
]