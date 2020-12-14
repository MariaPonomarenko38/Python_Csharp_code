from django.contrib import admin
from django.urls import include, path
from .views import MeetingsListView, OnlineMeetingDetailView

app_name = 'meeting'
urlpatterns = [
    path('meetings/', MeetingsListView.as_view()),
    path('meetings/<int:pk>/', OnlineMeetingDetailView.as_view()),
]
