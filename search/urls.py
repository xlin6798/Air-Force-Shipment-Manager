from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('source', views.source, name='source'),
    path('products/<str:un_code>/', views.detail, name='detail'),
    path('hazard', views.hazard, name='hazard'),
    path('shipmentHistory', views.shipmentHistory, name='shipmentHistory'),
]

