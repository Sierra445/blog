from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='blog-app-index'),
    path('add_post/', views.add_post, name='add-post')
]