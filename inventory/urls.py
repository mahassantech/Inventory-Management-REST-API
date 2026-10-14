from django.urls import path 
from .views import ProductView,ProductDetailView

urlpatterns = [
    path('products/',ProductView.as_view()),
    path('products/update/<int:pk>/',ProductDetailView.as_view()),
    
]
