from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    path('deposit-products/', views.deposit_products, name='deposit_products'),
    path('save-installment-savings_products/', views.save_installment_savings_products, name='save_installment_savings_products'),
    path('installment-savings_products/', views.installment_savings_products, name='installment_savings_products'),
]