from django.urls import path, include

urlpatterns = [
    path('UserManagement/', include('UserManagement.urls')),
    ]