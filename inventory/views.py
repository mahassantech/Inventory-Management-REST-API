from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework import status

class ProductView(APIView):
    def get(self,request):
        product_list=Product.objects.all()
        serializer=ProductSerializers(product_list,many=True)
        return Response (serializer.data)