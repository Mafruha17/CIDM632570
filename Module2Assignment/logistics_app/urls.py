# logistics_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_create, name='order_create'),
    path('predict/', views.predict_eta, name='predict_eta'),
]
# logistics_app/urls.py