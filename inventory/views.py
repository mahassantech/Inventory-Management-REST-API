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
    
    def post(self,request):
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)