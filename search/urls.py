from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('source', views.source, name='source'),
    path('products/<int:pid>/', views.detail, name='detail'),
    path('hazard', views.hazard, name='hazard'),
    path('conversion', views.conversion, name='conversion'),
    path('shipmentHistory', views.shipmentHistory, name='shipmentHistory'),
]

