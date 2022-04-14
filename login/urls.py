from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('login.api.urls', 'login_api'))
]