from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/meetings/', include('meetings.urls')),
    path('admin/', admin.site.urls),
]