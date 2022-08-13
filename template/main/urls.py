from main.views import (
    views_auth,
    views_crash
)
from django.urls import path

urlpatterns = [
    path('api/crash', views_crash.break_on_purpose),
    path('api/whoami', views_auth.whoami),
    path('api/login', views_auth.login),
    path('api/logout', views_auth.logout),
]
