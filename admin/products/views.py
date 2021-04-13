from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        # Query the data
        products = Product.objects.all()
        # Serialize the data
        serializer = ProductSerializer(products, many=True)
        # Return the serialized data into response
        return Response(serializer.data)
    
    def create(self, request):
        pass
    
    def retreive(self, request, pk=None):
        pass
    
    def update(self, request, pk=None):
        pass
    
    def destroy(self, request, pk=None):
        pass