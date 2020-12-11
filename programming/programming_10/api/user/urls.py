from django.contrib import admin
from django.urls import include, path
from .views import RegistrationAPIView, LogoutView


app_name = 'user'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
]
