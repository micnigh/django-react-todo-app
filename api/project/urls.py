"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .settings.base import BASE_URL

# fix site url for admins
admin.site.site_url = f'/{BASE_URL}'

appUrlPatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('api.urls')),
]

# serve app urls under baseUrl
urlpatterns = [
    url(r'^{0}'.format(BASE_URL), include(appUrlPatterns))
]
