from django.contrib import admin
from django.urls import include, path
from .views import OnlineMeetingCreateView, MeetingsListView, OnlineMeetingDetailView

app_name = 'meeting'
urlpatterns = [
    path('meeting/create/', OnlineMeetingCreateView.as_view()),
    path('meetings/', MeetingsListView.as_view()),
    path('meeting/detail/<int:pk>/', OnlineMeetingDetailView.as_view()),
]
