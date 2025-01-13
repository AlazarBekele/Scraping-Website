from django.urls import path
from .views import index, body

urlpatterns = [
    path ('', body, name='Main'),
    path ('post/', index, name='index')
]
