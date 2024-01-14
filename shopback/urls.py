from django.urls import path, include

from products import views

urlpatterns = [
    path('products/', include('products.urls')),
    path('index/<int:pk>/', views.index),
]
