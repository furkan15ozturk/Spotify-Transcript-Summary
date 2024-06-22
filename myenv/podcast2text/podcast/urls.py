from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), # When the user goes to the root URL, the homepage view will be called.
    ]
