from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
    path('deposit-products/<int:deposit_pk>/', views.deposit_detail),
    path('save-installment-products/', views.save_installment_savings_products),
    path('installment-savings-products/', views.installment_savings_products),
    path('installment-savings-products/<int:installment_pk>/', views.installment_detail),
    path('exchange/', views.exchange),
    path('recommend-service/', views.recommend),
    path('map/', views.map_info),
]