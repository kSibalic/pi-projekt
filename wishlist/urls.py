from django.urls import path

from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.index, name='index')
]