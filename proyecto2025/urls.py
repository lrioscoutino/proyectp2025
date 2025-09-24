"""
URL configuration for proyecto2025 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import urls
from users.views import welcome, about
from django.contrib.auth.views import LoginView, LogoutView
from users.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(urls)),
    path('',
         LoginView.as_view(template_name="base.html"),
         name="login"
         ),
    path('logout/',
         LogoutView.as_view(),
         name="logout"
         ),
    path('about/', about, name="about" ),
    path('api/', include(router.urls)),
]
