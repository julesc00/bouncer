
from django.urls import path, include

urlpatterns = [
    path("", include("bouncer.urls", namespace="bouncer")),
]
