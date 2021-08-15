from django.urls import path
from bouncer.views import landing


app_name = "bouncer"

urlpatterns = [
    path("", landing, name="landing"),
]
