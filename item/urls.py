from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('items/<int:pk>/', views.detail, name='detail'),
    path('items/new/', views.new, name='new'),
    path('items/<int:pk>/delete/', views.delete, name='delete'),
    path('items/<int:pk>/edit/', views.edit, name='edit'),
    path('items/', views.items, name='items'),
    path('items/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('new_category/', views.new_category, name='new_category'),
    path('<int:pk>/delete_category/', views.delete_category, name='delete_category'),
    path('categories/', views.categories, name='categories'),
]