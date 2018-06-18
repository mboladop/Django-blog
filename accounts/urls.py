from django.urls import path
from accounts.views import login, register, logout, profile

#ACCOUNTS
urlpatterns = [
    path('accounts/login', login, name = 'login'),
    path('^accounts/register', register, name = 'register'),
    path('^accounts/logout', logout, name = 'logout'),
    path('^accounts/profile', profile, name = 'profile')
    ]