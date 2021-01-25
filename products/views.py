from rest_framework import generics

from .models import (   Product,
                        P_Category,
                        P_Brand,
                        P_Color,
                        P_Size,
                        P_Image)
from .serializers import (  ProductSerializer,
                            PCategorySerializer,
                            PBrandSerializer,
                            PColorSerializer,
                            PSizeSerializer,
                            PImageSerializer)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PCategoryList(generics.ListCreateAPIView):
    queryset = P_Category.objects.all()
    serializer_class = PCategorySerializer

class PCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = P_Category.objects.all()
    serializer_class = PCategorySerializer

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

class PImageList(generics.ListCreateAPIView):
    queryset = P_Image.objects.all()
    serializer_class = PImageSerializer

class PImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = P_Image.objects.all()
    serializer_class = PImageSerializer