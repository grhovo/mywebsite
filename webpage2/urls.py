from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
]