from django.urls import path
from . import views

urlpatterns = [
    # We rely on django.contrib.auth.urls for login/logout
    # But we can override or add custom signup if needed.
    # We mainly need a home/dashboard router.
]
