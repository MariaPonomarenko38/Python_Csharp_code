from django.contrib import admin
from django.urls import include, path
from .views import MeetingsListView, OnlineMeetingDetailView, RegistrationAPIView, LogoutView


app_name = 'collection'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('collection/', MeetingsListView.as_view()),
    path('collection/<int:pk>/', OnlineMeetingDetailView.as_view()),
]
