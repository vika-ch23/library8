from django.urls import path, include
from . import views

urlpatterns = [
    path('api/account/', include('login.api.urls', 'login_api'))
]