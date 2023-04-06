from django.urls import path

from . import views

urlpatterns = [
    path('', views.printer_list, name='printer_list'),
    path('<str:pk>/', views.printer_view, name='printer_view'),
]
