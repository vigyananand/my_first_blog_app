from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from .views import home, post,category


urlpatterns = [
    path('home/', home),
    path('BLOG/<slug:url>',post),
    path('category/<slug:url>',category)
   
]