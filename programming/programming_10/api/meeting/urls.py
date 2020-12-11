from django.contrib import admin
from django.urls import include, path
from .views import MeetingsView, OnlineMeetingDetailView

app_name = 'meeting'
urlpatterns = [
    path('collection/', MeetingsView.as_view()),
    path('collection/<int:pk>/', OnlineMeetingDetailView.as_view()),
]
