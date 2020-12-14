from django.contrib import admin
from django.urls import include, path
from .views import OrderView, OrderDetailView


app_name = 'order'
urlpatterns = [
    path('orders/', OrderView.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),
]
