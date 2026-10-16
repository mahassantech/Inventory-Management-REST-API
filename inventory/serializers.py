from rest_framework import serializers 
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    class Meta: 
        model= Product 
        fields= "__all__"
        read_only_fields=['created_by']