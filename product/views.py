from django.shortcuts import render

from django.http import Http404
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class ProductDetail(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductDetail(APIView):
    def get(self, request, name):
        try:
            product = Product.objects.get(product_name__iexact=name)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404("Product does not exist")


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDelete(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

