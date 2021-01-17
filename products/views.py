from rest_framework import generics

from .models import (   Product,
                        P_Category,
                        P_Brand,
                        P_Color,
                        P_Size,
                        P_Image)
from .serializers import (  ProductSerializer,
                            PCategorySerialier,
                            PBrandSerializer,
                            PColorSerializer,
                            PSizeSerializer,)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PCategoryList(generics.ListCreateAPIView):
    queryset = P_Category.objects.all()
    serializer_class = PCategorySerialier

class PCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = P_Category.objects.all()
    serializer_class = PCategorySerialier

class PBrandList(generics.ListCreateAPIView):
    queryset = P_Brand.objects.all()
    serializer_class = PBrandSerializer

class PBrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = P_Brand.objects.all()
    serializer_class = PBrandSerializer

class PColorList(generics.ListCreateAPIView):
    queryset = P_Color.objects.all()
    serializer_class = PColorSerializer

class PColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = P_Color.objects.all()
    serializer_class = PColorSerializer

class PSizeList(generics.ListCreateAPIView):
    queryset = P_Size.objects.all()
    serializer_class = PSizeSerializer

class PSizeDetail(generics.ListCreateAPIView):
    queryset = P_Size.objects.all()
    serializer_class = PSizeSerializer