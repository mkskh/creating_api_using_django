from django.shortcuts import render, redirect

from django.http import Http404
from django.urls import reverse
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


def redirect_home(request):
    return redirect(reverse('product:all'))


class ProductList(generics.ListAPIView):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class ProductDetail(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, name):
        try:
            product = Product.objects.get(product_name__iexact=name)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404("Product does not exist")


class ProductCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

