from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="authentication-home"),
    path('tenant/', include('tenant.urls'), name="tenant-app"),
    path('landlord/', include('landlord.urls'), name="landlord-app")
]
