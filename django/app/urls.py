"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from rest_framework.authtoken import views as drf_token_view

from api.views import HealthView


app_name = 'app'
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'i18n/', include('django.conf.urls.i18n')),
    path(r'api/v1/', include('api.urls', namespace="api")),
    path(r'api/v1/authentication/token',  drf_token_view.ObtainAuthToken.as_view(), name='auth'),
    path(r'', include('api.urls', namespace="api")),
]
