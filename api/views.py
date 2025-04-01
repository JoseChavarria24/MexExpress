from django.shortcuts import render
from shopApp.models import Product
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def get_all_products(request):
    queryset = Product.objects.all()
    json = serializers.serialize("json", queryset)
    return JsonResponse(json, safe=False)