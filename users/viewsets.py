from rest_framework import viewsets
from users.serializers import ProductSerializer
from users.models import Product

class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    