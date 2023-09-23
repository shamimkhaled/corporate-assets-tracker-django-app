from django.shortcuts import render
from assets.models import *
from .serializers import *
from rest_framework import viewsets


# Create the all views here.

# Create CompanyViewSet
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('company_name')
    serializer_class = CompanyModelSerializer


# Create EmployeeViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('full_name')
    serializer_class = EmployeeModelSerializer


# Create CategoryTypeViewSet
class CategoryTypeViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all().order_by('category_type')
    serializer_class = CategoryTypeModelSerializer


# Create SupplierViewSet
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('supplier_name')
    serializer_class = SupplierModelSerializer


# Create AssetsViewSet
class AssetsViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('title')
    serializer_class = AssetModelSerializer


# Create AssetAllocationViewSet 
class AssetAllocationViewSet(viewsets.ModelViewSet):
    queryset = AssetAllocation.objects.all().order_by('device')
    serializer_class = AssetAllocationModelSerializer