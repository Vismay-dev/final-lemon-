from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']

class MenuItemSerializer(serializers.ModelSerializer):
    
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # Method 1
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset = Category.objects.all(),
    #     write_only = True
    # )
    # category_name = serializers.StringRelatedField(
    #     source = 'category',
    #     read_only = True
    # )
    # Method 2
    # category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'price_after_tax', 'stock', 'category']
        # Method 3
        depth = 1
        
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
        
