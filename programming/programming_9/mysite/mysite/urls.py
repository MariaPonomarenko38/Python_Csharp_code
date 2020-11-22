from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('meetings.urls')),
    path('admin/', admin.site.urls),
]