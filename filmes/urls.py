from django.urls import path
from .views import busca_filme

urlpatterns = [
    path('busca_filme/', busca_filme, name='busca_filme'),
]