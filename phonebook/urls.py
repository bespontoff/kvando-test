"""kvando URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.EntryAddView.as_view(), name='add'),
    path('detail/<int:pk>/', views.EntryDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.EntryEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.EntryDeleteView.as_view(), name='delete'),
    path('search/', views.EntrySearchView.as_view(), name='search'),
]
