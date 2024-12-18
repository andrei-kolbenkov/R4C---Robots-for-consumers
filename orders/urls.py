from django.urls import path
from . import views

urlpatterns = [
    path('api/create_order/', views.create_order, name='create_order'),
    path('create_order/', views.create_order_view, name='create_order_view'),
]
