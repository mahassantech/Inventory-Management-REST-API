from django.urls import path 
from .views import CategoryView

urlpatterns = [
    path('all/',CategoryView.as_view(),name='category')
    
]
