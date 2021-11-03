from main import views
from django.urls import path

urlpatterns = [
    path('api/crash', views.crash.break_on_purpose),
    path('api/whoami', views.auth.whoami),
    path('api/login', views.auth.login),
    path('api/logout', views.auth.logout),
]
