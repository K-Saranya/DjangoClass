from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class ProductsCRUDAPI(APIView):
    def post(self, request):
        try:
            serializer = ProductsInfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Product Created Successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, productId=None):
        try:
            if productId:
                product = ProductsInfo.objects.get(id=productId)
                serializer = ProductsInfoSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                products = ProductsInfo.objects.all()
                serializer = ProductsInfoSerializer(products, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, productId):
        try:
            if productId:
                product = ProductsInfo.objects.get(id=productId)
                serializer = ProductsInfoSerializer(product, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"Product data Updated Successfully!", "data":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Id must"})
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
    def delete(self, request, productId):
        try:
            if productId:
                product = ProductsInfo.objects.get(id=productId)
                product.delete()
                return Response({"message":"Product data deleted Successfully!"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Id must"})
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)  
        

@api_view(["POST","GET","PUT","DELETE"])
def ProductsCRUDAPIFunction(request, productId=None):
    if request.method == "POST":
        try:
            serializer = ProductsInfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Product Created Successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "GET":
        try:
            if productId:
                product = ProductsInfo.objects.get(id=productId)
                serializer = ProductsInfoSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                products = ProductsInfo.objects.all()
                serializer = ProductsInfoSerializer(products, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProductsPOSTAPIGenerics(generics.ListCreateAPIView):
    queryset = ProductsInfo.objects.all()
    serializer_class = ProductsInfoSerializer
    
    
class ProductsUPDATEAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductsInfo.objects.all()
    serializer_class = ProductsInfoSerializer


class ProductsAPIViewset(ModelViewSet):
    queryset = ProductsInfo.objects.all()
    serializer_class = ProductsInfoSerializer