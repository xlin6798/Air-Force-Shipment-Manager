from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('<str:un_code>/', views.details, name='details'),
    path('shipmentHistory', views.shipmentHistory, name='shipmentHistory'),
]