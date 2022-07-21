from django.urls import path
from .views import *

from apps.home.views import home

app_name = 'post'

urlpatterns = [
    path('', home, name='home'),
    path('blog-single/<int:pk>/', blog_single, name='blog-single'),
    path('fashion/', fashion, name='fashion'),
    path('travel/', travel, name='travel'),
]
