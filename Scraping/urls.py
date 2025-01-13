from django.urls import path
from .views import index, body

urlpatterns = [
    path ('', index, name='index'),
    path ('index/', body, name='Main')
]
