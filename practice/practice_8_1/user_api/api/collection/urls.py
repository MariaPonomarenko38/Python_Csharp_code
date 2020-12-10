from django.contrib import admin
from django.urls import include, path
from .views import MeetingsListView, OnlineMeetingDetailView


app_name = 'collection'
urlpatterns = [
    path('collection/', MeetingsListView.as_view()),
    path('collection/<int:pk>/', OnlineMeetingDetailView.as_view()),
]
