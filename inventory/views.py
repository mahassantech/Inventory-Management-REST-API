from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class ProductView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        product_list=Product.objects.all()
        serializer=ProductSerializers(product_list,many=True)
        return Response (serializer.data) 
    
    def post(self,request):
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid(): 
            serializer.save(created_by=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        product_list=get_object_or_404(Product,pk=pk)
        serializer=ProductSerializers(product_list)
        return Response (serializer.data) 
    
    def put(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        product=get_object_or_404(Product, pk=pk)
        serializer=ProductSerializers(product, data=request.data, partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        product=get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)