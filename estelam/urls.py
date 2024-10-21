from django.urls import path
from .views import page, searchmaterials, searchcompanies
from . import views

urlpatterns = [
    path('', views.page, name="page"),
    path('materials/', views.searchmaterials, name="materials"),
    path('companies/', views.searchcompanies, name="companies"),
]