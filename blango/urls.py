"""blango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar
from django.conf import settings
from django.contrib import admin
import blog
from django.urls import path, include
import blango_auth.views

# for registration
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('ip/', blog.views.get_ip),
    path('accounts/', include('django.contrib.auth.urls')), # neeeded for 'login' url
    path("accounts/", include("allauth.urls")), # for allauth but django.contrib.auth.urls take precedence since both of them define some same rules (e.g. login/)
    path('accounts/profile/', blango_auth.views.profile, name='profile'),
    path(
        'accounts/register/',
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),
    path('accounts/', include("django_registration.backends.activation.urls")), #apparently this builds on top of the other include
    path('api/v1/', include('blog.api.urls')),
]

# only show django debug toolbar is debug is True in settings.py
if settings.DEBUG:
  urlpatterns += [
    path('__debug__/', include(debug_toolbar.urls)),
  ]
