from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render


def home_page():
    return HttpResponseRedirect("home/")


@api_view(['POST', 'GET'])
def registration_view(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) is not None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)

        username = request.data.get('username')
        if validate_username(username) is not None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            return Response(data)

        user = User(username=username, email=email)
        password = request.data.get('password')
        user.set_password(password)
        user.save()

        data['response'] = 'successfully registered new user.'
        data['email'] = user.email
        data['username'] = user.username

        auth.login(request, user)
        return HttpResponseRedirect("home/")
        # return Response(data)


def validate_email(email):
    user = None
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    if user is not None:
        return email


def validate_username(username):
    user = None
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    if user is not None:
        return username


@api_view(['POST', 'GET'])
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        data = {}
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            data['response'] = 'Successfully authenticated.'
            data['username'] = username.lower()
            return HttpResponseRedirect("home/")
        else:
            # Отображение страницы с ошибкой
            data['response'] = 'Error'
            data['error_message'] = 'Invalid credentials'
            return HttpResponseRedirect("/api/account")
        # return Response(data)


@api_view(['GET', ])
def logout_view(request):
    if request.method == 'GET':
        auth.logout(request)
        # Перенаправление на страницу.
        return HttpResponseRedirect("/api/account")

