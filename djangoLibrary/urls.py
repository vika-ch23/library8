from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('home/', include('books.urls')),
    path('books/', include('books.urls'))
]
