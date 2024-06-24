from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home), # When the user goes to the /podcast URL, the podcast app's URLs will be included.
    path('aboutme', views.aboutMe), # When the user goes to the /podcast URL, the podcast app's URLs will be included.
    path('home', include('podcast.urls')), # When the user goes to the /podcast URL, the podcast app's URLs will be included.
]
