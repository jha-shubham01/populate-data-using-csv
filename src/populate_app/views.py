
from rest_framework import serializers, viewsets

from .models import Product


# Serializer
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


# Viewset
class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
