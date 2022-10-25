from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import log_in


urlpatterns = [
    path('login/', log_in, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
