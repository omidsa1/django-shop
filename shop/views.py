from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from .models import *
from .serializers import *


@api_view(["GET"])
def overview(request):
    api_urls = {
        "Add": "/product/create",
        "List Products": "/product/view",
        "Update": "/product/update/pk",
        "Delete": "/product/pk/delete",
        "Search by Category": "/product/category/pk",
    }

    return Response(api_urls)


@api_view(["POST"])
def add_product(request):
    product = ProductSerializer(data=request.data)

    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This product already exists")

    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def view_products(request):

    if request.query_params:
        products = Product.objects.filter(**request.query_param.dict())
    else:
        products = Product.objects.all()

    if products:
        data = ProductSerializer(products)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    data = ProductSerializer(instance=product, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def view_products_by_category(request, category):

    if request.query_params:
        products = Product.objects.filter(category__name=category)
    else:
        products = Product.objects.none()

    if products:
        data = ProductSerializer(products)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
