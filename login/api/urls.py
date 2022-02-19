from django.urls import path
from login.api.views import registration_view, login_view, home_page, logout_view

app_name = "register"

urlpatterns = [
    path('register', registration_view, name="register_page"),
    path('', login_view, name="login_page"),
    path('home', home_page, name="start_page"),
    path('logout', logout_view, name='logout_page')
]
