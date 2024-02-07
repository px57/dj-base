"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'info/', 
        views.info, 
        name='site__info'
    ),
]