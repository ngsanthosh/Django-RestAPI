
from django.contrib import admin
from django.urls import path, include
from api import urls
urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
