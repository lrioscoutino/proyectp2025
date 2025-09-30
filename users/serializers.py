from rest_framework import serializers
from users.models import Product, DetailProduct


class DetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailProduct
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    products = DetailProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ("name", "stock", "is_active", "products")

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

