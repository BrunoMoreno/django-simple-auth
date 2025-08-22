"""
    With  this lines we include the default authentication URLs provided by Django.

    accounts/login/ [name='login']
    accounts/logout/ [name='logout']
    accounts/password_change/ [name='password_change']
    accounts/password_change/done/ [name='password_change_done']
    accounts/password_reset/ [name='password_reset']
    accounts/password_reset/done/ [name='password_reset_done']
    accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/reset/done/ [name='password_reset_complete']
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from accounts.urls import urlpatterns as accounts_urls  # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),  # new
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new    
]
