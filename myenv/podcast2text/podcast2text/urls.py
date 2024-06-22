from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage), # When the user goes to the root URL, the homepage view will be called.
    path('about/', views.about), # When the user goes to the /about URL, the about view will be called.
]
