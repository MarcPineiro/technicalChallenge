# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/users', views.create_user, name='create_user'),
    path('api/users/<int:user_id>', views.get_user, name='get_user'),
]
